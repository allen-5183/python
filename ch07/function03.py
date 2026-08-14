def progress(a1, d, n):
    an = a1 + (n - 1) * d
    sn = n * (a1 + an) / 2
    return an, sn

a1 = eval(input("請輸入首項 a1: "))
d = eval(input("請輸入公差 d: "))
an = eval(input('輸入數列的項數：'))

an, sn = progress(a1, d, an)

print(f'等差數列的末項為 {an}，和為 {sn}', end = '')