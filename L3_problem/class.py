# def reverse_alternate(sentence):
#     words = sentence.split()
#     new = []
#     index = 0

#     for w in words:
#         if index % 2 == 1:     # odd index → reverse the word
#             rev = ""
#             for ch in w:
#                 rev = ch + rev
#             new.append(rev)
#         else:                  # even index → keep same
#             new.append(w)
#         index += 1

#     result = ""
#     for i in range(len(new)):
#         if i == len(new) - 1:
#             result += new[i]
#         else:
#             result += new[i] + " "

#     print(result)


# reverse_alternate("Python is super powerful and amazing")



# def counts(nums):
#     even_sum = []
#     odd_sum = []

#     for i in nums:
#         sum = 0
#         for j in str(i):
#             sum += int(j)
#         if sum % 2 == 0:
#             even_sum.append(i)
#         else:
#             odd_sum.append(i)

#     result = even_sum + odd_sum
#     print(result)

# counts([12, 35, 40, 13, 111])




# def counts(a):
#     result = []
#     for i in a:
#         if i % 2 == 0:
#             result.append(i)
#         elif i % 2 != 0:
#             break
#     print(result)
# counts([2,4,6,3,8,10])



# def upper(a):
#     b = []
#     c = "QWERTYUIOPASDFGHJKLZXCVBNM"
#     for i in range(0,len(a)):
#         if a[i][0] in c:
#             b.append(a[i])
#     print(b)
# upper(["Apple",'ball',"Cat",'dog'])


# def lists(a):
#     b = []
#     for i in range(0,len(a)):
#         if a[i] >= 1000 and a[i] <= 9999:
#             if a[i] % 2 == 0:
#                 b.append(a[i])
#     print(b)

# lists([2481,3572,602,7890,4214])


# def alpha(a):
#     b = ""
#     c = "qwertyuiopasdfghjklzxcvbnm"
#     for i in a:
#         if i in c:
#             b +=i
#     print(b)
# alpha("PyTHonProGRam")


# def alpha(a):
#     b = []
#     for i in a:
#         if i[0] == i[-1]:
#             b.append(i)
#     print(b)
# alpha(["Apple", "ball",'level',])


# def marks(a,b):
#     c = []
#     for i in range(0,len(a)):
#         if a[i] > 80 and b[i] > 80:
#             c.append(i)
#     print(c)
# marks([92, 45, 81] , [88, 90, 70])



# def floats(a):
#     b = []
#     for i in a:      
#         if type(i) == float:
#             b.append(i)
#     print(b)

# floats([10, 3.5, "hello", 8.2, 6])


# def chars(a):
#     for i in a:
#         if i[0] == i[-1]:
#             print(i)
# chars(["level", "apple", "noon", "code"])


# def vowels(a):
#     b = []
#     c = "aeiou"
#     for i in a:
#         count = 0
#         for w in i:
#             if w in c:
#                 count +=1
#         if count == 2:
#             b.append(i)
#     print(b)

# vowels(["team", "sky", "apple", "road"])



# def odd(a):
#     b = []
#     for i in a:
#         c = i % 10
#         d = i // 10
#         if c % 2 != 0 and d % 2 !=0:
#             b.append(i)
#     print(b)
# odd([13, 22, 51, 87])


# def words(a):
#     b = "aeiou"
#     for i in a:
#         count = 0
#         sum = 0
#         for el in i:
#             if el in b:
#                 count += 1
#             else:
#                 sum +=1
#         if sum > count:
#             print(i)
# words(["apple", "tree", "rhythm", "code"])

# def counts(a):
#     for i in a:
#         b = str(i)
#         count = 0
#         for el in b:
#             if el == '0':
#                 count +=1
#         if count == 1:
#             print(i)
    
            

# counts([10, 101, 2005, 340, 89])




# def equal(a):
#     c = []
#     for i in a:
#         b = ""                 
#         for el in i:
#             if el not in b:
#                 b += el
#         if len(b) == len(i):
#             c.append(i)
#     print(c)

# equal(["apple", "cat", "moon", "dog"])


# def match(a):
#     b = "qwertyuiopasdfghjklzxcvbnm"
#     for i in a:
#         count = 0
#         sum = 0
#         for el in i:
#             if el in b:
#                 count +=1
#             else:
#                 sum +=1
#         if sum > count:
#             print(i)
# match(["HeLLo", "WORLD", "python", "ApP"])






# x=[12, 14, 77, 30]
# o = []
# for i in x:
#     b = i%10
#     c = i//10
#     d = str(b)
#     e = str(c)
#     t = d + e
#     y = int(t)
#     if y > i:
#         o.append(i)
# print(o)


# def loose(names,birthdates):
#     result = []
#     for i in range(len(birthdates)):
#         month = int(birthdates[i].split("/")[1])
#         if month in [1, 2, 3, 4, 5, 6]:
#             result.append(names[i])
#     print(result)
# loose(["hari","venkat","koli","azhagan"],["01/09","02/05","04/03","30/03"])


# def counts(a):
#     b = "aeiouAEIOU"
#     c = []
#     for i in a:
#         if len(i) % 2 != 0:
#             mid = len(i) // 2
#             # for j in i:
#             if i[mid] in b:
#                 c.append(i)
#     print(c)
# counts(["cat","cream","joy","last","lost"])



# def counts(a):
#     for i in a:
#         count = 0
#         sum = 0
#         for j in i:
#             if j in "aeiou":
#                 count +=1
#             else:
#                 sum +=1
#         if sum == count:
#             print(i)
# counts(["baal","cat","room","man"])


# def counts(a):
#     result = []
#     count = 0
#     for i in a:
#         if i == 0:
#             count +=1
#         if count == 1:
#             result.append(i)
#     print(result)
            

# counts([10, 101, 2005, 340, 89])


# def compare(a):
#     b = []
#     for i in a:
#         for j in range(0,len(i)):
#             if i[j-3] == "i" and i[j-2] == "n" and i[j-1] == "g":
#                 b.append(i)
#     print(b)
# compare(["playing", "run", "walking", "see", "coding"])




# def top_vowel_students(students, scores):
#     vowels = "AEIOUaeiou"
#     total = 0
#     for score in scores:
#         total += score
#     avg = total / len(scores)
#     result = []
#     for i in range(len(students)):
#         name = students[i]
#         count = 0
#         for ch in name:
#             if ch in vowels:
#                 count += 1
#         if count >= 3 and scores[i] > avg:
#             result.append(name)

#     print(result)
# top_vowel_students(["Aravind", "Bala", "Eeshwar", "Louis", "Gita"],[85, 70, 92, 88, 60])


# def chars(a):
#     b = a.split(" ")
#     n = ""
#     for i in b:
#         if len(i) <= 3:
#             n = n + i + " "
#         else:
#             j = i[::-1]
#             n = n + j + " "
#     print(n)

# chars( "I love is writing python code")

# def saturated(n):
#     count = 0
#     if n >= 1 and n <= 9999:
#         b = str(n)
#         c = ""
#         for i in b:
#             if i not in c:
#                 c +=i
#         for j in c:
#                 count +=1
#         if count == 2:
#             print("Saturated")
#         else:
#             print("Unsaturated")
# saturated(9199)



# def saturated(n):
#     # start
#     if n == 0:
#         print("Unsaturated")
#     else:
#         x = n
#         nums = []
#         while x > 0:
#             div = x % 10
#             quot = x // 10
#             nums.append(div)
#             x = quot


#         count = 0
#         result = []
#         for i in range(0, len(nums), +1):
#             if nums[i] in nums[i : len(nums) - 1]:
#                 count += 1
#             if count == 1:
#                 result.append(nums[i])
#             count = 0
#         if len(result) == 2 :
#             print("Saturated")
#         else:
#             print("Unsaturated")
# saturated(9199)





# def counts(arrays):
#     if len(arrays) == 0:
#         print("Invalid Input")
#     else:
#         count = 0
#         sum = 0
#         for i in arrays:
#             count+=i
#         avg = count/len(arrays)
#         for i in arrays:
#             if i > avg:
#                 sum+=1
#         print(sum)
# counts([10,20,30,40,50])
# counts([5,5,5,5])


# def duplicate(a):
#     if len(a) == 0:
#         print("Invalid Input")
#     else:
#         b = ""
#         for i in a:
#             if i not in b:
#                 b +=i
#         print(b)
# duplicate('programming')
# duplicate("")



# def longest(a):
#     if len(a) == 0:
#         print("Invalid Input")
#     else:
#         b = a.split(" ")
#         big = b[0]
#         for i in range(len(b)):
#             if len(b[i]) > len(big):
#                 big = b[i]
#         print(big)

# longest("Python makes programming enjoyable")



        

# def longest(a):
#     b = a.split(" ")
#     c = b[0]
#     for word in b:
#         if len(word) > len(b):
#             b = word
#     print(b)
# longest("Data science evolves every year")


# def largest(a):
#     b = a.split()
#     add = []
#     c = "aeiouAEIOU"
#     for i in b:
#         count = 0
#         for j in i:
#             if j in c:
#                 count+=1
#         add.append(count)
#     f = add[0]
#     for i in range(len(add)):
#         if add[i] > f:
#             f = add[i]
#     print(b[i])
# largest("Learning Python is interesting")


# def greater(a):
#     b = a.split()
#     for i in b:
#         if len(i) > 4:
#             print(i)
# greater("This is a python program")




# def largest(a):
#     b = a.split()
#     add = []
#     count = 0
#     c = "aeiouAEIOU"
#     for i in b:
#         if c in i:
#             count+=1
#         add.append(count)
#     f = add[0]
#     for i in range(len(add)):
#         if add[i] > f:
#             f = add[i]
#     print(b[i])
# largest("Learning Python is interesting")
































                

        































