# a = 1
# b = 5
# while a <= b :
#     if a % 2 == 0 :
#         print(a)
#     a = a + 1


# a = 1
# b = 5
# sum = 0
# while a <= b :
#     sum = sum + a 
#     a = a + 1
# print(sum)


# a = 1
# b = 15
# sum = 0
# while a <= b :
#     if a % 2 != 0 :
#         sum = sum + a
#     a = a + 1
# print(sum)


a = 1
b = 4
sum = 0
while a <= b:
    sum = sum + a ** 3
    a = a + 1
print(sum)



i = 1
total = 0
while i <= 4:
    total += i**3   # i**3 means cube of i
    i += 1
print("Sum of cubes 1 to 4 =", total)
