n = int(input('Enter a year:'))
if n % 100 !=0 and n % 4 ==0 or n % 400 ==0 :
    print('Y')
else :
    print('N')


a = int(input('Enter a number:'))
b = int(input('enter a number:'))
sum = 0
while a <= b :
    if a % 2 == 0:
        sum += a
    a += 1
print(sum)

# . Write a program that calculates the shipping cost for an e-commerce product based
# on weight. If the weight is less than or equal to 5 kg, the shipping cost is $10; if the
# weight is more than 5 kg but less than or equal to 20 kg, the cost is $20; for more than
# 20 kg, the cost is $50. Please add 5% tax to the end shipping cost.
# ● Input: The weight of the product in kilograms.
# ● Output: The shipping cost (edited)
#  Grade 100 S 90 - 99 A 80 - 89 B 70 - 79 C 60 - 69 D 50 - 59 E
# < 50 F
# Program to calculate shipping cost with tax

weight = float(input("Enter the weight of the product: "))
if weight <= 5:
    cost = 10
elif weight <= 20:
    cost = 20
else:
    cost = 50
total_cost =(cost * 1.05)

print("Final Shipping Cost = $", total_cost)

a = int(input('Enter the marks:'))
if a == 100 :
    print('S')
elif a < 100 and a >= 90 :
    print('A')
elif a < 90 and a >= 80 :
    print('B')
elif a < 80 and a >= 70 :
    print('C')
elif a < 70 and a >= 60 :
    print('D')
elif a < 60 and a >= 50 :
    print('E')
elif a < 50 and a > 0 :
    print('F')
else :
    print('Invalid Input')

a = input('P for pizza, B for burger, S for sandwich:')
b = int(input('Enter quantity:'))
if b > 0 :
    if a == 'P':
        print(b*200*1.05)
    elif a == 'B':
        print(b*100*1.05)
    elif a == 'S':
        print(b*50*0.05)
    else :
        print('Invalid Input')
else :
    print('Invalid input')

