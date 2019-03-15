cardno=input("Enter the card number: ")
def cardvalidation(cno):
    l = len(cno)
    check = 0
    cardname = "Not Identified"
    if (13 <= l <= 16):
        type = cno[0]
        if (type == '4'):
            cardname = "VISA"
            check = 1
        elif (type == '5'):
            cardname = "MASTER CARD"
            check = 1
        elif (type == '3'):
            if (cno[1] == '7'):
                cardname = "AMERICAN EXPRESS"
                check = 1
            else:
                cardname = "Not Identified"
        elif (type == '6'):
            if (cno[1] == '5'):
                if (cno[2] == '2'):
                    if (cno[3] == '1'):
                        cardname = "RUPAY"
                        check = 1
            else:
                cardname = "Not Identified"
        elif (type == '6'):
            cardname = "DISCOVER"
            check = 1

    else:
        print("Invalid Length")

    sum1 = 0
    sum2 = 0
    i = len(cno)
    j = len(cno)

    if (check == 1):
        while (i > 1):
            c = int((cno[i - 2])) * 2
            if (c > 9):
                c = int((c % 10) + (c / 10))
            sum1 = sum1 + c
            if (i > 0):
                i = i - 2

        while (j > 0):
            sum2 = sum2 + int(cno[j - 1])
            j = j - 2

        sum3 = sum1 + sum2
        if (sum3 % 10 == 0):
            print("\nValid {} card".format(cardname))
        else:
            print("\n Invalid card")

    else:
        print("Invalid Details")

cardvalidation(cardno)












