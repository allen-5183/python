def printChar(ch, n):
    for i in range(n):
        print(f'{ch}', end = '')
    print()  # 換行


ch1 = 'A'
n1 = 12

# printChar('A', 12)
printChar(ch1, n1)
printChar('$', 15)
printChar('B', n1+4)