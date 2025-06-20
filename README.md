## Парсер csv-документа с функциями фильтрации и агрегации по полям
#### Автор: Поздняков Евгений (https://github.com/PozdnyakovE)

### Как развернуть локально:
Клонируйте репозиторий к себе на компьютер:
```
git clone https://github.com/PozdnyakovE/csv_file_parser.git
```
В корневой папке нужно создать виртуальное окружение и установить зависимости.
```
python -m venv venv
```
```
pip install -r requirements.txt
```
### запустить файл main.py с необходимыми параметрами
```
python main.py [аргументы]
```
### Параметры запуска парсера
Обязательный аргумент, указывается имя файла или ссылка на него.
```
-f или --file 
Пример: python main.py -f products.csv  
```
Аргумент фильтрации, указывается поле и тип фильтрации.
```
-w или --where 
Пример: python main.py -f products.csv -w "price>200" 
```
Аргумент агрегации, указывается поле (числовое) и тип агрегации.
```
-w или --where 
Пример: python main.py -f products.csv -w "price>200" -a "price=avg" 
```
### Пример работы
![Иллюстрация к проекту](https://github.com/PozdnyakovE/csv_file_parser/blob/master/csv_parser_results.jpg)
