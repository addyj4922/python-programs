def is_anagram(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    c=0
    for i in range(0,len(s1)):
        if(s2[i] in s1):
            c=c+1
    if c==len(s1):
        return True
    else:
        return False
print(is_anagram("Listen","Silent"))
