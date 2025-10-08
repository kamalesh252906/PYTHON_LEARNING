# 1st problem
n = int(input('Enter a number:'))
m = int(input('Enter a number:'))
y = n + m 
if y % 2 == 0 :
    print('Even')
else :
    print('odd')

# 2nd problem 

a = int(input('Enter a two digit number:'))
b = a // 10 
c = a % 10
m = b + c
j = b * c
if m + j == a :
    print('Great')
else :
    print('Not Great')

# 3rd problem 

a = input('Enter residential or commercial:')
b = int(input('Enter a number of units:'))
if a == 'residential' :
    if b >= 0  and b <= 100 :
        print( b * 3 , 'rupees')
    elif b >= 101 and b <= 200 :
        print(b * 5, 'rupees')
    else:
        print(b * 7, 'rupees')
else :
    if a == 'commercial' :
        if b >= 0 and b <= 100 :
            print(b * 5, 'rupees')
        elif b >=101 and b<=200 :
            print(b * 7, 'rupees')
        else :
            print(b * 10, 'rupees')
    else:
        print('Invalid input')

# 4th problem 


a = int(input('Enter a distance:'))
b = 50
if a >= 0 and a <= 5 :
    print(b, 'rupees')
elif a >= 6 and a <= 15 :
    print(a * 8, 'rupees')
elif a > 15 :
    print(a * 6, 'rupees')
else :
    print('Invalid input')

# 5th problem 


a = int(input('Enter a value a:'))
b = int(input('Enter a value b:'))
c = int(input('Enter a value c:'))
if a == b == c :
    print('equal')
elif a == b != c or a == c != b or c == b != a:
    print('isosceles')
elif a != b != c :
    print('scalene')
else :
    print('Invalid input')

# 6th problem 

a = int(input('Enter a number:'))
if a % 3 == 0 and a % 5 == 0 :
    print('FizzBuzz')
elif a % 5 == 0 :
    print('Buzz')
elif a % 3 == 0:
    print('Fizz')
else :
    print(a)

# 7th problem 

a = input('Enter a group (Science / Commerce / Arts):')
match a :
    case 'Science' :
        b = input('Enter a sub-choice (Medical / Engineering):')
        match b :
            case 'Medical' :
                print('You Chose Science - Medical')
            case 'Engineering' :
                print('You Chose Science - Engineering')
            case _ :
                print('You Chose Invalid')
    case 'Commerce' :
        b = input('Enter a sub-choice (CA / B.com):')
        match b :
            case 'CA' :
                print('You Chose Commerce - CA')
            case 'B.com' :
                print('You Chose Commerce - B.com')
            case _ :
                print('You Chose Invalid')
    case 'Arts' :
        b = input('Enter a sub-choice (Literature / History):')
        match b :
            case 'Literature' :
                print('You Chose Arts - Literature')
            case 'History' :
                print('You Chose Arts - History')
            case _ :
                print('You Chose invalid')
    case _ :
        print('Invalid Input')


# 8th problem 

a = int(input('Enter the show time in 24 hours format:'))
if a >= 9 and a <= 12 :
    print(a,': AM   Morning Show')
elif a > 12 and a <= 16 :
    print(a,': PM  Matinee Show')
elif a > 16 and a <= 20 :
    print(a,': PM  Evening Show')
elif a > 20 :
    print(a,': PM  Night Show')
else :
    print('Invalid Show Time')

# 9th problem 

a = int(input('Enter a kilometer:'))
b = int(input('Enter a conversion Choice meters(1) / millimeters(2) / centimeters(3) / miles(4) : '))
match b :
    case 1 :
        print(a * 1000 )
    case 2 :
        print(a * 1000000)
    case 3 :
         print(a * 100000)
    case 4 :
        print(a * 0.621371)
    case _ :
        print('Invalid Conversion')


# 10th problem 

a = input('Enter a payment mode:')
match a :
    case 'UPI' :
        print("You selected UPI payment")
    case 'Card' :
        print("You selected Debit/Credit Card payment")
    case 'COD' :
        print( "You selected Cash on Delivery")
    case 'Net banking' :
        print("You selected Net Banking")
    case _ :
        print('Invalid payment mode')



