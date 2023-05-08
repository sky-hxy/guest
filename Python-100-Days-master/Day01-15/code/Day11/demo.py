'''
Author: hxy 1305149167@qq.com
Date: 2023-04-25 02:04:26
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-04-25 02:19:29
FilePath: /Python-100-Days-master/Day01-15/code/Day11/demo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import requests
import json

def main():
    myDict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('Day01-15/code/Day11/data.json', 'w', encoding='utf-8') as fs:
            json.dump(myDict, fs)

        with open('Day01-15/code/Day11/致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except IOError as e:
        print(e)
    print('保存数据完成')

    

if __name__ == '__main__':
    main()
