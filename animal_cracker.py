def animal_crack(a):
    wordlist=a.lower().split()
    return wordlist[0][0]==wordlist[1][0]
print(animal_crack(str(input("Enter a 2 word string"))
