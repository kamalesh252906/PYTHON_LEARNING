# def ratings(a):
#     sum = 0
#     for i in a:
#         if i == 5:
#             sum = sum+1
#     print(sum)
        
# ratings([5,3,4,5,2,5])
# ratings([])

# def lists(a,b):
#     if len(a) == 0:
#         print('empty list')
#     else :
#         for a in b:
#             return'available'
#         return
            
                
        
        
# lists(['asha','vikram','Ravi'],'Ravi')

# def lists(a,b):
#     if b in a:
#         print('available')
#     else:
#         print('Not available')
# lists(['asha','vikram','Ravi'],'Ravi')


# def check(a,b):
#     if b in a:
#         print('Found')
#     else:
#         print('Not Found')
# check([12,23,45,6,7],7)
# check([12,35,25,29],90)

# def check_even(a):
#     sum = 0
#     for i in a:
#         sum += i
#     if sum % 2 == 0:
#         print('even')
#     else:
#         print('odd')
# check_even([20,3])
# check_even([12,100])
    

# def between(a,b,c):
#     for i in c:
#         if a < i and b > i:
#             print(i)
# between(10,30,[11,12,13,20,23,90])

# def find(b):
#     mini = min(b)
#     maxi = max(b)
#     print(mini)
#     print(maxi)
# find([12,35,98,100,1000])


userdata = {'name':'kamalesh','skills':['HTML','CSS','JS'],'age':19,'gender':'male','status':True,
'comments':{'kamlesh':'lower upper','hari':'sower power'}}
userdata['email'] = 'cherrykamalesh@gmail.com'
# # print(userdata)
# # kia = userdata.keys()
# # print(list(kia))
# # print(kia)
# mic = userdata.values()
# print(list(mic))



# def days(n):
#     print(n)
# day = {}
# days = {
#     '1':'monday','2':'tuesday','3':'wednesday','4':'thursday','5':'friday','6':'saturday','7':'sunday'
# }
# for k, v in days.items():
#     print(k, "→", v)

# Dictionary of days without quotes for keys
# days = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }

# # Function to get day name from number
# def get_day_name(day_number):
#     if day_number in days:
#         print(days[day_number])
#     else:
#         print("Invalid day number! Please enter 1 to 7.")

# # User input
# get_day_name(7)

# def sums(a,b):
#     hari = 0
#     if type == str or type == bool:
#         print('Invalid input')
#     else :
#         for i in a:
#             if i > b:
#                 hari += i
#     print(hari)
# sums([1,2,3,4,5],2)

# def odd(a):
#     for i in a:
#         if i % 2 != 0:
#             print(i)
# odd([1,2,4,56,67,23,])



def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    print(a)



