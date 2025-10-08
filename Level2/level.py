A cinema charges:
* ₹150 for ages under 18
* ₹250 for ages 18–60
* ₹100 for ages above 60

def age(n):
    if n < 18 and n > 0 :
        print('150 rupees')
    elif n >= 18 and n < 60 :
        print('250 rupees')
    elif n >= 60 and n <= 100 :
        print('100 rupees')
    else :
        print('Invalid age') 

age(19)
age(17)
age(65)
age(101)
age(-9)


def num(a,b):
    for i in range(a,b+1):
        print(i)
num(1,10)

def num(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    print(sum)
num(10,20)

def counts(a,b,n):
    add = 0
    if n <= 0 :
        print('Invalid divisor')
    else :
        for i in range(a,b+1):
            if i % n == 0 :
                add = add + 1
        print(add)
counts(1,120,12)

def steps(n):
    if n < 1000 :
        print('No points')
    elif n >= 1000 and n < 5000 :
        a = 5 * n
        b = a // 1000
        print(b)
    elif n >= 5000 :
        if n % 5000 == 0 :
            c = 5 * n
            d = c // 1000 * 20
            print(d)
        else :
            c = 5 * n
            d = c // 1000 + 20
            print(d)
    else :
        print('Invalid')
steps(10000)
steps(6000)
steps(600)


def walk(steps):
    points = (steps // 1000) * 5
    bonus = (steps // 5000) * 20
    total_points = points + bonus
    print(total_points)


walk(10000)
walk(6000)


A stadium sells entry passes with the following rules:
* If age < 12 → Ticket = ₹50
* If age between 12–59 → Ticket = ₹120
* If age ≥ 60 → Ticket = ₹80
Additionally, if the person’s age is a Even number, give a ₹5 discount.
Get the input from the user and return the final discounted stadium ticket price.
Sample Input:
59
Sample Output:
120

def entry_pass(age):
    if age > 0 and age < 12 :
        if age % 2 == 0 :
            print(50-5,'rupees')
        else :
            print('50 rupees')
    elif age >= 12 and age <= 59 :
        if age % 2 == 0 :
            print(120-5,'rupees')
        else :
            print('120 rupees')
    elif age > 59 and age < 100 :
        if age % 2 == 0 :
            print(120-5,'rupees')
        else :
            print('120 rupees')
    else :
        print('Invalid age')

entry_pass(24)
entry_pass(23)
entry_pass(11)
entry_pass(10)
entry_pass(-9)
entry_pass(64)
entry_pass(63)
entry_pass(101)


def employ(salary,sales):
    if sales >= 100:
        bonus = salary * 0.10 + salary
        print(bonus)
    elif sales <= 99 and sales >= 50 :
        bonus = salary * 0.05 + salary
        print(bonus)
    elif sales < 50 and sales > 0 :
        print('No bonus')
    else :
        print('Invalid input')

employ(40000,100)
employ(10000,89)
employ(40000,49)
employ(10000,-9)


A shopkeeper has n mangoes.
He wants to pack them into baskets, with 5 mangoes in each basket.
Write a program to calculate:
* How many full baskets can be made
* How many mangoes will be left
Sample Input:
23
Sample Output:
Full Basket is 4
Left Over mangoes is 3

def mangoes(n):
   print(n//5)
   print(n%5)
mangoes(29)


def num(a,b):
    rev = 0
    for i in range(b,a-1,-1):
        rev += i
        print(i)

num(1,10)


def num(a,b,n):
    total = 0
    for i in range(a,b+1):
        if i % n == 0:
            total = total + 1
    print(total)

num(1,20,10)


def num(a):
    fact = 1
    for i in range(1,a+1,+1):
        fact *= i
    print(fact)
num(5)


def fare(kms):
    if kms <= 10 and kms > 0:
        print(kms*15)
    elif kms > 10 and kms <= 20:
        print(kms*12)
    elif kms > 20 and kms <= 30:
        print(kms*10)
    else :
        print('Invalid')
fare(22)








