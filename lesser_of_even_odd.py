def lesser_of_even_odd(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_even_odd(int(input("enter 1st no.")),int(input("enter 2nd no."))))