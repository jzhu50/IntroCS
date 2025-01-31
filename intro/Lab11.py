#Michelle Zhu
#IntroCS pd3 sec4
#Lab11 -- Euler's project
#2023-04-17
#time cost: 2
#consulted: chatgpt, Andrew Choi

import math

'''Find the sum of all the multiples of 3 or 5 below 1000.'''

def sum_multiples():
    sum = 0
    for i in range (1, 1000):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

print(sum_multiples())

'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum'''

def sum_square_diff():
    sum=0
    sum2=0
    for i in range(1, 101):
        sum += i**2
        sum2 += i
    print(sum2**2 - sum)
    
sum_square_diff()

def sm20():
    n=2520
    while True: #basically forever loop
        for i in range(3,20):
            if n%i != 0:
                break
            if i == 19:
                return n
        n += 20

print(sm20())

'''Find the largest palindrome made from the product of two 3-digit numbers.'''

def p():
    largest_num=0
    for i in range(1,1000):
        for n in range (1,1000):
            product=i*n
            str_p=str(product)
            if str_p[0:3]==str_p[5:2:-1] and product > largest_num:
                largest_num = product
    return largest_num
                
print(p())

'''
!!! the for loop doesn't repeat itself

my_string[6:1:-1] # starts at index 6, ends at index 2 (not inclusive), with a step of -1
'''

'''another way:'''

def s3():
    n = 998001
    while True:
        for i in range(2,1000):
            if n%i==0 and n/i<1000 and str(n)[0:3]==str(n)[5:2:-1]:
                return n
        n -= 1

print(s3())

'''What is the largest prime factor of the number 600851475143?'''

def lpf():
    n=600851475143
    largest_factor=1
    for i in range(2, int(math.sqrt(n)+1)):
        while n%i==0:
            largest_factor=i
            n = n//i
    return largest_factor
    
print(lpf())

"By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."

def f():
    x=1
    y=2
    sum=2
    while y<4000000:
        x, y = x, x+y
        if y%2==0:
            sum+=y
    return sum

print(f())           
