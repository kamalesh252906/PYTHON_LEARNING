# def selection(a):
#     n = len(a)
#     for i in range(0,n):
#         min_index = i
#         for j in range(i+1,n):
#             if a[j] < a[min_index]:
#                 min_index = j
#         temp = a[min_index]
#         a[min_index] = a[i]
#         a[i] = temp
#     return a
# print(selection([50,20,30,40,10]))


# def select(n):
#     m = len(n)
#     for i in range(0,m):
#         index = i
#         for j in range(i+1,m):
#             if n[j] < n[index]:
#                 index=j
#         n[i],n[index] = n[index] , n[i]
#     return n
# print(select([10,90,70,45,87,100]))
