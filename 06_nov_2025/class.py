# def zeros(a):
#     if a.count(0) < 2: 
#         print(-1); return
#     s = a.index(0)
#     e = a.index(0, s + 1)
#     b = []
#     for i in range(s + 1, e):
#         b.append(a[i])
#     print(b)
# zeros([10,0,9,8,7,0,3,4,5])


# def brace(a):
#     count = 0
#     for i in a:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -=1
#     if count < 0:
#         print(False)
#     else:
#         print(True)
# brace("(())")


# class Orders:
#     def __init__(self):
#         self.cart = []

#     # add items
#     def add_item(self, id, product_name, qty, price):
#         # write your code here
#         current_item = {
#             "id": id,
#             "product_name": product_name,
#             "qty": qty,
#             "price": price,
#         }
#         self.cart.append(current_item)

#     def remove_item(self, id):
#         # write your code here
#         idx = None

#         for i in range(0, len(self.cart), +1):
#             if self.cart[i]["id"] == id:
#                 idx = i

#         del self.cart[idx]
#         print("\nItem deleted successfully\n")

#     def find_total_bill(self):
#         # write your code here
#         total = -0
#         for el in self.cart:
#             total += el["price"] * el["qty"]
#         print(total)
        

#     def view_bill(self):
#         print(self.cart)


# print("\nfirst user")
# narayanan = Orders()
# narayanan.add_item(id=1, product_name="samosa", price=20, qty=10)
# narayanan.add_item(id=2, product_name="tea", price=10, qty=3)
# # narayanan.view_bill()
# # narayanan.remove_item(1)
# # narayanan.view_bill()
# narayanan.find_total_bill()


# print("\nSecond user")
# # alice
# # alice = Orders()
# # alice.add_item(id=1, product_name="greetings", price=100, qty=1)
# # alice.view_bill()
# # Collapse



# def chars(a):
#     max = 0
#     max_char = ''
#     for i in a:
#         if a.count(i) > max:
#             max = a.count(i)
#             max_char = i
#     print(max,max_char)
# chars("success")
# chars("python")
# chars("mississppi")


# def short(a):
#     b = a[0]
#     for i in range(0,len(a),+1):
#         if a[i] == " ":
#             b += a[i+1]
#     print(b.upper())
# short("united states america")

# def pos(a):
#     counts = 0
#     char = ""
#     for i in a:
#         if a.count(i) > counts:
#             counts = a.count(i)
#             char = i
#             print(char , counts)
# pos("apple")

# def maxi(a):
#     b = a.split(" ")
#     sum = 0
#     chars = ''
#     for i in b:
#         if b.count(i) > sum:
#             sum = b.count(i)
#             chars = i
#             print(chars,"=",sum)
# maxi("apple mango apple orange mango apple")

# def is_count(sen):
#     for i in sen:
#         count = 0
#         for j in sen:
#             if i == j :
#                 count += 1
#     print(set((i, "->",count)))

# is_count("Banana")


# def first(a):
#     b = a[0]
#     for i in range(1,len(a)):
#         if a[i] == " ":
#             b = b + a[i+1]
#     print(b.upper())
# first("united states america")

# def sent(a):
#     b = a.title()
#     c = ""
#     for i in b:
#         if i not in " ":
#             c += i
#     print(c)
# sent('welcome to python')


# def sent(a):
#     flog = None
#     b = ""+a[0].upper()
#     for i in range(0,len(a)):
#         flog = i+1
#         if a[i-1] == " ":
#             b = b + a[flog].upper()
#         elif i != " ":
#             b = b + a[i]
#     print(b)
# sent('welcome to python')

def parent(a):
    count = 0
    for i in a:
        if i == "(":
            count += 1
        elif i == ")":
            count -=1
            if count == -1:
                print(False)
                break
    if count == 0:
        print(True)
parent("())(")
# parent("()()")

# def counts(a):
#     for i in a:
#         count = 0
#         for j in i:
#             count += 1
#         print(a , count)
# counts(['kamal','yash'])


# def reve(a):
#     rev = ""
#     for i in a:
#         rev = i + rev
#     print(rev)
#     if rev == a:
#         print('T')
#     else:
#         print('F')
# reve("level")
# reve("def")
# reve("malayalam")



# def counts(a):
#     count = 1
#     for i in a:
#         if i == " ":
#             count+=1
#     print(count)
# counts("pyhton la ushaar")    









        















