# def funcg(arr,key):
#     left = 0
#     right = len(arr)-1
#     center = (left - right)//2+1
#     while left <=right:
#         if arr[center] == key:
#             return True
#         if arr[center] < key:
#             right = center - 1
#         if arr[center] > key:
#             left = center + 1
#     return -1

# lists = [12,90,87,56,43,25,99]
# y = 25

# result = funcg(lists,y)

# if result != -1:
#     print("found index at" , result)
# else:
#     print("Not found")


# def binary_search(arr, key):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1
# lists = [12, 25, 43, 56, 87, 90, 99]  # MUST be sorted
# y = 99

# result = binary_search(lists, y)

# if result != -1:
#     print("Found index at", result)
# else:
#     print("Not found")


# def fact(a):
#     if a == 0:
#         return "Invalid"
#     elif a == 1:
#         return 1
#     elif a > 1:
#         return a*fact(a-1)
# print(fact(6))