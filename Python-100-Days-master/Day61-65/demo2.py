'''
Author: hxy 1305149167@qq.com
Date: 2023-05-08 23:15:08
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-05-08 23:43:57
FilePath: /Python-100-Days-master/Day61-65/demo2.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import re
import asyncio
import aiohttp
from aiohttp import ClientSession

TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.DOTALL)

async def fetch_page_title(url):
    async with ClientSession(headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }) as session:
    
        async with session.get(url, ssl=False) as resp:
            try:
                if resp.status == 200:
                    html_code = await resp.text()
                    matcher = TITLE_PATTERN.search(html_code)
                    title = matcher.group(1).strip()
                    print(title)
            except Exception as e:
                print(e)


def main():
    urls = [
        'https://www.python.org/',
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://git-scm.com/',
        'https://www.sohu.com/',
        'https://gitee.com/',
        'https://www.amazon.com/',
        'https://www.usa.gov/',
        'https://www.nasa.gov/'
        ]
    objs = [fetch_page_title(url) for url in urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(objs))
    loop.close()

if __name__ == "__main__":
    main()