a = 12
b =  10
print(a*b)

k = 'kamalesh'
z = 'batman'
print(k + z)


a = int(input('enter'))
b = int(input('enter'))
for i in range(max(a,b),a*b):
    if i % a == 0 and i % b == 0:
        return i
        