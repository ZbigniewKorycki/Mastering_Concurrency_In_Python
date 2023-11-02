import concurrent.futures
from math import sqrt
from timeit import default_timer as timer
from concurrent import futures
import time


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(sqrt(x) + 1)
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return True


input_numbers = [i for i in range(10 ** 13, 10 ** 13 + 500)]


if __name__ == '__main__':
    start = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        futures_x = [executor.submit(is_prime, i) for i in input_numbers]
        for i, future in enumerate(concurrent.futures.as_completed(futures_x)):
            if future.result():
                result.append(input_numbers[i])

    print('Result 2:', result)
    print('It took %.2f seconds' % (timer() - start))

    