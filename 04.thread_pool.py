# -*- coding = utf-8 -*-
# @Time: 2021/8/31 上午12:09
import concurrent.futures

import blog_spider


# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():
    #     print(url, future.result())

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())


# if __name__ == '__main__':
    
