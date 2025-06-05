import csv
import zipfile
from io import BytesIO
from io import TextIOWrapper
import PyPDF2
import pandas as pd


# создаём ZIP-архив в режиме записи
def test_create_arhive():
    with zipfile.ZipFile('my_archive.zip', 'w') as zipf:
    # Добавляем каждый файл по отдельности
        zipf.write('One.csv')
        zipf.write('Two.pdf')
        zipf.write('Three.xlsx')
    with zipfile.ZipFile('my_archive.zip', 'r') as zipf:
        print(zipf.namelist())

def test_csv_one():
    with zipfile.ZipFile('C:/Users/user/Desktop/Files_Phyton/my_archive.zip') as zip_file: # открываем архив
        with zip_file.open('One.csv') as csv_file: # открываем файл в архиве
            csvreader = list(csv.reader(TextIOWrapper(csv_file, 'utf-8-sig'))) # читаем содержимое файла и преобразуем его в список и декодируем его если в файле есть символы не из английского алфавита
            second_row = csvreader[0] # получаем первую строку

            assert second_row[0] == 'Roma' # проверка значения элемента в первом столбце второй строки
            assert second_row[1] == '28' # проверка значения элемента во втором столбце второй строки
            assert second_row[2] == 'Moscow' # проверка значения элемента во втором столбце второй строки

def test_xlsx_three():
    with zipfile.ZipFile('C:/Users/user/Desktop/Files_Phyton/my_archive.zip') as zip_file:  # открываем архив

        with zip_file.open('Three.xlsx') as xlsx_file:

            xlsx_data = BytesIO(xlsx_file.read()) # Читаем содержимое файла в память (BytesIO)


            df = pd.read_excel(xlsx_data, engine='openpyxl', header=None) # Загружаем Excel-файл в pandas. Добавляя что нет заголовков
            first_row = df.iloc[0].tolist() # Проверяем первую строку (индекс 0)
    assert first_row == ['Roma', 28, 'Moscow']


def test_pdf_two():
    with zipfile.ZipFile('C:/Users/user/Desktop/Files_Phyton/my_archive.zip') as zip_file: # открываем архив

        with zip_file.open('Two.pdf') as pdf_file: # Открываем PDF-файл из архива
            pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read())) # Загружаем PDF в байтах в PyPDF2
            page_text = pdf_reader.pages[0].extract_text()      # Извлекаем весь текст из первой страницы

    assert "Roma" in page_text
    assert "28" in page_text
    assert "Moscow" in page_text


# путь C:/Users/user/Desktop/Files_Phyton
