# def counts(a):
#     b = []
#     count = 0
#     for i in a:
#         if i == 0:
#             count+=1
#         elif count == 1:
#             b.append(i)
#     print(b)
# counts([1,2,3,0,9,8,7,6,0])


# def longest(a):
#     maxi = a[0]
#     for i in a:
#         if len(i) > len(maxi):
#             maxi = i
#     print(maxi)
# longest(["thalapathy","thala","superstar"])


# def counts(a):
#     b = ""
#     for i in a:
#         if i not in b:
#             b+=i
#     print(b)
# counts("programming")

# def counts(a,b):
#     count = 0
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             var = a[i:j+1]
#             if var == b:
#                 count+=1
#     print(count)
# counts("ababab","aba")


# def remove(a,b):
#     print(a.replace(b,""))
# remove("testcase","case")


# def remove(a,b):
#     c = ""
#     i = 0
#     while i < len(a):
#         if a[i:i+len(b)] == b:
#             i =i + len(b)
#         else:
#             c+=a[i]
#             i+=1
#     print(c)
# remove("testcase","case")


# def find(a):
#     mug = 1500/3
#     jean = 3000
#     tshirt = 1500
#     pen = 10
#     total = 0
#     for i in range(len(a)):
#         b = int(a[i].split(" ")[1])
#         if a[i][0] == "M":
#             total+=mug*b
#         elif a[i][0] == "J":
#             total+=jean*b
#         elif a[i][0] == "T":
#             total+=tshirt*b
#         elif a[i][0] == "P":
#             total+=pen*b
#     print(total)
# find(["M 3", "J 1", "T 2"])



# def find(names,birthdates):
#     b = []
#     for i in range(len(birthdates)):
#         month = int(birthdates[i].split("/")[1])
#         if month in [1,2,3,4,5,6]:
#             b.append(names[i])
#     print(b)
# find(["john","leo","yash","dev"],["25/3/2006","29/9/2006","12/12/2007","01/1/200"])


# def counts(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count+=1
#     print(count)
# counts(123)



# def sat(a):
#     b = str(a)
#     c = ""
#     count = 0
#     for i in b:
#         if i not in c:
#             c+=i
#             count+=1
#     if count == 2:
#         print("Saturated")
#     else:
#         print("Unsaturated")
# sat(123)


# def seconds(a):
#     first = second = a[0]
#     for i in a:
#         if i > first:
#             first = i
#     for j in a:
#         if j!=first and j > second:
#             second = j
#     print(second)
# seconds([1,2,3,4,9])




# def find(arr,value):
#     if len(arr) == 0:
#         print(-1)
#     else:
#         for i in range(len(arr)):
#             if arr[i] == value:
#                 print(i)
#                 break
#         else:
#             print(-1)
# find([9, 7, 4, 1, 7, 0], 2)


# def stud(names,physics,chemistry,maths,subject):
#         if subject == "physics":
#             maxi = physics[0]
#             index = 0
#             for i in range(len(names)):
#                 if physics[i] > maxi:
#                     maxi = physics[i]
#                     index = i
#             print(names[index])

#         elif subject == "chemistry":
#             maxi = chemistry[0]
#             index = 0
#             for i in range(len(names)):
#                 if chemistry[i] > maxi:
#                     maxi = chemistry[i]
#                     index = i
#             print(names[index])

#         elif subject == "maths":
#             maxi = maths[0]
#             index = 0
#             for i in range(len(names)):
#                 if maths[i] > maxi:
#                     maxi = maths[i]
#                     index = i
#             print(names[index])

#         else:
#             print("Invalid Subject")
# stud(["Arun", "Bala", "Cathy", "Divya"] , [88, 92, 76, 90] , [81, 89, 95, 70] , [90, 87, 85, 91] , "physics")



# def remove(a):
#     b = ""
#     for i in a:
#         if i not in "aeiouAEIOU":
#             b+=i
#     print(b)
# remove("apple")


# def lists(a):
#     b = []
#     count = 0
#     for i in a:
#         count+=i
#     avg = count/len(a)
#     sum = 0
#     for i in a:
#         if i > avg:
#             b.append(i)
#             sum+=1
#     print(b)
#     print(sum)
# lists([10,20,30,40,50])



# def print_m_pattern(n):
#     for i in range(1, n+1):
#         space = n - i
#         star = i
#         print("  " * space + "* " * star)

#     for i in range(n-1, 0, -1):
#         space = n - i
#         star = i
#         print("  " * space + "* " * star)

#     print()
# print_m_pattern(3)



# def print_m_pattern(n):
#     for i in range(1,n+1):
#         space = n - i
#         star = i
#         print("  "*space+"* "*star)
#     for i in range(n-1,0,-1):
#         space = n - i
#         star = i
#         print("  "*space+"* "*star)
#     print()
# print_m_pattern(3)



# def remove_duplicates_row_wise(arr):

#     for row in arr:
#         unique = []

#         for num in row:
#             if num not in unique:
#                 unique.append(num)
#         for val in unique:
#             print(val, end=" ")
#         print()
# remove_duplicates_row_wise([
#     [1, 2, 2, 3],
#     [4, 4, 5, 4],
#     [7, 8, 8, 7, 9]
# ])





