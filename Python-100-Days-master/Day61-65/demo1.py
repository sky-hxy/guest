'''
Author: hxy 1305149167@qq.com
Date: 2023-05-08 00:34:57
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-05-08 23:11:25
FilePath: /Python-100-Days-master/Day61-65/demo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import asyncio
import time

async def display(num):
    await asyncio.sleep(1)
    print(num)

def main():
    start = time.time()
    objs = [display(i) for i in range(1, 10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(objs))
    end = time.time()
    print(f'{end - start:.3f}秒')

if __name__ == '__main__':
    main()