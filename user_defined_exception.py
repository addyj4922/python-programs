try:
    a=100
    b=a/0
    print(b)
except ZeroDivisionError as z:
    print("Error= ",z)