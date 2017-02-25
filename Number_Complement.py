# -*-coding=utf-8-*-
__author__ = 'Rocky'
def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    result=[]
    while num!=0:
        remainder=num%2
        num=num/2
        result.append(remainder)
    l=len(result)

    for i in range(l/2):
        temp=result[i]
        result[i]=result[l-i-1]
        result[l-i-1]=temp
    lam=lambda x:abs(x-1)

    for i in range(l):
        result[i]=lam(result[i])

    #print result
    sum=0
    for i in range(l):
        sum=sum+result[l-i-1]*pow(2,i)
    return sum

i=8
i=i<<1
print i-1
for i in range(1,20):
    pass
    #print findComplement(i)