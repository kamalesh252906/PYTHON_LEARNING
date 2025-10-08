a = int(input('enter a number:'))
b = int(input('enter a number:'))
if a > 0 and b > 0 :
    print('1st q')
elif a < 0 and b > 0 :
    print('2nd q')
elif a < 0 and b < 0 :
    print('3rd q')
elif a > 0 and b < 0 :
    print('4th q')
else :
    print('Center point')

a = int(input('Enter your rating :\n'))
match a :
    case 1 :
        print('Very bad')
    case 2 :
        print('Bad')
    case 3 :
        print('Average')
    case 4 :
        print('Good')
    case 5 :
        print('Excellent')
    case _ :
        print('Invalid Rating')

def square_of_number (n) :
    if n % 4 == 0 :
        print('Even')
    else :
        print('odd')
square_of_number (8)

def number (a) :
    if a > 0 :
        print('The number is positive')
    elif a == 0 :
        print('The number is zero')
    else :
        print('The number is negative')
number (-8)

a = input('Enter a character')

a = int(input('enter amount:'))
b = int(input('enter member or not if member enter 1 if non member enter 0:'))
if b == 1:
    print( a / 10 , 'is a reward point')
elif b == 0 :
    print('no reward points')
else :
    print('invalid')

