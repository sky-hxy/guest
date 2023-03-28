'''
Author: hxy 1305149167@qq.com
Date: 2022-07-31 06:48:29
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-03-24 01:02:27
FilePath: /webSocketDemo/Demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random as rd

x = rd.randint(0, 10)
print(x)
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
f = open("example.txt", "r")
s = f.readline()
print(s)
f.close()