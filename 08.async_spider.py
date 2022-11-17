# -*- coding = utf-8 -*-
# @Time: 2021/8/31 下午9:40
import asyncio
import aiohttp
import time

import blog_spider


async def async_craw(url):
    print('craw url:', url)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, verify_ssl=False)) as session:
        async with session.get(url) as res:
            result = await res.text()
            print(f'craw url:{url}, {len(result)}')


loop = asyncio.get_event_loop()

task = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]


if __name__ == '__main__':
    start = time.time()
    loop.run_until_complete(asyncio.wait(task))
    end = time.time()
    print('use time second:', end-start)
