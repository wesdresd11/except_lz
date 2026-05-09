#Вариант 4
import os.path
import pandas as pd


class ValidationError(Exception): #Пользовательское исключение, из лекции
    pass

class CheckingDataSet:                      #Класс проверки датасета
    def __init__(self, file_path):              #конструктор, путь к файлу, прописал ожидаемые структуру и тип данных в столбцах
        self.file_path = file_path              #ипользовал типы данных pandas
        self.structure = [
            "Участники гражданского оборота",
            "Тип операции", "Сумма операции",
            "Вид расчета", "Место оплаты",
            "Терминал оплаты",
            "Дата оплаты",
            "Время оплаты",
            "Результат операции",
            "Cash-back",
            "Сумма cash-back"
        ]
        self.data_types = ['object', 'object', 'float64', 'object', 'object', 'object', 'object', 'object', 'object', 'object', 'float64']
        self.errors_str = ""            #пустая строка для записи в нее ошибок в типах данных столбцов


    def file_open_read(self):
        #https://ru.stackoverflow.com/questions/414593/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0
        if os.path.isfile(self.file_path) == False:         #проверка на существование файла в указанной директории, если файла в директории нет, то ошибка
            raise FileNotFoundError(f"Возникла следующая ошибка: [Errno 2] No such file or directory: {self.file_path}")
        else:
            self.dataset = pd.read_csv(self.file_path) #если файл есть, то открываем его и проверяем на пустоту, где len кол-во строк датафрейма, если 0, то ошибка пустого датафрейма
            if len(self.dataset) == 0:
                raise ValidationError("Возникла следующая ошибка: Датафрейм пуст")
    

    def structure_check(self):              #проверяем структуру датасета
        self.columns = self.dataset.columns.to_list()           #получаю в виде списка все названия колонн датасета 
        if self.columns != self.structure:                      #и сравниваю с ожидаемыми названиями
            raise ValidationError("Структура датафрейма не соответствует ожидаемой:\n"      #если названия не совпали - ошибка
            "- Названия столбцов не совпадают.\n"
            f"Ожидаемые: {self.structure}\n"
            f"Фактические: {self.columns}")
    
    def columns_type_check(self):               #проверка на типы данных в колоннах
        #https://stackoverflow.com/questions/68787511/how-to-get-the-column-types-of-a-dataframe-into-a-list
        self.types = self.dataset.dtypes.astype(str).tolist()           #получил типы данных колонн в список 
        for i in range(len(self.types)):                   #проревка ожидаемого типа данных с реальным для каждой колонки
            if self.data_types[i] != self.types[i]:             #если типы не совпали, то добавляем об этом запись в строку с ошибками
                self.errors_str += (f"В столбце {self.columns[i]} тип данных не соответствует ожидаемому\n"     #а не сразу поднимаем ошибку, чтобы проверить на
                f"Ожидается {self.data_types[i]}, Фактически {self.types[i]}\n")                                #наличие ошибки типа данных все столбцы
        
        if len(self.errors_str) != 0:           #если у нас ыла хотя бы одна ошибка, то строка с ошибками не будет пустой, поэтому если она не пуста - есть ошибка
            raise ValidationError(self.errors_str)