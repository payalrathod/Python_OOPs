i = 0
while i<5:
    print(i)
    i = i+1

print(" ")

for i in range(5):
    print(i)

for i in [1,2,3,4]:
    print(i)

for c in 'hello':
    print(c)

for x in ('a','b',4):
    print(x)

for i,j in [(1,2),(3,4),(5,6)]:
    print(i,j)

for i in range(5):
    if i == 3:
        continue #break
    print(i)
print("")
for i in range(1,14):
    # print(i)
    if i%7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiple of 7 in range')

for i in range(5):
    print('----------------')
    try:
        10/(i-3)
    except ZeroDivisionError:
        print('divided by zero')
        continue
    finally:
        print('always executed')
    print(i)

s = 'hello'
for c in s:
    print(c)
i = 0
for c in s:
    print(i,c)
    i = i+1

for i in range(len(s)):
    print(i, s[i])

print(" ")

for i,c in enumerate(s):
    print(i,c)
