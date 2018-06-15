---
layout: post
title: "Static, Abstract and Final"
description: ""
category: 
tags: []
---
{% include JB/setup %}

### static
static 关键子用来定义静态方法和属性。 psr-2 规定： static 应该位于访问控制（publi, protected and private）
后面。 
<font color="#0099ff">声明类属性或方法为静态，就可以不实例化类而直接访问。静态属性不能通过一个类已实例化的对象访问（但静态方法可以）。</font>
由于静态方法不需要通过对象即可调用，所以伪变量 $this 在静态方法中不可用。

静态属性直接通过类名加上范围操作符即可调用， simple example like this: 
```
 <?php 
 class Foo
 {
     public static $my_static = 'foo';
 }
 
 print Foo::$my_static;
 $classname = 'Foo';
 print $classname::$my_static;  //As of PHP 5.3.0
```
静态方法实例：
``` 
<?php
class Foo
{
    public static function aStaticMethod()
    {
        // ....
    }
}

Foo::aStaticMethod();
$classname = 'Foo';
$classname::aStaticMethod(); // As of 5.3.0
```

#### 静态变量
变量范围的另一个重要特性就是 静态变量(static variable)。 静态变量仅在局部函数域中存在，但当程序执行离开此作用域时，其值并不丢失。
例子如下：
``` 
// 需要静态变量但是没有使用的例子
 <?php
 function test()
 {
     $a = 0；
     echo $a;
     $a++；
 }
 
 //上述函数没有什么用处，因为每次调用时都将$a的值设为0并输出0.将变量加一的$a++没有作用，因为一旦退出本函数，则变量$a就不存在了。要写一个不会丢失本次计数值的计数函数，要将变量 $a 定义为静态的：
 
 <?php
 function testStatic()
 {
     static $a = 0;
     echo $a;
     $a++;
 }
 
 //现在 变量$a 仅在第一次调用testStatic函数时被初始化，之后每次调用test函数都会输出 $a 的值并加一。
```

静态变量也提供了一种处理递归函数的方法，递归函数是一种调用自己的函数，写递归函数要小心，因为可能会无穷递归下去。必须确保有充分的方法来终止递归，以下这个简单的递归函数计数到10，使用静态变量 $count 来判断何止停止：
``` 
<?php
 function test()
 {
     static $count = 0;
     
     $count++;
     echo $count;
     if($count < 10) {
         test();
     }
     $count--;
 }
```

#### 后期静态绑定
自 PHP5.3.0起，PHP增加了一个叫做后期静态绑定的功能，用于在继承范围内引起静态调用的类。
准确说，后期静态绑定工作原理是存储了在上一个 "非转发周期" （non-forwarding call）的类名。当进行静态方法调用时，该类名即为明确指定的那个（通常在:: 操作符左侧部分）；当进行非静态方法调用时，即为该对象所属的类。所谓的"转发调用"指的是通过以下几种方式进行静态调用：
self::, parent::, static:: 以及forward_static_call。 可用get_called_class() 函数来得到被调用的方法坐在的类名，static:: 则指出了其范围。


未完