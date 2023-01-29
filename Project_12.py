a = int(input('Enter Your Number: '))
b = 0
while a:
    a , remainder = divmod(a , 10)
    b += remainder
    

print(f'Sum of your number: {b}')

