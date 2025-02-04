a =10
b =0

try:
    a/b
except ZeroDivisionError:
    print("divide by zero")
finally:
    print("this always executes")

a = 0
b = 10
while a<4:
    print("------------------")
    a = a+1
    b = b-1
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - div by zero".format(a,b))
        continue #break
    finally:
        print("{0}, {1} - always executes".format(a,b))

    print("{0}, {1} - main loop".format(a,b))
else:
    print('code executed without zero division')

