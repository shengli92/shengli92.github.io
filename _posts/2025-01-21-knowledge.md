---
layout: post
tags: [python]
---
{% include JB/setup %}


### Knowledge List

python 迭代器与可迭代对象:

可迭代对象: 包含 __iter__ 方法，能够被遍历的都可以称之为可迭代对象。 例如python的容器类数据类型：List, Tuple, Set, Dict。使用 `iter()` 函数可以将可迭代对象转换成迭代器。
迭代器: 包含 __next__ 魔法方法的对象。 对于可迭代对象，可以通过 `next()` 方法调用，每次调用，都会返回可迭代对象的下一个元素。直到没有元素返回时抛出StopIteration异常。
生成器: 可以看成是一个特殊的迭代器。使用 yield 方法代替 return。 每次调用，都会记录函数状态并返回当前值。下次调用，会继续从纪录的地方继续执行。


装饰器: 包含wrapper方法。旨在不改变函数原有代码的前提下，修改函数/给函数添加功能。 实现原理是因为 将原函数当成参数传入装饰器函数。 涉及到一个概念： Python中，函数是一等公民.
上下文管理器:  可以理解成包含__enter__, __exit__魔法方法的对象。 通过with调用，在读取文件，数据库连接，锁的获取和释放中经常使用。作用是确保资源的正确使用和释放。例如：
```
    with open('example.json', 'r'):
        content = file.read()
        print(content)
```
open('example.json', 'r') 会创建一个文件对象，它就是一个上下文管理器。进入with语句时，文件被打开。当with语句结束时，文件会自动关闭。就算读取文件过程中发生异常，文件也会被正常关闭。
下面是数据库上下文管理器示例：
```
import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None


    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection


    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()


# 使用数据库连接上下文管理器
with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print(rows)
```

contextlib 提供了一些创建上下文管理器的工具，使代码更简洁。使用 contextmanager 装饰器可以将一个生成器函数转换为上下文管理器：
```
from contextlib import contextmanager

@contextmanager
def simple_context_manager():
    print("进入上下文")
    try: 
        yield "在上下文中的对象"
    finally:
        print("退出上下文")
```

