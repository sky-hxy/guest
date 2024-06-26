'''
Author: hxy 1305149167@qq.com
Date: 2023-03-15 00:50:23
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-03-15 00:57:40
FilePath: /webSocketDemo/base/process.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import get_fruits
a = get_fruits.a
b = get_fruits.b
try:
    total = int(a) + int(b)
except Exception as e:
    raise print("\33[41m[error]]\33[0mInput should be numbers]")
