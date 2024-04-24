def factorial(number):
    fact=1
    while number>0:
        fact*=number
        number-=1
    return fact

num=int(input("Enter a number: "))
print("Factorial:",factorial(num))