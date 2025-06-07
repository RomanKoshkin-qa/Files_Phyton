import os.path


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, 'my_files')
ARCHIVE_DIR = os.path.join(CURRENT_DIR, 'resources')
ZIP_DIR = os.path.join(ARCHIVE_DIR, 'my_archive.zip')