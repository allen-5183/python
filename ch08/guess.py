from random import randint

pc = set()
while len(pc) < 2:
    pc.add(randint(1,7))

print(f'電腦已經選好號碼了 {pc}，請輸入兩個 1~7 的號碼，總共有三次機會') 



count = 3
while (count):
    you = set()
    while (len(you) < 2):
        x = int(input (f'請輸入第 {len(you) + 1} 個號碼：'))
        if(x <= 7 and x > 0):
            you.add(x)

    if(pc == you):
        print('答對了')
        break

    print('答錯了')
    count = count -1
        