a = int(input('Enter the amount:'))
if a >= 1000 :
    amount = a * 0.10
    print(a - amount)
elif a < 1000 and a >= 500 :
    amount = a * 0.5
    print(a - amount) 
else :
    print(a)
