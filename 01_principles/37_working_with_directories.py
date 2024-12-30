from pathlib import Path

# path = Path("emails")
# path.exists()

# Create a directory
# path.mkdir()

# Remove directory
# path.rmdir()

path = Path()
files = path.glob("*.py")

for file in files:
    print(file)