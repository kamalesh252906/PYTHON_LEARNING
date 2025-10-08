a = 5
b = 2
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)

x = int(input('Enter a number:'))
if x%2 == 0:
    print("even=", x)
else :
    print("odd=", x)


x = int(input('Enter the year:'))
if x%4 == 0:
    print(x ,"is a leap year")
else :
    print(x ,"is not a leap year")

x = int(input('Enter a number:'))
if x%3 == 0 or x%5 == 0:
    print(x ,'is divisible')
else :
    print(x ,'is not divisible')

x = int(input('Enter a number:'))
if 2001 <= x <= 2100:
    print(x , 'is a century')
else :
    print(x ,'is not a century')