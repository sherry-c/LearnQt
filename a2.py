"""
Too broad exception clause
这是Exception没有指定错误类型，因为捕获的异常过
于宽泛，没有针对性，自己可以通过指定精确的异常类型来解决，如果不知道确切错误，可以
关闭编译器中代码检测中有关检测
"""
import os
import sys

import traceback

# noinspection PyBroadException
try:
    print('1')
    a = 100 / 0
except Exception as e:
    # except ZeroDivisionError as e:
    traceback.print_exc()
    print(e)

finally:
    print(os.path)
    print(sys.argv)
