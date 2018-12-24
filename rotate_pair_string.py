def rotate(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]==l[j][::-1]:
                print(l[i], l[j])

l=["addy","ydda","harry","monu","unom"]
print(rotate(l))
