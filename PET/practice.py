a = int(input('Enter a number:'))
if a % 2 == 0 :
    print('even')
else :
    print('odd')

>=90 → "Grade A"

>=75 → "Grade B"

>=50 → "Grade C"

else → "Fail"

a = int(input('Enter your marks:'))
if a >= 90 :
    print('A')
elif a >= 75 :
    print('B')
elif a >= 50 :
    print('C')
elif a < 50 :
    print('Fail')
else :
    print('Invalid marks')

a = int(input('Enter a number:'))
match a :
    case 1 :
        print('Monday')
    case 2 :
        print('Tuesday')
    case 3 :
        print('Wednesday')
    case 4 :
        print('Thursday')
    case 5 :
        print('Friday')
    case 6 :
        print('Saturday')
    case 7 :
        print('Sunday')
    case _ :
        print('Invalid Number')


n = int(input('Enter a number:'))
sum = 0
a = 1
while a <= n :
    sum += a
    a += 1
print(sum)


n = int(input('Enter a number:'))
a = 1
b = 10
for i in range(a,b+1):
    print(n,'x',i,'=',n*i)
    

a = (input('Enter a number:'))
if a == a[::-1]:
    print('Palindrome')
else :
    print('Not palindrome')


n = input('Enter your operator:')
a = int(input('Enter first number:'))
b = int(input('Enter your second number:'))
if n == '+' :
    print(a + b)
elif n == '/' :
    print(a / b)
elif n == '*' :
    print(a * b)
elif n == '-' :
    print(a - b)
else :
    print('Invalid operator')


n = int(input('Enter a number:'))
match n :
    case 1 :
        print('Jan')
    case 2 :
        print('Feb')
    case 3 :
        print('Mar')
    case 4 :
        print('Apr')
    case 5 :
        print('May')
    case 6 :
        print('Jun')
    case 7 :
        print('Jul')
    case 8 :
        print('Aug')
    case 9 :
        print('Sep')
    case 10 :
        print('Oct')
    case 11 :
        print('Nov')
    case 12 :
        print('Dec')
    case _ :
        print('Invalid input')



n = int(input('Enter a number:'))
rev = 0
while  n > 0 :
    rev = rev*10 + n % 10
    n = n // 10
print(rev)


Prime number check using for loop

n = int(input('Enter a number:'))
if n > 1 :
    for i in range(2,n):
        if n % i == 0 :
            print('Not a prime numbner')
            break
    else :
        print('Prime number')
else :
    print('Not a prime number')

n = int(input('Enter a number:'))
a = int(input('Enter a number:'))
for num in range(n,a,+1):
    if num > 1 :
        for i in range(2,num):
            if num % i == 0 :
                break
        else :
            print(num,end = '  ')


a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
while a <= b :
    print(a)
    a += 1


n = int(input('Enter a number:'))
a = 0
while n > a :
    print(n)
    n -= 1


n = int(input('Enter a number:'))
a = 1
while a <= n :
    print(a**2)
    a += 1

a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))
if a > b and a > c :
    print(a)
elif b > a and b > c :
    print(b)
else :
    print(c)


a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))
if a > b and b < c :
    print('yes')
else :
    print('no')

n = int(input('Enter a number:'))
if n % 2 == 0 :
    print('even')
else :
    print('odd')

n = int(input('Enter a number:'))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 :
    print('Leap year')
else :
    print('Not leap year')


n = int(input('Enter a number:'))
if n % 3 == 0 and n % 5 == 0 :
    print('divisible')
else :
    print('not divisible')

n = int(input('Enter a number:'))
if n >= 2001 and n <= 2100 :
    print('21st century')
else :
    print('Not in 21st century')


n = int(input('Enter a number:'))
if n > 0 and n < 13 :
    print('child')
elif n >= 13 and n < 20 :
    print('teen')
elif n >= 20 and n <= 59 :
    print('adult')
elif n > 59 and n <= 100 :
    print('senior')
else :
    print('Invalid') 



n = int(input('Enter a number:'))
a = 0
b = 10
while a <= b :
    print(a*n)
    a += 1


n = 5
a = 0
b = 100
while a <= b :
    if a % n == 0:
        print(a)
    a += 5

n = int(input('Enter a number:'))
sum = 0
for i in range(0,n+1):
    if i % 2 == 0 :
        sum += i
        i += 1
print(sum)


n = int(input('Enter a number:'))  
a = 1
while a <= n :
    print(a**2)
    a +=1


a = 1
b = 10
while a <= b :
    print(a**2)
    a +=1


a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))
print(a,b,c,end = '')

a = int(input('Enter a amount:'))
if a > 500 :
    print(a,'delivery free')
elif a <= 500 and a > 0 :
    print(a+50,'delivery charged')
else :
    print('Invalid amount')


a = int(input('Enter a amount:'))
if a % 7 == 0 :
    print('yes')
else :
    print('no')



a = input('Enter rainy or sunny:')
if a == 'rainy' :
    print('Bring umbrella')
else :
    print('No needed')


a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))
if a >= 40 and b >= 40 and c >= 40 :
    print('promoted')
else :
    print('not promoted')


n = int(input('Enter a number:'))
a = n
rev = 0
while n > 0 :
    rev = rev * 10 + n % 10
    n //= 10
if a == rev :
    print('Palindrome')
else :
    print('Not palindrome')

n = int(input('Enter a number:'))
m = int(input('Enter a number:'))
for j in range(n,m+1) :
    if j > 1 :
        for i in range(2,j) :
            if j % i == 0 :
                break
        else :
            print(j)

n = int(input('Enter a year:'))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 :
    print('Leap year')
elif n == 0 or n < 0:
    print('Invalid year')
else :
    print('Not a leap year')


n = int(input('Enter a number:'))
sum = 0
a = 1
while a <= n :
    if a % 2 == 0 :
        sum = sum + a
    a = a + 1
print(sum)

n = int(input('Enter a number:'))
a = 0
sum = 0
for i in range(a,n+1,+1):
    sum = sum + i
print(sum)


n = int(input('Enter a number:'))
a = 1
fact = 1
for i in range(a,n+1,+1):
    fact = fact * i
print(fact)


