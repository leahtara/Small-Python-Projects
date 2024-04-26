def is_armstrong(num):
    digits=len(str(num))
    sum=0
    temp_num=num
    for i in range(digits):
        sum+=((temp_num%10)**digits)
        temp_num//=10
    if sum==num:
        return 'Armstrong'
    else:
        return 'not armstrong'

number=int(input('Enter a number: '))
print(number, 'is', is_armstrong(number))
