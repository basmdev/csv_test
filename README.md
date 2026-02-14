# Тестовое задание для StafIT
## Скрипт для обработки CSV-файлов
### Установка
```
cd csv_test
pip install -r requirements.txt
```
### Инструкция по запуску
Скрипт запускается с аргументами **-f, --files** (указывается путь к одному или нескольким файлам) и **-r, --report** (указывается тип отчета, на данный момент доступен только average-gdp).
```
python main.py -f economic1.csv economic2.csv -r average-gdp
```
<img width="568" height="189" alt="image" src="https://github.com/user-attachments/assets/ff7ca6bd-c092-45fb-82ec-4fc492756876" />
В случае указания несуществующего типа отчета, выводится ошибка со списком доступных отчетов.
<img width="825" height="94" alt="image" src="https://github.com/user-attachments/assets/83d3cd2a-595b-491a-8262-6b6887aa57e5" />
