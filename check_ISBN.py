isbn=str(input("enter your isbn no"))
l=[]
for i in range (0,len(isbn)):
    l.append(int(isbn[i])
checksum=10-( l[0]+(3*l[1])+l[2]+(3*l[3])+l[4]+(3*l[5])+l[6]+(3*l[7])+l[8]+(3*l[9])+l[10]+(3*l[11]))%10
if checksum==10:
    checksum=0
l.append(checksum)
for i in range(0,len(l)):
    print(l[i],end="")
