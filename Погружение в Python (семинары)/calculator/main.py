import logging
import argparse

def calculate(expression):
    try:
        # Вычисление результата
        result = eval(expression)
        print(f'Результат: {result}')
        logging.info(f'Результат: {result}')
    except Exception as e:
        logging.error(f'Ошибка вычисления: {str(e)}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help="Математическое выражение, которое нужно вычислить")
    args = parser.parse_args()
    # Настройка логирования
    logging.basicConfig(filename='calculator.log', level=logging.INFO)
    
    calculate(args.expression)