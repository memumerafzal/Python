import os

def rename_images(directory, prefix="12"):
    # Get a list of all files in the directory
    files = sorted([f for f in os.listdir(directory) if f.endswith('.jpg')])

    # Rename each file
    for i, filename in enumerate(files):
        new_name = f"{prefix}-{i+1:03}.jpg"
        source = os.path.join(directory, filename)
        destination = os.path.join(directory, new_name)
        os.rename(source, destination)

    print("Renaming completed.")

# Set the directory path
directory_path = "E:\Medical\DEC"
rename_images(directory_path)
