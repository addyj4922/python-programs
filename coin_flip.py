import random as r
heads=0
tails=0
tries=-1
def coin_flip():
    tails=0
    heads=0
    if r.randint(0,1)==1:
        print("Tails!!")
        tails+=1
    else:
        print("Heads!!")
        heads+=1
    if tails==1:
        d={"tails":1}
    else:
        d={"heads":1}
    return d
while True:
    tries+=1
    flip=str(input("Do you want to flip the coin enter y or n"))
    if flip[0].lower()=='y':
        a=coin_flip()
        if a.get("heads")==1:
            heads+=1
        else:
            tails+=1

    else:
        print("Thank you!")
        print(f"Total no. of tries= {tries}")
        print("Total no. of heads= {} \nTotal no. of tails= {}".format(heads,tails))
        break