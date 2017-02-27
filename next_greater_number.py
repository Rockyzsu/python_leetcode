# -*-coding=utf-8-*-
__author__ = 'Rocky'
def next_greater_number(findNums,nums):
        l=len(nums)
        result=[]
        for i in findNums:
            findIt=False
            for j in range(l):
                if i==nums[j]:
                    for k in range(j,l):
                        if i<nums[k]:
                            result.append(nums[k])
                            findIt=True
                            break
                if findIt:
                    break

            if findIt ==False:
                result.append(-1)
        return result

a=[2,4,5]
b=[1,2,3,4,5]
print next_greater_number(a,b)
