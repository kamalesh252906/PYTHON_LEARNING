# def sen(a):
#     count = 0
#     b = 'qwertyuiopasdfghjklzxcvbnm'
#     for i in b:
#         if i in a:
#             count += 1
#     if count == 26:
#         print(True)
#     else:
#         print(False)
# sen('The quicks brown fox jumps over the  dog')
# sen('The quick brown fox jumps over the lazy dog')

# def pali(a):
#     v = a.lower()
#     b =""
#     c = ""
#     for i in v:
#         if i not in " ":
#             b += i
#     # print(b)
#     for j in range(0,len(b)):
#         c = b[j] + c
#     if b == c:
#         print('pali')
#     else:
#         print('Not pali')
# pali('Too hot to hoot')


# def pali(a):
#     b = ""
#     c = ""
#     for i in a:
#         if i != " ":
#             b += i
#             c += i
#     if b == c:
#         print('Pali')
#     else:
#         print('Not pali')

# pali('Too hot to hoot')


# def comps(a):
#     b = a.title()
#     t =""
#     c = " "
#     for i in range(0,len(a)):
#         if a[i] not in c:
#             t = t + a[i]
#     print(c)

# comps('welcome to python')


# class Order:
#     def __init__(self):
#         self.cart = []    

#     def add_item(self, name, price, qty):
#         item = {"name": name, "price": price, "qty": qty}
#         self.cart.append(item)

#     def total(self):
#         total = 0
#         for item in self.cart:
#             total += item["price"] * item["qty"]
#         print("Total amount:", total)

# # 🔹 create object
# c = Order()
# c.add_item("Levis", 900, 2)
# c.add_item("Nike", 1200, 2)
# c.total()







# def second_largest(a):
#     first = second = a[0]
#     for i in a:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             second = i
#     print(second)

# second_largest([10, 30, 44, 9, 100])



# def parentheses_match(s):
#     count = 0
#     for ch in s:
#         if ch == '(':
#             count += 1
#         elif ch == ')':
#             count -= 1
#         if count < 0:       
#             print(False)
#             return
#     print(count == 0)       

# parentheses_match("())(")     
# parentheses_match("((()))")   




# def between(a):
#     b = []
#     count = 0
#     for i in a:
#         if i == 0:
#             count+=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# between([10,34,23,0,9,8,7,55,0])


# def second(a):
#     first = second = a[0]
#     for i in a:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             second = i
#     print(second)
# second([12,78,56,34,2])

# def between(a):
#     b = []
#     count = 0
#     for i in a:
#         if i == 0:
#             count +=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# between([12,89,0,9,8,7,2,3,1,0])

# def duplicate(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)

#     print(b)
# duplicate([10,10,90,90,12,12,13])


# def counts(a):
#     b = ""
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count += 1
#                     b +=i
#             print(i , count)
# counts('success')


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
#     b = 'aeiouAEIOU'
#     c = ""
#     for i in a:
#         if i not in b:
#             c += i
#     print(c)
# vowels('education')

# def pali(a):
#     b =""
#     for i in a:
#         b = i + b
#     if a == b:
#         print("Palindrome")
#     else:
#         print("not palindrome")
# pali("level")
# pali("hari")


# def second(a):
#     first = second = a[0]
#     for i in a:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             second = i
#     print(second)
# second([1,2,3,5,9])


# def brackets(a):
#     count = 0
#     for i in a:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -=1
#             if count < 0:
#                 print(False)
#                 break
#     if count == 0:
#         print(True)
# brackets("())")
# brackets("(())")


# def is_input(a):
#     count = 0
#     result = []
#     for i in a:
#         if i == 0:
#             count = count + 1
#         elif count ==1:
#             result.append(i)
#     print(result)


# def counts(a):
#     large = a[0]
#     second = a[0]
#     for i in a:
#         if i > large:
#             large = i
#     for j in a:
#         if j != large and j > second:
#             second = j
#     print(second)
# counts([1,2,3,4,6,5,10,1])



# def counts(a):
#     count = 0
#     b = []
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count +=1
#                     b.append(i)
#             print(i , count)
# counts([1,1,2,2,3,4,5,1,2])


# def counts(a):
#     b = ""
#     for i in a:
#         count = 0
#         for j in a:
#             if i == j:
#                 count +=1
#                 b +=i
#     print(i , "->",count)
# counts("saravana")



# def middle(a):
#     n = len(a)
#     if n == 0:
#         print(None)
#     elif n % 2 == 1:
#         print(a[n // 2])
#     else:
#         print(a[n // 2 -1] , a[n // 2])
# middle([2,4,9,5])

# def highest_marks(names, maths, physics, chemistry):
#     topper = ""
#     top_total = 0
#     found = False

#     for i in range(len(names)):
#         if maths[i] > 90 and physics[i] > 90 and chemistry[i] > 90:
#             found = True
#             total = maths[i] + physics[i] + chemistry[i]
#             if total > top_total:
#                 top_total = total
#                 topper = names[i]

#     if found:
#         print("Topper:", topper)
#     else:
#         print("No student found")


# highest_marks(["jason", "priya", "madhan", "syed"], 
#               [91, 92, 81, 75],
#               [91, 89, 100, 90],
#               [91, 95, 100, 90])

# highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
# [85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
# [84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
# [86, 85, 84, 83, 87, 88, 82, 81, 85, 86])

# def counts(a):
#     b = ""
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count +=1
#                     b +=i
#             print(i,"->",count)
# counts("hariharan")


# def longest(a):
#     b = a.split()
#     print(b)
#     c = a[0]
#     for i in b:
#         if len(i) < len(b):
#             b = i
#     print(c)
# longest("hari",)


# def combine(a,b):
#     c = []
#     for i in range(0,len(a)):
#         c.append(a[i])
#         c.append(b[i])    
#     print(c)
# combine([1,3,5], [2,4,6])



# a = [5, 1, 4, 2, 3]
# result = []
# small = a[0]
# while a:
#     small = a[0]             

# for i in a:              # list la each element check pandrom
#     if i < small:        # smaller value kedaicha update pannrom
#         small = i

#     result.append(small)     # smallest add pannrom result la
#     a.remove(small)          # original list la irundhu delete pannrom
#     print(result)

# def targets(a,b):
#     c=[]
#     for i in range(0,len(a)):
#         for j in range(1,len(a)-1):
#             if a[i] + a[j] == b:
#                 c.append(i),c.append(j)        
#     print(c)
# targets([1,2,3,4],5)

# def appear(a):
#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[i] == a[j]:
#                 print(True)
#                 return
#     print(False)
# appear([1,2,3])
# appear([1,1,1,3,3,4,3,2,4,2])
# appear([1,2,3,4])


# def counts(a):
#     count = 0
#     b = []
#     for i in a:
#         if i == 0:
#             count+=1
#         elif count == 0:
#             b.append(i)
#     print(b)
# counts([1, 1, 1, 0, 1, 0, 1, 1, 0, 1])

# def counts(a,b):
#     c = []
#     # d = len(a) - b
#     for i in range(len(a)-b,0,+1):
#         c.append(a[i])
#     print(c)
# counts([10,20,30,40,50],4)



# def chars(a):
#     for i in range(0,len(a)):
#         if a[i] == 's' or a[i] == 'h':
#             print(i)
# chars("Nandhinis")



# def counts(a,b):
#     for i in range(0,len(a)):
#         if a[i] == b:
#             print(i)
#             return
#     print(-1)
# counts([1,2,3,4,5],5)



# def zero(a,b):
#     count = 0
#     c = []
#     for i in range(0,len(a)):
#         if a[i] == b:
#             count +=1
#         elif count == 1:
#             c.append(i)
#     print(c)
# zero([5,4,0,9,8,7,0,3,2],0)




# def sums(a,b):
#     c = []
#     for i in range(0,len(a)):
#         count = 0
#         for j in range(i,len(a)):
#             count +=a[j]
#             if count == b:
#                 print([i,j])
#                 return
#             if count > b:
#                 break
#     print([-1])
# sums([1,2,3,4,5],6)


# def last(a):
#     count = 0
#     for i in range(0,len(a),len(a)-1):
#         count +=a[i]
#     print(count)
# last([10,2,3,4,5])


# def combine(a,b):
#     c =[]
#     for i in range(0,len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     print(c)
# combine([1,3,5,7,9], [2,4,6,8,10])


# def counts(a):
#     b = ""
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     b +=i
#                     count +=1
#             print(i,count)
# counts("success")




# result = []
# for i in range(len(birthdates)):
#     month = int(birthdates[i].split("/")[1])
#     if month in [1, 2, 3, 4, 5, 6]:
#         result.append(names[i])
# print(result)





        






                

































































