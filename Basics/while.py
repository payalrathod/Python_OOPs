i = 0
while i<5:
    print(i)
    i = i+1
print(" ")
i = 5
while True:
    print(i)
    if i>=5:
        break
        print("abc")

minlength = 2
# name=input("enter your name: ")
# while not (len(name) >= minlength and name.isprintable() and name.isalpha()):
#     name=input("enter name: ")
#
# print("Hello, {0}".format(name))


# while True:
#     name = input("enter name: ")
#     if (len(name) >= minlength and name.isprintable() and name.isalpha()):
#         break
# print("Hello, {0}".format(name))

print(" ")

a = 0
while a<10:
    a= a+1
    if a%2 == 0:
        continue
    print(a)


l = [1,2,3]
val = 10
found =False
idc = 0
while idc < len(l):
    if l[idc] == val:
        found = True
        break
    idc = idc + 1
print(l)
if not found:
    l.append(val)
print(l)

l = [1,2,3,4]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx = idx + 1
else:
    l.append(val)
print(l)

