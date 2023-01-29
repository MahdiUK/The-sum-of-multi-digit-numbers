# Solution 1
a = int(input('Enter Your Number: '))
b = 0
while a:
    a , remainder = divmod(a , 10)
    b += remainder

print('Sum of your number:' , b)

# Solution 2
number = int(input('Enter Your Number: '))
SUM = 0
for items in str(number):
    SUM += int(items)
    
print('Sum of your number:', SUM)
