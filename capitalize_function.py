def capitalize_1st_and_4th_letter(s):
    first_3_letters=s[0:3]
    rest=s[3:]
    return first_3_letters.capitalize() + rest.capitalize()
print(capitalize_1st_and_4th_letter(str(input("Enter a String"))))
