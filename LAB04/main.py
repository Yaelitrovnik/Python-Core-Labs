import csv
import json
from datetime import datetime
from pathlib import Path
import shutil

# === Reading from a file ===
from pathlib import Path

print("Reading from input.txt:")
base_dir = Path(__file__).parent
input_path = base_dir / "input.txt"

try:
    with input_path.open("r") as file:
        content = file.read()
        print("--- File Content ---")
        print(content)
except FileNotFoundError:
    print("Error: input.txt not found!")


# === Writing to a new file ===
print("\nWriting to output.txt (overwrite mode)...")
with open("output.txt", "w") as file:
    file.write("First line of output.\n")
    file.write("Second line of output.\n")

# === Appending to a file ===
print("Appending to output.txt...")
with open("output.txt", "a") as file:
    file.write("Third line appended.\n")
    file.write("Fourth line appended.\n")

# === Handling file not found error ===
print("\nError Handling:")
try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File 'missing.txt' was not found.")

# === Bonus: Reading file line-by-line with line numbers ===
print("\nReading input.txt line by line:")
try:
    with (base_dir / "input.txt").open("r") as file:
        for idx, line in enumerate(file, start=1):
            print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print("Error: input.txt not found!")

# === Extra Challenge: CSV ===
# Create CSV
print("\nCreating data.csv with sample data...")
csv_filename = "data.csv"
with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Dana", "30", "Tel Aviv"])
    writer.writerow(["Tom", "25", "Jerusalem"])
    writer.writerow(["Leah", "27", "Haifa"])

# Read CSV manually
print("\nReading data.csv manually:")
with open(csv_filename, "r") as f:
    for line in f:
        print(line.strip())

# Read CSV with csv module
print("\nReading data.csv using csv.DictReader:")
with open(csv_filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old from {row['City']}")

# ---Extention Tasks---

# === Read and write binary files (image copy) ===
print("\n Binary file copy (if file exists)...")
image_path = base_dir / "sample_image.jpg"
image_copy_path = base_dir / "copy_image.jpg"
try:
    with image_path.open("rb") as src, image_copy_path.open("wb") as dst:
        dst.write(src.read())
    print(f"Copied {image_path.name} to {image_copy_path.name}")
except FileNotFoundError:
    print(f"{image_path.name} not found – skipping binary copy")


# === JSON read/write ===
print("\nWorking with JSON:")
data = {"name": "Dana", "age": 30, "languages": ["Python", "JavaScript"]}
json_filename = "data.json"
with open(json_filename, "w") as f:
    json.dump(data, f)

with open(json_filename, "r") as f:
    loaded = json.load(f)
    print(f"Loaded from JSON: {loaded}")

# === Count words in a text file ===
def count_words(filename):
    try:
        with filename.open("r") as f:
            text = f.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return 0

print(f"\nWord count in input.txt: {count_words(base_dir / 'input.txt')}")

# === Simple log parser ===
print("\nLog Parser:")
log_file = "sample.log"
with open(log_file, "w") as log:
    log.write("ERROR: Something went wrong\n")
    log.write("INFO: All good\n")
    log.write("WARNING: Check this\n")

with open(log_file, "r") as f:
    for line in f:
        if "ERROR" in line:
            print(f"Error Found: {line.strip()}")

# === File backup with timestamp ===
def backup_file(filename):
    if Path(filename).exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{filename}_{timestamp}.bak"
        shutil.copy(filename, new_name)
        print(f"Backup created: {new_name}")
    else:
        print(f"File {filename} does not exist.")

backup_file("output.txt")

# === Pathlib for modern path handling ===
print("\nPathlib Demo:")
path = base_dir / "input.txt"
if path.exists():
    print(f"File name: {path.name}")
    print(f"File path: {path.resolve()}")
    print(f"Parent directory: {path.parent}")
else:
    print("input.txt does not exist.")

