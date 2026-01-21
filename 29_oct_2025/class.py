class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(self.name + " deposited " + str(amount) + ". New balance: " + str(self.balance))
        print(f"{self.name} deposited: {amount} New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            # print(self.name + "Not enough balance to withdraw " + str(amount))
            print(f"{self.name} Not enough balance to transfer {amount}")
        else:
            self.balance -= amount
            # print(self.name + " withdraw " + str(amount) + ". New balance: " + str(self.balance))
            print(f"{self.name} withdraw: {amount} New balance: {self.balance}")

    def show_balance(self):
        # print(self.name + "current balance: " + str(self.balance))
        print(f"{self.name} current balance: {self.balance}")

    def transfer(self, amount, to_account):
        if amount > self.balance:
            # print(self.name + " Not enough balance to transfer " + str(amount))
            print(f"{self.name} Not enough balance to transfer {amount}")
        else:
            self.balance -= amount
            to_account.balance += amount
            # print("Transferred " + str(amount) + " from " + self.name + " to " + to_account.name)
            print(f"Transferred {amount} from: {self.name} to: {to_account.name} ")



# ac1 = BankAccount("Kamalesh", 2000)
# ac2 = BankAccount("Hari", 1000)


# ac1.deposit(1000)
# ac1.withdraw(4000)
# ac1.show_balance()
# ac1.transfer(1000,ac2)
# ac1.show_balance()

# class LibraryBook:
#     def __init__(self, title, author,available_copies):
#         self.title = title
#         self.author = author
#         self.available_copies = available_copies
#     def borrow_book(self,borrow):
#         if borrow > self.available_copies:
#             print(f"Book not available! I have only:{self.available_copies} copies")
#         else:
#             self.available_copies -= borrow
#             print(f"title: {self.title} name: {self.author} borrow: {borrow} total: {self.available_copies}")
#     def return_book(self,returns):
#         self.available_copies += returns
#         print(f"title: {self.title} name: {self.author} returns: {returns} total: {self.available_copies}")
#     def show_status(self):
#         print(f"title: {self.title} author: {self.author} available_copies: {self.available_copies}")
# bb1 = LibraryBook('three friends','kamalesh',90)
# bb2 = LibraryBook('Tiger' , 'yashika' , 40)
# bb1.borrow_book(10)
# bb1.return_book(0)
# bb1.show_status()

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self):
#         add = self.a + self.b
#         print(add)
#     def subtraction(self):
#         sub = self.a - self.b
#         print(sub)
#     def multiplication(self):
#         multiply = self.a * self.b
#         print(multiply)
#     def division(self):
#         try :
#             div = self.a / self.b
#             print(div)
#         except:
#             print('Error occurred')
# v = Calculator(0,0)
# v.division()



# class Factory:
#     def __init__(self):
#         pass

#     def make_vehicle(self):
#         print("I am making a general vehicle")


# def words(a):
#     b = a[0]
#     for i in range(1,len(a),+1):
#         if a[i] == " ":
#             b += a[i+1]
#     print(b)
# words('National Aero SDat Arial')


# def sentence(a):
#     b = ("1234567890")
#     c =[]
#     for i in a:
#         if i in b:
#             c.append(i)
#     print(c)            
# sentence('py11hon 09 bus67')


# def words(a):
#     b = ""
#     for i in a:
#         if i == " ":
#             b += '-'
#         else:
#             b += i
#     print(b)
# words('Learning python is good')


































