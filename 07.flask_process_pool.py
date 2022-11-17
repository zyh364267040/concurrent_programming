# -*- coding = utf-8 -*-
# @Time: 2021/8/31 下午9:10
import flask
import math
import json
from concurrent.futures import ProcessPoolExecutor


app = flask.Flask(__name__)


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


@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    num_list = [int(x) for x in numbers.split(',')]
    results = process_pool.map(is_prime, num_list)
    return json.dumps(dict(zip(num_list, results)))


if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()
    app.run()
