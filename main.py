from excepts import ValidationError
from excepts import CheckingDataSet


def main():
    file = CheckingDataSet('D:\учеба\!2 семестр\ОМП\lab5\\var4.csv')        #функция main, создал обьект класса с путем к файлу
    try:                        #далее в порядке проверки использую методы класса
        file.file_open_read()   #проверка идет в порядке написания, здесь это удобно, потому что если есть файл не открылся или пуст, то 
        file.structure_check()  #дальнейшие проверки бессмысленны

    except FileNotFoundError as e:
        print(e)

    except ValidationError as e:
        print(e)
    
    try:                            #эта проверка отдельно, т.к. в задании лабы указано обработать все возможные ошибки датасета
        file.columns_type_check()

    except ValidationError as e:
        print(e)

    else:                           #если все проверки прошли успешно, то сообщаем об этом
        print('Чтение датафрейма завершено успешно.')


if __name__ == '__main__':
    main()