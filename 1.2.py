def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return 'Composite'
    return 'Prime'

number=int(input('Enter a number: '))
print(number, 'is', is_prime(number))
