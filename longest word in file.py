f=open("data.txt","r")
l=f.read().split(" ")
print(l)
max=l[0]
for i in l:
    if len(l[i])>len(max):
        max=l[i]
print(max)
f.close()