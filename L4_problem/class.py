# def counts(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count+=1
#     print(count)
# counts(89777)




def prime(arr):
    count = 0
    for i in arr:
        if i > 1:
            is_prime = True
            for j in range(2,i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count+=1
    print(count)
prime([8, 14, 11, 23, 6])