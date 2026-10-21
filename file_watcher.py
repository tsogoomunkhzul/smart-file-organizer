from pathlib import Path
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Define our project folders
WATCH_FOLDER = Path("watch_folder").resolve()
ORGANIZED_FOLDER = Path("Organized").resolve()


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

    # Ignore files that no longer exist
    if not file_path.is_file():
        return

    # Determine the destination
    folder_name = get_destination(file_path)

    destination_folder = ORGANIZED_FOLDER / folder_name
    destination_folder.mkdir(parents=True, exist_ok=True)

    destination_path = destination_folder / file_path.name

    # Avoid overwriting an existing file
    if destination_path.exists():
        print(f"Skipped {file_path.name}: destination already exists.")
        return

    try:
        shutil.move(str(file_path), str(destination_path))
        print(f"Moved {file_path.name} to {folder_name}")

    except OSError as error:
        print(f"Could not move {file_path.name}: {error}")


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        # Ignore directories
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        print(f"New file detected: {file_path.name}")

        # Give the application that created the file time to finish writing
        time.sleep(1)

        organize_file(file_path)


def main():
    # Make sure the watched folder exists
    WATCH_FOLDER.mkdir(parents=True, exist_ok=True)

    # Create the event handler
    event_handler = FileHandler()

    # Create the folder observer
    observer = Observer()

    # Tell the observer which folder to watch
    observer.schedule(
        event_handler,
        str(WATCH_FOLDER),
        recursive=False
    )

    # Start watching
    observer.start()

    print("Smart File Organizer is running!")
    print(f"Watching folder: {WATCH_FOLDER}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping file watcher...")

        observer.stop()

    observer.join()

    print("File watcher stopped.")


if __name__ == "__main__":
    main()