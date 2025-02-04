# fibonacci series

c = 10
a = 0
b = 1
j=0
for i in range(c):
    print(a) # 0        1
    j = a+b  # j=1      j=2
    a=b     #a=1
    b=j     #b=1

# sum of two large numbers

str1 = "87678321233"
str2 = "1232343443"

result = int(str1)+int(str2)
print(result)

a = [1, 4, 2, 5, 0]
sumleft = 0
sumright = 0
for i in range(1,len(a)):
    sumleft = sum(a[0:i])
    sumright=sum(a[i+1:])

    if sumleft == sumright:
        print(a[i], sumleft, sumright)

# count repeated words in a list

lst = ['a', 'b', 'a', 'b', 'c', 'a', 'a', 'e']
dic={}
count=0
for i in lst:
    if i not in dic:
        dic[i]= 1
    else:
        dic[i] += 1
print(dic)

dct={}
for i in lst:
    dct[i] = lst.count(i)
print(dct)


# array rotation
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2

c = arr[l:]+arr[:l]
print(c)

arr = [12, 3, 4, 15]
su=0
for i in arr:
    su = i+su
print(su)

# Find largest element in an array
arr = [12, 3, 4, 15]
print(max(arr))
c=0
for i in range(1, len(arr)):
    if arr[i]>c:
        c=arr[i]
print(c,"c")

lar_ele = max(arr, key=lambda x: x)
print(lar_ele)

# Program for Array Rotation
j=[1, 2, 3, 4, 5, 6, 7, 8]
c = j[::-1]
print(c)

rotateBy = 2
tmep = []
i=0
while i<rotateBy:
    tmep.append(j[i])
    i=i+1
print(tmep)
i=0
while rotateBy<len(j):
    j[i] = j[rotateBy]
    i=i+1
    rotateBy=rotateBy+1
j[:] = j[:i]+tmep
print(j)





# a = [int(a) for a in input("Enter 3 digits: ").split(",")]
# # print(a)
# b=[]
# for i in range(len(a)):
#     for j in range(i):
#         for k in range(k):
#             if k != i and k != j and i!=j:
#                 b.append((a[i],a[j],a[k]))
# print(b)
