def summer_of_69(l):
    add=True
    s=0
    for i in l:
        while add:
            if i!=6:
                s+=i
                break
            else:
                add=False
        while not add:
            if i != 9:
                break
            else:
                add=True
    return s

print(summer_of_69([1,2,3,4,5,6,7,8,9,10]))