# -*-coding=utf-8-*-
__author__ = 'Rocky'

def fizzBuzz_wrong(n):
    result=[]
    for i in range(1,n+1):
        s=str(i)
        if '3' not in s and '5' not in s:
            result.append(s)
            continue
        if '3'  in s and '5' not in s:
            result.append('Fizz')
            continue
        if '3' not in s and '5' in s:
            result.append('Buzz')
            continue
        if '3'  in s and '5' in s:
            result.append('FizzBuzz')
            continue

    return result
print fizzBuzz_wrong(15)

def fizzBuzz(n):
    result=[]
    for i in range(1,n+1):
        remainder1=i%3
        remainder2=i%5
        if remainder1 != 0 and remainder2!=0:
            result.append(str(i))
        elif remainder1==0 and remainder2!=0:
            result.append('Fizz')
        elif remainder1!=0 and remainder2 == 0:
            result.append("Buzz")
        else:
            result.append("FizzBuzz")

    return result

print fizzBuzz(45)