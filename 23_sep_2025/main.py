# n = int(input('Enter a number:'))
# a = 1
# while a <= n :
#     print(a*a*a)
#     a = a + 1



# n = int(input('Enter a number:'))
# a = int(input('Enter how many times:'))
# while a <= n :
#     print(a)
#     a = a + 1


# n = int(input('Enter a number:'))
# i = 1
# if n <= 0 :
#     print('Invalid Input')
# while i <= n :
#     print(i*i)
#     i += 1


n = int(input('Enter a number:'))
a = 0
b = 1
i = 1
while i <= n :
    print(a)
    a,b = b , a + b
    i += 1