#num=[2,3,5,9,12,33,4,22,90,17]
num=[2,3,5,9,12,33,4,22,90,17,1]
target=91
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if target== num[i]+num[j]:
            print "[%d,%d]" %(i,j)