import math  # 匯入 math 模組，提供 π、e、log、ceil 等數學函式與常數。
print(f"圓周率 π：{math.pi}")  # 輸出圓周率 pi（約 3.14159），示範如何讀取 math 常數。
print(f"自然對數 e：{math.e}")  # 輸出自然常數 e（約 2.71828），常用於成長/衰減與自然對數計算。
states = 1000  # 設定總狀態數為 1000，代表系統可能出現的不同情況數量。
print(math.log(states, 2))  # 計算 log2(1000)：用 2 為底的對數，表示理論上需要多少「二進位位元」來區分 1000 種狀態。
bits_needed = math.ceil(math.log(states, 2))  # 將 log2(1000) 無條件進位成整數，因為位元數必須是整數且要足夠容納所有狀態。
print(f"儲存 {states} 種狀態需要 {bits_needed} 個位元")  # 輸出結論：儲存 1000 種狀態至少需要幾個 bit。
