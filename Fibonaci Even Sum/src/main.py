num1 = 0
num2 = 1
summ = 0
even = 0
i = 0

#for i in range(4000000):
while i <= 4000000: 
       
               
    if (summ % 2 == 0):
        even = even + summ
    
    summ = num1 + num2
    num1 = num2
    num2 = summ    
    i = summ
            
print('Even: {}'.format(even))
        
a=0
b=1
p=0
while  a < 4000000:
    c= a+b
    if c % 2 ==0 :
        p=p+c
    a = b
    b = c
print (p)        
        
        
    