from loguru import logger

def fib(num):
    if num == 0 or num == 1:
        return num

    return fib(num-1) + fib(num-2)

num = int(input("Enter the Num:"))

logger.info(fib(num))