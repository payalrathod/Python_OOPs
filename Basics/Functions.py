from math import sqrt
import math

s = [1,2,3]

print(sqrt(16))
print(math.exp(1))

def func_1():
    print("running func_1")

func_1()

def func_2(a: int,b: int):
    return a*b

print(func_2('a',4))
print(func_2([1,2],4))

def func_3():
    return func_4()
def func_4():
    return 'running func 4'

fn1 = lambda x: x**2
print(fn1(2))


