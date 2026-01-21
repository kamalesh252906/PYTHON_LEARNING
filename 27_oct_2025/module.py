# import math
# print(math.sqrt(5))
# print(math.sin(90))

# print(24*60*60)


# def arrays(a):
#     b =[]
#     for i in a:
#         if i == 0:
#             b.append(i)
#     print(b)
# arrays([0, 1, 0, 3, 12])


# word = "Python"
# rev = ""
# for i in range(len(word)):
#     rev = word[i] + rev 
# print("Reversed:", rev)



# text = "Education"
# count = 0
# for ch in text:
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         count = count + 1
# print("Vowels:", count)


# nums = [9, 5, 3, 8]
# min_num = nums[0]
# for i in nums:
#     if i > min_num:
#         min_num = i
# print(min_num)


# def lists(a):
#     b = []
#     for i in range(0,len(a),+2):
#         b.append(a[i])
#     print(b)
# lists([10,20,30,40,50,60])


# def nums(a):
#     for i in range(0,len(a)):
#         if a[i] < 0:
#             a[i] = 0
#     print(a)
# nums([-3,5,-2,7])


# nums = [-3, 5, -2, 7]
# for i in range(len(nums)):
#     if nums[i] < 0:
#         nums[i] = 0

# print(nums)   # Output: [0, 5, 0, 7]


# def words(a):
#     b = ['a','e','i','o','u']
#     c = []
#     for i in a:
#         if i in b:
#             c.append(i)
#     print(c)
# words('education')


words = ["cat", "eagle", "umbrella", "sky"]
vowels = "aeiou"

max_vowels = 0
word_with_max = ""

for i in range(len(words)):           # outer loop for each word
    count = 0
    for j in range(len(words[i])):    # inner loop for each character
        if words[i][j] in vowels:
            count += 1
    if count > max_vowels:
        max_vowels = count
        word_with_max = words[i]

print(word_with_max)



# def nums(a):
#     count = 0
#     sum = 0
#     dicts = {}
#     for i in a:
#         if i % 2 == 0:
#             count += 1
#     for i in a:
#         if i % 2 != 0:
#             sum += 1
#     dicts['even'] = count
#     dicts['odd'] = sum
#     return dicts
# print(nums([1, 2, 3, 4, 5, 6, 7]))



# nums = [2, 4, 6, 4, 8, 4, 10]
# target = 4

# first = -1
# last = -1

# for i in range(len(nums)):
#     if nums[i] == target:
#         if first == -1:     
#             first = i
#         last = i            

# result = {"first_index": first, "last_index": last}
# print(result)

# # - Combine Two Lists Alternately
# #   Write a Python program to combine two lists by picking elements alternately.
# #   (Assume both lists are of the same length.)

# def combine_list(n,m):
#     new=[]
#     for i in range(0,len(n)):
#         new.append(n[i])
#         new.append(m[i])
#     print(new)
# combine_list([10, 20, 30],[1, 2, 3])

    

