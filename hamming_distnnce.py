x=10
y=20
z=x^y
#solution 1
s=bin(z)
print type(s)
distance=0
for i in s[2:]:
    if i=='1':
        distance+=1
print "distance is %d" %distance

#solution 2
