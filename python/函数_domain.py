#!/usr/bin/env python
#coding=utf-8

#定义函数
def name(params):
    pass
def fn(x):
    print(x)
#函数调用
fn('x')


#函数参数
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
#当函数有多个参数的时候，参数之间使用逗号分隔
add(1, 2)


#调用的时候，按顺序传入相同个数的参数, 所以，参数的顺序非常重要
def append(lst, x):
    lst.append(x)
lst = [1, 2, 3]
print(type(lst))
append(lst, 4)
print(lst)


#Python中，参数总是引用传递
def swap(x, y):
    x, y = y, x
    print(x, y)
x = 3
y = 4
print(x)
print(y)
swap(x, y)

#作用域
#函数式Python的最小作用域
#返回值

def fn():
    pass
fn()
def add(x, y):
    return x+y
print(add(1, 2))
print(a)
a = fn()
print(a)
