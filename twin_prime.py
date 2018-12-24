import math as m
l=[]
def prime(n):
    c=0
    if n==2:
        return True
    if n<=1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if(n%i==0):
            c=c+1
    if c>0:
        return False
    else:
        return True
for i in range(1,1000):
    if prime(i)==True and prime(i+2)==True:
        l.append(i)
        l.append(i+2)
for i in range(0,len(l),2):
    print("({},{})".format(l[i],l[i+1]))

