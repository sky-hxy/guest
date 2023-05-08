'''
Author: hxy 1305149167@qq.com
Date: 2023-04-27 00:10:16
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-04-27 00:35:04
FilePath: /Python-100-Days-master/Day01-15/code/Day13/deno.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s。。。' % filename)
    time_to_load = randint(2, 10)
    sleep(time_to_load)
    print('下载%s文件耗时%d秒' % (filename, time_to_load))

def main():
    start = time()
    download_task('Python学习手册.txt')
    download_task('泰坦尼克号.mp4')
    end = time()
    print('下载文件总共耗时%.2f秒' % (end - start))

if  __name__ == '__main__':
    main()