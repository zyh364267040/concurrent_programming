# -*- coding = utf-8 -*-
# @Time: 2021/8/31 下午8:39
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


primes = [112272535095293] * 100


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return False
    if num % 2 == 0:
        return False
    sqrt_num = int(math.floor(math.sqrt(num)))
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    return True


def single_thread():
    for num in primes:
        is_prime(num)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, primes)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, primes)


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print('single_thread, cost', end-start, 'second')

    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread, cost', end-start, 'second')

    start = time.time()
    multi_process()
    end = time.time()
    print('multi_process, cost', end-start, 'second')
