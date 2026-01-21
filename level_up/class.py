# def word(a):
#     count = 0
#     b = "aeiouAEIOU"
#     for i in a:
#         if i in b:
#             count += 1
#     print(count)
# word('hariharnbatman')


# def numbers(a):
#     b =[]
#     for i in a:
#         if i % 2 == 0:
#             b.append(i)
#     print(b)
# numbers([2,1,4,16,90,67,4,80])



# def reverse(a):
#     b = ""
#     for i in range(len(a)-1,-1,-1):
#         b = b + a[i]
#     print(b)
# reverse('apple')


# def lists(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)
# lists([1,2,2,3,4,3,5,6,5])


# def large(a):
#     for i in a:
        
# large([20,90,78,67])

# def pali(a):
#     b = ""
#     for i in range(len(a)-1,-1,-1):
#         b += a[i]
#     if b == a:
#         print('palindrome')
#     else:
#         print('not')
# pali('madam')
# pali('hello')

# def lists(a,b):
#     c = []
#     for i in a:
#         if i in b:
#             c.append(i)
#     print(c)
# lists([1,2,3,2,3,4],[1,6,2,3,4])

# def lists(a):
#     shortest = a[0]
#     longest = a[0]
#     for i in a:
#         if len(i) < len(shortest):
#             shortest = i
#             # return shortest
#         elif len(i) > len(longest):
#             longest = i
#             # return longest
#     print("Shortest:", shortest)
#     print("Longest:", longest)

# # sort_by_length(["cat", "elephant", "dog", "tiger"])

# lists(['eat','elephant','dog','lion'])


# def add(a):
#     b = []
#     c = []
#     for i in a:
#         if i % 2 == 0:
#             b.append(i)
#         else:
#             c.append(i)
#     print(b)
#     print(c)
# add([2,1,3,34,56,23,3])


# def candles(a):
#     max = 0
#     count = 0
#     for i in a:
#         if i > max :
#             max = i
#     for j in a:
#         if max == j:
#             count += 1
#     print(count)
# candles([2,4,4,1,3,4,5,5,5])



# def search(a,b):
#     for i in range(0,len(a),+1):
#         if a[i] in b:
#             print(i)
# search([1,2,3,4,9,8],[9])


# def words(a):
#     b = ""
#     for i in range(0,len(a),+1):
#         if a[i] == " " :
#             b = b + "-"
#         else:
#             b = b + a[i]
#     print(b)
# words("Learn Python Easily")


# def lists(a):
#     b = [11,22,33,44,55]
#     p = 0
#     for i in range(0,len(b),+1):
#         if b[i] == a:
#             p = i
#     print(p)
# lists(33)


# def lists(a,b):
#     count = 0
#     for i in range(0,len(a),+1):
#         if a[i] < b[i]:
#             count += 1
#     print(count)
# lists([1,3,4,2],[6,7,3,4])

# def lists(a,b):
#     y = 0
#     for i in range(0,len(a),+1):
#         if a[i] == b:
#             y = i
#     print(y)
# lists([2,3,4,5,6,7],5)



# data = {'name': 'kamalesh', 'city': 'chennai', 'age': '21'}

# new_data = {}
# for k in data:
#     new_data[k.upper()] = data[k]

# print(new_data)






