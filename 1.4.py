def reverse(num):
    if len(num)==1:
        return num
    else:
        return num[len(num)-1] + reverse(num[:len(num)-1])

n=input('Enter a number: ')
if n==reverse(n):
    print(n, 'is Palindrome')
else:
    print(n, 'is not a Palindrome')
