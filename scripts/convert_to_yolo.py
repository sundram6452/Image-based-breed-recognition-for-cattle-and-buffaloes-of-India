import os
import pandas as pd
import shutil

# Path setup
dataset_path = r"C:\Users\kumar\OneDrive\Desktop\cattles\dataset\test"
csv_file = os.path.join(dataset_path, "_classes.csv")
output_dir = os.path.join(dataset_path, "sorted")

os.makedirs(output_dir, exist_ok=True)

# Load CSV
df = pd.read_csv(csv_file)

# Get class columns (ignore 'filename')
class_columns = [c for c in df.columns if c != "filename"]

for _, row in df.iterrows():
    filename = row["filename"]
    src = os.path.join(dataset_path, filename)

    # Find which class = 1
    for cls in class_columns:
        if row[cls] == 1:
            class_folder = os.path.join(output_dir, cls)
            os.makedirs(class_folder, exist_ok=True)

            # Copy (or move) file
            dst = os.path.join(class_folder, filename)
            shutil.copy(src, dst)   # change to shutil.move() if you want to move
            break

print("✅ Images sorted into class folders at:", output_dir)
