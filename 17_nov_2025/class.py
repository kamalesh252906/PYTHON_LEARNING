# def reverse(a):
#     b = []
#     for i in range(len(a),0,-1):
#         b.append(i)
#     print(b)
# reverse([1,2,3,4,5]) 


# def upper(a):
#     count = 0
#     b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     for i in a:
#         if i in b:
#             count +=1
#     print(count)
# upper('WelComeTo')


# def long(a):
#     longest = ""
#     current = ""
#     for i in a:
#         if i != " ":
#             current += i
#         else:
#             if len(current) > len(longest):
#                 longest = current
#             current = ""
#     if len(current) > len(longest):
#         longest = current

#     print(longest)

# long("Johannesburg is the most populous city of South Africa")


# def rotate(a,b):
#     b = b % len(a)
#     print(a[:-b] + a[-b]):
# rotate([1,2,3,4,5],2)



# def swap_around_and(sentence):
#     words = sentence.split()
#     for i in range(len(words)):
#         if words[i] == "and":
#             words[i-1], words[i+1] = words[i+1], words[i-1]
#     print(" ".join(words))
# swap_around_and("apple and banana")


# def long(a):
#     longest = ""
#     current = ""
#     for i in a:
#         if i != " ":
#             current += i
#         else:
#             if len(current) > len(longest):
#                 longest = current
#             current = ""
#     if len(current) > len(longest):
#         longest = current

#     print(longest)

# long("Johannesburg is the most populous city of South Africa")


# def smallest_word(a):
#     words = a.split()
#     a = words[0]
#     for i in words:
#         if len(i) < len(a):
#             a = i
#     print(a)

# smallest_word("Python is super powerful")


# def great(a):
#     for i in range(0,len(a)- 1):
#         if a[i+1] <= a[i]: 
#             print(False)
#             return
#     print(True)


# great([1,2,3,4,5])   # True
# great([1,2,2,3])     # False
# great([10,5,6])      # False


# def rev_even(s):
#     even = ""
#     for i in range(0, len(s), 2):
#         even = s[i] + even  # reverse by front-adding
#     out = ""
#     e_index = 0
#     for i in range(len(s)):
#         if i % 2 == 0:
#             out += even[e_index]
#             e_index += 1
#         else:
#             out += s[i]
#     return out

# print(rev_even("abcdefg"))


# def replace(a):
#     b = ""
#     for i in range(0,len(a)):
#         if i % 2 == 0:
#             b += a[i]
#         else:
#             b += '*'
#     print(b)
# replace("Hello")



# def counts(a):
#     b = ""
#     # count = 0
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count += 1
#                     b +=i
#             print(i , count)
# counts('succccess')



# def counts(a):
#     b = ""
#     for i in a:
#         count = 0
#         for j in a:
#             if i == j:
#                 count += 1
#     print(i ,'-',count)
# counts('yashika')


# def vowels(a):
#     b = []
#     c = "aeiou"
#     for i in range(0,len(a)):
#         if a[i] in c:
#             b.append(i)
#     print(b)
# vowels("education")


# def chars(a,c):
#     b = ""
#     for i in range(0,len(a),c):
#         b += a[i]
#     print(b)
# chars("abcdefghijklmnopqrstuvwxyz",2)




# def counts(a):
#     b = ""
#     # count = 0
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count += 1
#                     b += i
#             print(i,"->",count)
# counts("yashika")


# def between(a):
#     b = []
#     count = 0
#     for i in a:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# between([1,2,0,6,5,4,0])


# def second(a):
#     first = second = a[0]
#     for i in range(0,len(a)):
#         if a[i] > first:
#             second = first
#             first = a[i]
#         elif a[i] > second and a[i] != first:
#             second = a[i]
#     print(second)
# second([1,2,5,3,4,5])

# def sec(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     f = s = b[0]
#     for j in b:
#         if j > f:
#             s = f
#             f = j
#         elif j > s and j != f:
#             s = j
#     print(s)
# sec([9,8,7,9])

# def sec(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)

#     f = b[0]
#     s = -100

#     for j in b:
#         if j > f:
#             s = f
#             f = j
#         elif j > s and j != f:
#             s = j
#     print(s)

# sec([9,8,7,9])


# def lion(a):
#     count = 0
#     for i in a:
#         if i == "(":
#             count +=1
#         elif i == ")":
#             count -=1
#             if count < 0:
#                 print(False)
#                 return
#     if count == 0:
#         print(True)
#     else:
#         print(False)
# lion("(((())))")




# def square(a):
#     b = []
#     for i in range(0,len(a)):
#         if i % 2 == 0:
#             b.append(a[i]*a[i])
#         else:
#             b.append(a[i])
#     print(b)
# square([0,1,2,3,4,5,6])

# def query(a):
#     b = ""
#     c =  ""
#     d = ""
#     for i in range(2,len(a)-2):
#         b = a[i] + b
#     for i in range(0,2):
#         c +=a[i]
#     for i in range(len(a)-2,len(a)):
#         d +=a[i]
#     print(c+b+d)
# query("Success")


# def post(a):
#     count = 0
#     for i in range(0,len(a),len(a)-1):
#         count +=a[i]
#     print(count)
# post([1,2,3,4,5])




# def nums(a,b):
#     for i in range(0,len(a)):
#         if a[i] == b:
#             print(i)
# nums([11,22,33,44,55],33)




# def chars(a):
#     b = ""
#     for i in a:
#         count = 0         
#         for j in a:
#             if i == j:
#                 count += 1
#         if count == 1: 
#             b += i
#             break
#     print(b)
# chars("swiss")


# def chars(a):
#     count = 0
#     b = []
#     for i in a:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# chars([1,2,0,9,8,7,0])


# def ascend(a):
#     b = []
#     min = a[0]
#     for i in a:
#         if i < min:
#             min = i
#             # min = i
#             print(i)
# ascend([4,3,2,1,9,8])

# def letter(a):
#     # count = 0
#     b = ""
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count +=1
#                     b +=i
#             print(i,count)
# letter("malayalam")


# def counts(a):
#     count = 0
#     b = []
#     for i in a:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# counts([1,0,9,6,4,0])

        






































































        













