def spy_game(l):
    code=[0,0,7,'x']
    for i in l:
        if i==code[0]:
            code.pop(0)
    return len(code)==1

print(spy_game([1,0,0,3,7]))