ch = ord('a')
i = 1
while ch <= ord('z'):
    print(chr(ch), end=" ")
    if i % 8 == 0:
        print()
    ch += 1
    i += 1
