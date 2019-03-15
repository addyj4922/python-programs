import time
import math
def prime(n):
    n1=str(n)
    n2=n1[::-1]
    if(n1==n2):
        c=0
        a=int(math.sqrt(n))
        for i in range(2,a+1):
            if(n%i==0):
                return False
            else:
                return True

start=time.time()
num=1
l=int(input("Enter limit: "))
while(num<=l):
    if(prime(num)==True):
        print(num)
    num=num+1
print("Sorting time: {} sec".format(time.time()-start))
