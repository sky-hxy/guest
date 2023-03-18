'''
Author: hxy 1305149167@qq.com
Date: 2023-03-15 00:20:14
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-03-17 00:45:09
FilePath: /webSocketDemo/base/get_fruits.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

a = input("how many apples do you got?\n")
try:
    a = int(a)
except Exception as e:
    raise print("请输入数字")
print("you got %s" % a + " apples")
b = input(("how many bread do you got?\n"))

try:
    b = int(b)
except Exception as e:
    raise print("请输入数字")
print("you got %s" % b + " bread")
