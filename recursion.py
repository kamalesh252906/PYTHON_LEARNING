def adds(a):
    if a == 0:
        return "Invalid"
    elif a == 1:
        return 1
    elif a > 1:
        return a+adds(a-1)

print(adds(3))