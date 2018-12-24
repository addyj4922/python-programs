import math as m
area=0
n=int(input("enter the no of sides"))
s=int(input("enter lenght"))
area = (n*s*s)/(4*m.tan(3.14/n))
print(area)
