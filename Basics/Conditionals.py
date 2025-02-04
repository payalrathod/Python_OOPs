a = 2

if a<5:
    print('a<5')
else:
    print('a>=5')

b =10
if b<5:
    print('b<5')
else:
    if b<10:
        print('5<a<10')
    else:
        print('a>=10')

if a<5:
    print('a<5')
elif a<10:
    print('5<=a<10')

c =25
c = '25' if c < 30 else False
print(c)

print(True) if a<0 else print(False)

# print(a)