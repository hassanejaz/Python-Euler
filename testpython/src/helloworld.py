# Euler problem 1 in Python

import platform

version=platform.python_version()
print('This is python version{}'.format(version)) 


num = 0
summ = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        summ += num
                
print(summ)
    
n=0
sum=0

while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        sum = sum + n
    n = n + 1

print(sum)

