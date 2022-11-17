# -*- coding = utf-8 -*-
# @Time: 2021/8/30 下午9:52
import threading
import time

import blog_spider


def single_thread():
    print('multi_thread begin')
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print('multi_thread end')


def multi_thread():
    print('multi_thread begin')
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('multi_thread end')


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print('single_thread cost', end - start)

    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread cost', end - start)
