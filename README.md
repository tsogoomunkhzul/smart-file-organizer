# Smart File Organizer

A Python automation project that monitors a folder and automatically
organizes new files based on their file extensions.

## Features

- Automatically detects newly created files.
- Organizes files by extension.
- Supports CSV, PDF, JPG, JPEG, and PNG files.
- Moves other file types into an Other folder.
- Uses watchdog to monitor file system events.
- Prevents overwriting existing files with the same name.

## Technologies

- Python
- Watchdog
- pathlib
- shutil

## Project Structure

    smart-file-organizer/
    ├── file_watcher.py
    ├── watch_folder/
    └── Organized/
        ├── Spreadsheets/
        ├── Documents/
        ├── Images/
        └── Other/

## Installation

1. Clone this repository.
2. Create a virtual environment:

       python3 -m venv .venv

3. Activate the environment on Linux:

       source .venv/bin/activate

4. Install the dependency:

       python -m pip install watchdog

## Usage

Run the application:

    python file_watcher.py

Add a file to the watch_folder directory.

The application will detect the new file and move it into the
appropriate folder inside Organized.

Press Ctrl+C to stop the application.

## Future Improvements

- Handle files that are still being written.
- Add logging.
- Support configurable file organization rules.
- Handle additional file types.
