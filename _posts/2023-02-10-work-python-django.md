---
layout: post
tags: [work, python]
---

## Django
### django中间件
django 的中间件作用在 request 和 response 之间。 一个自定义的中间件必须继承 MiddlewareMixin (`from django.utils.deprecation import MiddlewareMixin`) 类，且自定义的中间件中可以定义五个方法，用来定义该中间件的行为，分别为

- process_request(self, request)
- process_view(self, request, callback, callback_args, callback_kwargs)
- process_template_response(self, request, response)
- process_exception(self, request, response)
- process_response(self, request, response)


中间价的注册是在settings.py文件中的MIDDLEWARE变量中，执行顺序是顺序执行， 即 process_request是自上而下，process_response是自下而上。

#### process_view
参数是 request， 跟视图函数接收到的request相同。 在视图函数之前执行。可以返回None，或者 HttpResponse。

    - 如果返回 None值，则继续执行，交给下一个中间件。
    - 如果返回 HttpResponse, Django 将不执行后续视图函数之前执行的方法以及视图函数，直接以该中间件为起点，倒序执行中间件，且执行的是视图函数之后执行的方法。

#### process_template_response
在视图函数之后执行，需要注意的是，要执行该方法，在视图函数中，需要返回一个 render 对象。 
```python
### view.py 视图函数
from django.http import HttpResponse


def index(request):
    print("index")
    rep = HttpResponse("")
 
    def render():
        print("render")
        return HttpResponse("")
 
    rep.render = render
    return rep

### 最终只打印 render
```


#### process_exception
用来捕捉视图函数的错误， 方法只有在视图函数中出现异常了才执行，按照 settings 的注册倒序执行


## Python

### python bitwise operator (位操作符)

#### ^ (6上面的数字)
按位异或， 对应位置上相同则为0，否则为1
```python
a = 6 ^ 2
print(a) # 4
# 6: 0110
# 2: 0010
# 按位异或的结果就是： 0100 即为4
```


#### 其余操作符


| 位运算符         |    说明 |  示例 |
|--------------|:--:|----:|
| &            | 按位与     | 4&5 |
| |            | 按位或     | 4|5 |
| ^            | 按位异或   |  6^2 |
| ~            | 按位取反   | ~6   |
| <<           | 按位左移   | 4 << 2 | 
| >>           | 按位右移   | 4 >> 2 | 

