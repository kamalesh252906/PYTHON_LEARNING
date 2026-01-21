def reverse(n):
    #start
    if n >=0 or n <=9:
        return n
    else:
        x = n
        temp = ""
        digits = []
        while x > 0:
            quotient = x // 10 # 134
            remainder =  x % 10 # 2
            digits.append(remainder)
            x = quotient 
        print(digits)
    #stop

reverse(1342)