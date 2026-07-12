# Verify the dataset
import os

dataset_path = "dataset"

for split in ["train", "val", "test"]:
    print(f"\n{split.upper()}")

    split_path = os.path.join(dataset_path, split)

    for cls in os.listdir(split_path):
        class_path = os.path.join(split_path, cls)
        print(f"{cls}: {len(os.listdir(class_path))} images")