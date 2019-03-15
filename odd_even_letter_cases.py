def myfunc(name):
    a=name.lower()
    l=list(a)
    l1=[]
    print(l)
    for i in range(0,len(l)):
        if i%2==0:
            b=l[i].upper()
            l1.append(b)
        else:
            l1.append(l[i])
    print(l1)

myfunc('heLLO worLd')