"""
train_model.py
==============
Trains EfficientNet-B0 on the PlantVillage dataset and saves the weights
as  leaf_disease_model.pth  in the current directory.

USAGE
-----
1. Download the PlantVillage dataset:
   • Kaggle: https://www.kaggle.com/datasets/emmarex/plantdisease
   • Or: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

2. Extract so the folder structure looks like:
       PlantVillage/
           Apple___Apple_scab/
               image1.jpg
               ...
           Apple___healthy/
               ...
           ...

3. Run:
       python train_model.py --data_dir PlantVillage --epochs 15 --batch_size 32

4. The trained model is saved as  leaf_disease_model.pth
"""

import os
import argparse
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.optim.lr_scheduler import CosineAnnealingLR
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader, random_split

# ─── Args ─────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Train EfficientNet-B0 on PlantVillage")
parser.add_argument("--data_dir",   default="PlantVillage", help="Path to dataset root")
parser.add_argument("--epochs",     type=int, default=15)
parser.add_argument("--batch_size", type=int, default=32)
parser.add_argument("--lr",         type=float, default=1e-3)
parser.add_argument("--val_split",  type=float, default=0.2)
parser.add_argument("--output",     default="leaf_disease_model.pth")
args = parser.parse_args()

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"▶ Using device: {DEVICE}")

# ─── Transforms ───────────────────────────────────────────────────────────────
train_tf = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.RandomRotation(30),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])
val_tf = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# ─── Dataset ──────────────────────────────────────────────────────────────────
print(f"▶ Loading dataset from: {args.data_dir}")
full_dataset = datasets.ImageFolder(args.data_dir, transform=train_tf)
num_classes  = len(full_dataset.classes)
print(f"  Found {len(full_dataset)} images across {num_classes} classes")
print(f"  Classes: {full_dataset.classes}")

# Save class names for the app
import json
with open("class_names.json", "w") as f:
    json.dump(full_dataset.classes, f, indent=2)
print("  ✓ Saved class_names.json")

# Train / val split
val_size   = int(len(full_dataset) * args.val_split)
train_size = len(full_dataset) - val_size
train_ds, val_ds = random_split(full_dataset, [train_size, val_size])
val_ds.dataset = datasets.ImageFolder(args.data_dir, transform=val_tf)

train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,  num_workers=4, pin_memory=True)
val_loader   = DataLoader(val_ds,   batch_size=args.batch_size, shuffle=False, num_workers=4, pin_memory=True)

# ─── Model ────────────────────────────────────────────────────────────────────
print("▶ Building EfficientNet-B0 …")
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)

# Freeze backbone; only train classifier head initially
for param in model.parameters():
    param.requires_grad = False

model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
model = model.to(DEVICE)

# ─── Training Loop ────────────────────────────────────────────────────────────
criterion = nn.CrossEntropyLoss()
optimizer = Adam(model.classifier.parameters(), lr=args.lr)
scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)

best_val_acc = 0.0

print(f"\n▶ Starting training for {args.epochs} epochs …\n")
for epoch in range(1, args.epochs + 1):
    # ── Unfreeze all after 5 epochs for fine-tuning ──
    if epoch == 6:
        for param in model.parameters():
            param.requires_grad = True
        optimizer = Adam(model.parameters(), lr=args.lr * 0.1)
        scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs - 5)
        print("  ↳ Unfroze all layers for fine-tuning\n")

    # Train
    model.train()
    train_loss, train_correct, train_total = 0.0, 0, 0
    for batch_idx, (images, labels) in enumerate(train_loader):
        images, labels = images.to(DEVICE), labels.to(DEVICE)
        optimizer.zero_grad()
        outputs = model(images)
        loss    = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss    += loss.item() * images.size(0)
        preds          = outputs.argmax(dim=1)
        train_correct += (preds == labels).sum().item()
        train_total   += images.size(0)

        if (batch_idx + 1) % 20 == 0:
            print(f"  Epoch {epoch}/{args.epochs} | Batch {batch_idx+1}/{len(train_loader)} "
                  f"| Loss: {loss.item():.4f}", end="\r")

    train_loss /= train_total
    train_acc   = 100 * train_correct / train_total

    # Validate
    model.eval()
    val_correct, val_total = 0, 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            preds   = outputs.argmax(dim=1)
            val_correct += (preds == labels).sum().item()
            val_total   += images.size(0)

    val_acc = 100 * val_correct / val_total
    scheduler.step()

    print(f"  Epoch {epoch:02d}/{args.epochs} | "
          f"Train Loss: {train_loss:.4f} | "
          f"Train Acc: {train_acc:.2f}% | "
          f"Val Acc: {val_acc:.2f}%")

    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), args.output)
        print(f"  ✓ New best model saved → {args.output}  (Val Acc: {val_acc:.2f}%)")

print(f"\n✅ Training complete! Best Val Accuracy: {best_val_acc:.2f}%")
print(f"   Model saved to: {args.output}")
