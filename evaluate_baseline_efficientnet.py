"""
evaluate_baseline_efficientnet.py
==================================
Comprehensive evaluation for the ORIGINAL EfficientNet-B0 model — the one
saved by the old train_model.py as a raw state_dict (torch.save(model.state_dict(), ...)),
not the newer checkpoint-dict format used by the ConvNeXt-Tiny version.

Produces the same evaluation artifacts as evaluate_model.py (confusion matrix,
per-class precision/recall/F1, top confused pairs) so this project has a real
evaluation section too, not just a headline accuracy number.

USAGE
-----
    python evaluate_baseline_efficientnet.py --data_dir PlantVillage \
        --checkpoint leaf_disease_model.pth --class_names class_names.json

NOTE ON REPRODUCIBILITY: the original train_model.py did not set a random
seed, so this script's val split will not be pixel-identical to whatever
split the original model was trained/validated on. That's fine — this is
an honest, freshly-drawn evaluation split, and worth stating as-is rather
than implying it matches the original training run exactly.
"""

import os
import json
import argparse

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import models, datasets, transforms

from sklearn.metrics import confusion_matrix, classification_report
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--checkpoint", required=True, help="Path to the raw state_dict .pth file")
    parser.add_argument("--class_names", default="class_names.json",
                         help="Path to class_names.json saved alongside the model")
    parser.add_argument("--batch_size", type=int, default=32)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs("results", exist_ok=True)

    with open(args.class_names) as f:
        class_names = json.load(f)
    num_classes = len(class_names)

    # ── Rebuild EfficientNet-B0 exactly as the old train_model.py did ──
    model = models.efficientnet_b0(weights=None)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    state_dict = torch.load(args.checkpoint, map_location="cpu")
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()

    # ── Same preprocessing as the original app/training script ──
    val_tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

    # Load the validation dataset directly
    val_dataset = datasets.ImageFolder(args.data_dir, transform=val_tf)

    assert val_dataset.classes == class_names, (
       "Dataset class order does not match class_names.json.\n"
       "Check that you are using the correct validation folder and class_names.json."
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=2,
        pin_memory=torch.cuda.is_available()
    )

    print(f"Validation images: {len(val_dataset)}")
    print(f"Number of classes: {len(class_names)}")

    # ── Run inference ──
    y_true, y_pred = [], []
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            logits = model(images)
            preds = logits.argmax(dim=1).cpu().numpy()
            y_pred.extend(preds)
            y_true.extend(labels.numpy())
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    # ── Classification report ──
    report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True, zero_division=0)
    with open("results/baseline_classification_report.json", "w") as f:
        json.dump(report, f, indent=2)
    pd.DataFrame(report).transpose().to_csv("results/baseline_classification_report.csv")

    overall_acc = report["accuracy"] * 100
    print(f"EfficientNet-B0 overall accuracy: {overall_acc:.2f}%")
    print(f"Macro F1: {report['macro avg']['f1-score']:.4f}")

    # ── Confusion matrix ──
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(16, 14))
    sns.heatmap(cm, cmap="viridis", xticklabels=class_names, yticklabels=class_names)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"Confusion Matrix — EfficientNet-B0 (Acc: {overall_acc:.2f}%)")
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(rotation=0, fontsize=6)
    plt.tight_layout()
    plt.savefig("results/baseline_confusion_matrix.png", dpi=150)
    print("Saved results/baseline_confusion_matrix.png")

    # ── Top confused pairs ──
    cm_no_diag = cm.copy().astype(float)
    np.fill_diagonal(cm_no_diag, 0)
    top_confusions = []
    idxs = np.dstack(np.unravel_index(np.argsort(-cm_no_diag.ravel()), cm_no_diag.shape))[0][:10]
    for i, j in idxs:
        if cm_no_diag[i, j] > 0:
            top_confusions.append({
                "true_class": class_names[i],
                "predicted_as": class_names[j],
                "count": int(cm[i, j])
            })
    with open("results/baseline_top_confusions.json", "w") as f:
        json.dump(top_confusions, f, indent=2)

    print("\nTop confused class pairs:")
    for c in top_confusions[:5]:
        print(f"  {c['true_class']} -> predicted as {c['predicted_as']} ({c['count']} times)")


if __name__ == "__main__":
    main()
