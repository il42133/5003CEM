# code adapted from https://www.geeksforgeeks.org/processpoolexecutor-class-in-python/
# and https://superfastpython.com/processpoolexecutor-in-python/
# and https://stackoverflow.com/questions/1740726/turn-string-into-operator

from concurrent.futures import ProcessPoolExecutor
import operator
import time

OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def calc(x, y, opr):
    print("{} {} {} = {}".format(x, opr, y, OPS[opr](x, y)))


if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a number.")

    while True:
        try:
            num2 = int(input("Enter another number: "))
            break
        except ValueError:
            print("Please enter a number.")

    start = time.perf_counter()
    for op in OPS:
        calc(num1, num2, op)
    print("{}s\n".format(time.perf_counter() - start))

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=1) as exe:
        future = [exe.submit(calc, num1, num2, op) for op in OPS]
    print("{}s\n".format(time.perf_counter() - start))
