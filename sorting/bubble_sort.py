def bubble_sort(a):
    if len(a) == 0:
        print("Invalid")
    else:
        swap = True
        while swap:
            swap = False
            for i in range(0,len(a)-1,+1):
                if a[i] > a[i+1]:
                    temp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = temp
                    swap = True
        print(a)
bubble_sort([10,40,30,20,60,80])