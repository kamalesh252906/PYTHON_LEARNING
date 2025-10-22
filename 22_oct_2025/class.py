def sentence(a):
    sentence = (a.split('-'))
    for i in sentence:
        print(i)
sentence('kamalesh-secb-fssa-2025')

def sentence(a):
    for i in a:
        if i != '-':
            print(i,end='')
sentence('kamal-secb-fssa')
            


def sentence(a):
    word = ""
    for i in a:
        if i != '-':
            word += i
        else:                  
            print(word)
            word = ""           
    print(word)
sentence('kamal-fssa-secb')


# 2.

def reverse(a):
    b = a[::-1]
    print(b)
reverse('python')



def reverse(a):
    rev = ''
    for i in a:
        rev = i+rev
    print(rev)
reverse('python')


# 3.

def words(a):
    count = 0
    for i in a:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i !='u' and i != 'A' and i != 'E' and i != ' ' and i !='I' and i != 'O' and i !='U':
            count += 1
    print(count)
words('Hello World')


# 4.

def sentence(a):
    b = ""
    for i in a:
        if i != ' ':
            b = b+i
    print(b)
sentence('kamal esh sec b f s s a')


def sentence(a):
    sentence = (a.split(' '))
    for i in sentence:
        print(i,end='')
sentence('kamalesh secb fssa 2025')


# 5.

def password():
    password = input('Enter your password:')
    if len(password) >=8:
        for i in password:
            if i == '!' or i =='@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*':
                return 'password is strong'
        else:
            return 'password is not strong'
    else:
        return 'Please enter atleast 8 characters'
print(password())

def password(a):
    special ='!@#$%^&*'
    if special in a:
        print('pass strong')
    else:
        print('Not strong')
password('kama!@#$%^&*')


