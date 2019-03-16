def makes_twenty(a,b):
    if a==20 or b==20 or (a+b)==20:
        return True
    else:
        return False
print(makes_twenty(int(input("Enter 1st no.")),(int(input("Enter 1st no.")))))
