s = input("enter Price1 and Weight1").split(" ")
s1 = input("enter Price2 and Weight2").split(" ")
print(s, s1)
if (float(s[0])/float(s[1])) < (float(s1[0])/float(s1[1])):
    print("pack 1")
else:
    print("pack 2")
