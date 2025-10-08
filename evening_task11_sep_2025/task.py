# Barath sir tasks:



# Tara and Jyoti were given one number each. She has to find whether the sum of the two numbers is divisible by 5 or not . If yes then print 1 else print 0

Tara = int(input('Enter a number:'))
jyoti = int(input('Enter a number:'))
both = Tara + jyoti
if both%5 == 0 :
    print(1)
else :
    print(0)

# # Given a number N, print yes if the number is a multiple of 7 else print no.

x = int(input('Enter a number:'))
if x%7 ==0 :
    print(x, 'is divisible by 7')
else :
    print(x, 'is not divisible by 7')

# A food delivery app gives free delivery if the order amount is above ₹500. If the order is less than or equal to ₹500, a delivery charge of ₹50 is added. Write a program that takes the order amount from the user. Print whether delivery is free or charged and prints the total amount as well.

x = int(input('Enter the amount you ordered:'))
if x > 500 :
    print('delivery charges free')
else :
    print(x + 50, 'delivery charged')


# sathiya sir tasks:


# Find the Grades from the user input for the marks.
# Let "X" be marks obtained through input.
# Write a program to check if the mark falls in the below mentioned range.
# A -> 100 to 80
# B -> 60 to 79
# C -> 50 to 59
# D -> 40 to 49
# lesser than 40 - Fail
# Sample Input:
# 77
# Sample output:
# B (edited) 


x = int(input('Enter the marks :'))
if x >= 80:
    print(x, 'is a A grade')
elif x >= 60:
    print(x,'is a B grade')
elif x >= 50:
    print(x, 'is a C grade')
elif x >= 40:
    print(x, 'is a D grade')
else:
    print(x, 'is a Fail')

# Given 3 sides, check if they can form a triangle (sum of two sides > third).
# Sample Input:
# 3
# 4
# 5
# Sample Output:
# YES
# Ref:
# 3 + 4 = 7 which is greater than the third side 5


a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))
add = a + b
if add > c :
    print('yes')
else :
    print('no')

# Get an Input age from the user and classify based on the following criteria:
# Child (<13),
# Teen (13–19),
# Adult (20–59),
# Senior (60-100).
# Sample Input:
# 28
# Sample Output:
# Adult
# Sample Input 1:
# 14
# Sample Output 2:
# Teen



x = int(input('Enter the age :'))
if x >= 60:
    print(x, 'is a Senior')
elif x >= 20:
    print(x,'is a Adult')
elif x >= 13:
    print(x, 'is a Teen')
else :
    print(x, 'is a Child')


