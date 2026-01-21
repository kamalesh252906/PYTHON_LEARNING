# def fib(nums,position):
#     a,b = 0,1
#     c = []
#     for i in range(0,nums):
#         c.append(a)
#         a,b = b,a+b
#     sum = 0
#     for i in range(0,len(c)):
#         sum+=c[i]
#         if i == position:
#             break
#     return sum
# print(fib(8,4))


def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)
# print(fib_rec(8))


def sum_fib(position):
    if position < 0:
        return 0
    return fib_rec(position) + sum_fib(position-1)

print(sum_fib(4))