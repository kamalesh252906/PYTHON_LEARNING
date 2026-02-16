# def counts(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count+=1
#     print(count)
# counts(89777)




# def prime(arr):
#     count = 0
#     for i in arr:
#         if i > 1:
#             is_prime = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 count+=1
#     print(count)
# prime([8, 14, 11, 23, 6])


# def two_dimensional(a):
#     min = a[0][0]
#     max = a[0][0]
#     for i in a:
#         for j in i:
#             if j > max:
#                 max = j
#             if j < min:
#                 min = j
#     print(min)
#     print(max)
# two_dimensional([
#     [3, 8, 1],
#     [9, 2, 5],
#     [4, 7, 6]
# ]) 


# def subs(a,b):
#     count = 0
#     for i in range(len(a)-len(b)+1):
#         found = True
#         for j in range(len(b)):
#             if a[i+j] != b[j]:
#                 found = False
#                 break
#         if found:
#             count+=1
#     print(count)
# subs("this is python easy to understand very is easisi","is")



# def is_prime(a):
#     for i in range(0,a+1):
#         if i > 1:
#             prime = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     prime = False
#                     break
#             if prime:
#                 print(i,end=" ")
# is_prime(20)


# def is_prime(a):
#     if a <= 1:
#         print("not a prime")
#     else:
#         prime = True
#         for i in range(2,a):
#             if a % i == 0:
#                 prime = False
#                 break
#         if prime:
#             print("prime number")
#         else:
#             print("not a prime")
# is_prime(11)



# def star(a):
#     for i in range(1,a):
#         for j in range(i):
#             print("*",end= "" " ")
#         print()
# star(4)

# def star(a):
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
# star(3)



# def prime(a):
#     if a <= 1:
#         print("not prime")
#     else:
#         p = True
#         for i in range(2,a):
#             if a % i == 0:
#                 p = False
#                 break
#         if p:
#             print("prime")
#         else:
#             print("not a prime")
# prime(11)

# def lists(a):
#     for i in range(0,a+1):
#         if i > 1:
#             p = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     p = False
#                     break
#             if p:
#                 print(i,end=" ")
# lists(20)
            

# def starts(a,b):
#     for i in range(a,b+1):
#         if a > 1:
#             p = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     p = False
#                     break
#             if p:
#                 print(i,end=" ")
# starts(10,20)



# def star(a):
#     for i in range(0,a+1):
#         space = a - i
#         star = i
#         print("   "*space+"* "*star)
#     for i in range(a-1,0,-1):
#         space = a - i
#         star = i
#         print("   "*space+"* "*star)
# star(5)



# def star(a):
#     for i in range(0,a+1):
#         space = a - i
#         star = i
#         print("* "*star+"   "*space)
#     for i in range(a-1,0,-1):
#         space = a - i
#         star = i
#         print("* "*star+"   "*space)
        
# star(5)
               
            

# n = 9

# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# def pattern(a):
#     for i in range(0,a+1):
#         space = a + i
#         star = i
#         print("   "*space+"* "*star)
#     for i in range(a-1,0,-1):
#         space = a+i
#         star = i
#         print("   "*space+"* "*star)
# pattern(5)


# def star(a):
#     for i in range(0,a+1):
#         space = a - i
#         star = i
#         print(" "*space+"* "*star)
#     for i in range(a-1,0,-1):
#         space = a - i
#         star = i
#         print(" "*space+"* "*star)
# star(9)



# def pattern(a):
#     for i in range(a):
#         for j in range(a):
#             if i == j or i+j==a-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# pattern(7)
















