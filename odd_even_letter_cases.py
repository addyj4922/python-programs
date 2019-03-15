def myfunc(name):
    a=name.lower()
    l=list(a)
    l1=[]
    s=''
    for i in range(0,len(l)):
        if i%2==0:
            b=l[i].upper()
            l1.append(b)
        else:
            l1.append(l[i])
    s=''.join(l1)
    print(s)

myfunc('heLLO worLd')
