"""
physical newline
logical newline

implicit: list tuple dictionary set function arguments
explicit: \(backslash)
if a \
    and b \ :

\n, \t

multiline are not comments. but are docstrings.


"""

# implicit line continuation:
a = [1,2,3]
b = [1,2,
     3,4,5]
c = [1, #item,
    2]

d = (1
     ,2 #commet
     ,3)

e = {1:'a' #items
     ,2:'b' #items
    }

def my_func(a, #comment
            b,
            c):
    print(a,b,c)

my_func(10,
        20,30 #comment
        )

# explicit line continuation:

f =10
g= 20
h=30
if f>5 \
    and g>10 \
        and h>20:
    print(True)

i = '''this\nis string'''
print(i, type(i))

j = '''this is 
second
string'''
print(j)

k = '''some items:
        1. i1
        2. i2'''
print(k)

def new_func():
    l = '''multi line string
and this indents properly'''
    return l
print(new_func())