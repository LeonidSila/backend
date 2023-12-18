
import sys
import logging

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            logging.info("Треугольник существует и является равносторонним.")
        elif a == b or a == c or b == c:
            logging.info("Треугольник существует и является равнобедренным.")
        else:
            logging.info("Треугольник существует и является разносторонним.")
    else:
        logging.error("Треугольник с указанными сторонами не существует.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            check_triangle(a, b, c)
        except ValueError:
            logging.error("Некорректные параметры. Введите длины сторон треугольника a, b и c через пробел.")
    else:
        logging.error("Некорректные параметры. Введите длины сторон треугольника a, b и c через пробел.")