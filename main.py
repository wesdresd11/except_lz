from excepts import ValidationError
from excepts import CheckingDataSet


def main():
    file = CheckingDataSet('D:\учеба\!2 семестр\ОМП\lab5\\var4.csv')        #функция main, создал обьект класса с путем к файлу
    try:                        #далее в порядке проверки использую методы класса
        file.file_open_read()   #сначала пытаемся открыть файл в указанной директории, если его там нет - ошибка 
                                #и выходим из фукнции, так как дальнейшие проверки бессмысленны
    except FileNotFoundError as e:
        print(e)
        return
    
    try:                            #чтобы словить все возможные ошибки отдельно проверяем каждую через try, структура не та, что ожидалась - ошибка
        file.structure_check()

    except ValidationError as e:
        print(e)
    
    try:                            #эта проверка тоже отдельно, не те типы данных в столбцах - ошибка
        file.columns_type_check()

    except TypeError as e:
        print(e)

    else:                           #если все проверки прошли успешно, то сообщаем об этом
        print('Чтение датафрейма завершено успешно.')


if __name__ == '__main__':
    main()