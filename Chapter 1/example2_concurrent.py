import concurrent.futures
from timeit import default_timer as timer


def f(x):
    return x * x - x + 1


def concurrent_f(x):
    global result
    result = f(result)


start = timer()
result = 3

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(concurrent_f, x) for x in range(20)]

    _ = concurrent.futures.as_completed(futures)

print('Result is very large. Only printing the last digits:', result % 100000)
print('Sequential took: %.2f seconds' % (timer() - start))
