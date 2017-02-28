#-*-coding=utf-8-*-
x=1
y=4
z=x^y
#solution 1
s=bin(z)
distance=0
for i in s[2:]:
    if i=='1':
        distance+=1
print distance

#solution 2
x='abcdfeffg'
print x.count('f')
#自己实现bin函数

def my_bin(x):
    result=[]
    while 1:
        t=x%2
        result.append(t)
        x=x/2
        if x/2==1:
            result.append(1)
            break
    return result

a=my_bin(64)
print a[:]