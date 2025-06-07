import os
import shutil
import zipfile
import pytest


from script_os import FILES_DIR, ZIP_DIR, ARCHIVE_DIR

@pytest.fixture(scope="session", autouse=True)
def create_archive():
    if not os.path.exists(ARCHIVE_DIR):  # проверяем существует ли папка
        os.mkdir(ARCHIVE_DIR)  # создаем папку если её нет
        with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создаем архив
            for file in os.listdir(FILES_DIR): zf.write(os.path.join(FILES_DIR, file), file) # добавляем файлы в архив
    yield
    shutil.rmtree(ARCHIVE_DIR)