def blackjack(a,b,c):
    s=a+b+c
    if s<=21:
        return s
    elif s<=31 and (a==11 or b==11 or c==11):
        return (s-10)
    else:
        return 'BUST'
print(blackjack(9,9,9))