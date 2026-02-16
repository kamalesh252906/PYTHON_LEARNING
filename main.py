# section_name = "section-B"
# section_strength = 29
# pi = 3.14
# answer=True
# a=10
# b=10
# print(a+b)
# a=10
# b=20
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(True)
# print(section_name)
# print(section_strength)
# print(pi)
# print(type(section_strength))
# print(type(section_name))
# print(type(pi))
# print(type(True))

# def reverse(n):
#     # start
#     if n >= 0 and n <= 9:
#         return n
#     else:
#         x = n
#         temp = ""
#         digits = []
#         while x > 0:
#             quotient = x // 10  # 134
#             remainder = x % 10  # 2
#             digits.append(remainder)
#             x = quotient
#         print(digits)
#         number = 0
#         for i in range(0,len(digits),+1):
#             temp = (digits[i] * 10 ** (len(digits)-i-1))
#             number = number + temp
#         print(number)
#         # stop

# reverse(1342)

# Find the number of instances of a substring in a string without using any library 
# functionsstring - this is an islandsubstring - is number of instances 3

# def substring(n,m):
#     count = 0
#     for i in range(0,len(n)):
#         if n[i] in m:
# #             count+=1
# #     print(count)
# # substring("this is an island","is")

# def substring(n,m):
#     count = 0
#     li = []
#     for i in range(0,len(n)):
#         li.append(n[i])
#     # print(li)
#     for i in li:
#         if i in m:
#             count +=1
#     print(count)
    
# substring("this is an island","is")