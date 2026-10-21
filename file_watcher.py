from pathlib import Path
import shutil

# Define project folders
WATCH_FOLDER = Path("watch_folder")
ORGANIZED_FOLDER = Path("Organized")


def get_destination(file_path):
    extension = Path(file_path).suffix.lower()

    if extension == ".csv":
        return "Spreadsheets"

    elif extension == ".pdf":
        return "Documents"

    elif extension in [".jpg", ".jpeg", ".png"]:
        return "Images"

    else:
        return "Other"


def organize_file(file_path):
    file_path = Path(file_path)

    # Determine the destination folder
    folder_name = get_destination(file_path)

    # Build the complete destination path
    destination_folder = ORGANIZED_FOLDER / folder_name

    # Make sure the destination folder exists
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Move the file
    shutil.move(str(file_path), str(destination_folder / file_path.name))

    print(f"Moved {file_path.name} to {folder_name}")


for file_path in WATCH_FOLDER.iterdir():
    if file_path.is_file():
        organize_file(file_path)