'''
Author: hxy 1305149167@qq.com
Date: 2023-03-15 00:19:55
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-03-25 00:40:39
FilePath: /webSocketDemo/base/output.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import get_fruits
import process
try:
    print("you got %s" % process.total + " fruits!")
except Exception as e:
    raise print("\33[41m[error]]\33[0mInput should be numbers]")
