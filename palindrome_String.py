def palindrome(s):
    s.lower()
    p=s[::-1]
    if s==p:
        print("Palindrome!")
    else:
        print("Not Palindrome!")


palindrome(str(input("Enter a string to check for palindrome")))