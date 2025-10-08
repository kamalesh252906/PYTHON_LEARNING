a = int(input("Enter your marks below 100: "))
match a // 10:   
    case 10 | 9 | 8 :  
        print("A")
    case 7 | 6 :       
        print("B")
    case 5 :            
        print("C")
    case 4:           
        print("D")
    case _ if a < 40:
        print("Fail")


a = input('Enter a vowel:')
match a :
    case 'A' | 'a' | 'E' | 'e' | 'I' | 'i' | 'O' | 'o' | 'U' | 'u' :
        print('Vowel')
    case _ :
        print('Constant')


age = int(input('Enter a age:'))
if age > 0 and age < 5 :
    print('Free')
elif age >= 5 and age <= 12 :
    print('10')
elif age >= 13 and age <= 64 :
    print('20')
elif age >= 65 :
    print('15')
else :
    print('Invalid age')


monthNumber = int(input('Enter a number between 1 to 12:'))
match monthNumber :
    case 1 :
        print('January')
    case 2 :
        print('February')
    case 3 :
        print('March')
    case 4 :
        print('April')
    case 5 :
        print('May')
    case 6 :
        print('June')
    case 7 :
        print('July')
    case 8 :
        print('August')
    case 9 :
        print('September')
    case 10 :
        print('October')
    case 11 :
        print('November')
    case 12 :
        print('December')
    case _ :
        print('Invalid input')


