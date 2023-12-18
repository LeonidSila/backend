
import os
import logging

def get_file_info(file_path):
    # Получаем путь, имя файла и расширение с помощью функций модуля os.path
    path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    file_name_without_ext, ext = os.path.splitext(file_name)
    
    # Логирование ошибок
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    try:
        # Логирование полезной информации
        logging.info(f"Получена информация для файла: {file_path}")
    except Exception as e:
        # Логирование ошибок
        logging.error(f"Ошибка при получении информации о файле: {e}")
    
    return path, file_name_without_ext, ext

if __name__ == '__main__':
    import sys
    
    # Проверяем, получены ли аргументы командной строки
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        file_info = get_file_info(file_path)
        
        print("Путь:", file_info[0])
        print("Имя файла:", file_info[1])
        print("Расширение файла:", file_info[2])
    else:
        print("Необходимо передать аргумент - путь до файла.")
