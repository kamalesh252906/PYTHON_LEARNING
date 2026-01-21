# def odd_eve(s1,s2):
#     s3 = ""
#     for i in range(0,len(s1)):
#         if i < len(s1):
#             s3 += s1[i]
#         if i < len(s2):
#             s3 = s3 + s2[i]
#     print(s3)
# odd_eve("Abc","Xyz"[::-1])

def year(a):
    for i in range(3,5,+1):
        v = int(a[i])
    if v == 0 or v == 1  or v < 13:
        print("yes")
    else:
        print("No")
year("01/23/2006")