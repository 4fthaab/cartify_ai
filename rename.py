import os

# 🔴 CHANGE THIS PATH if needed
LABELS_DIR = r"C:\Users\AfthabRAHMAN\Desktop\PJct\AI Model\datasets\labels\val"

# Collect only valid label files
label_files = []

for f in os.listdir(LABELS_DIR):
    if not f.lower().endswith(".txt"):
        continue

    # Skip classes.txt and its copies
    if "classes" in f.lower():
        continue

    label_files.append(f)

# Sort for consistency
label_files.sort()

print(f"Found {len(label_files)} label files")

# Rename sequentially
for idx, filename in enumerate(label_files, start=1):
    new_name = f"img_{idx:04d}.txt"

    old_path = os.path.join(LABELS_DIR, filename)
    new_path = os.path.join(LABELS_DIR, new_name)

    # Safety check: avoid overwrite
    if os.path.exists(new_path):
        print(f"⚠ Skipping (already exists): {new_name}")
        continue

    os.rename(old_path, new_path)
    print(f"✔ {filename} → {new_name}")

print("\n✅ Renaming completed safely.")
