lst4 = [11, 22, 33, 44, 55, 66, 77, 88, 99]      
for i in range(len(lst4)):    # len(lst4) = 9
   print(lst4[i], end = ' ')  # 印出 11 22 33 44 55 66 77 88 99
print()
for j in range(1, 4):
   print(lst4[j], end = ' ')  # 印出 22 33 44
print()
for k in range(5, len(lst4)):
   print(lst4[k], end = ' ')  # 印出 66 77 88 99
print()
for m in range(len(lst4)-1, 5-1, -1):
   print(lst4[m], end = ' ')  # 印出 99 88 77 66
print()
for g in range(0, len(lst4), 2):
   print(lst4[g], end = ' ')  # 印出 11 33 55 77 99