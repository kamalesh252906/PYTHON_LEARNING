a = 'aple'
b = {}

def duplicate(a):
    n = 0

    for i in a:
        if i not in b:
            b[i] = n
            n = n+1
            print(b)
        else:
            return False
    return True


print(duplicate('apple'))