def judge(n):
    if len(n) <= 3:
        return n
    else:
        units = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        length = len(n)
        level = (length - 1) // 3  # 計算等級（從 1 開始）
        unit_index = level - 1    # 將等級轉換為單位字母的索引（從 0 開始）
        if unit_index >= len(units):
            return "Number too large"
        unit_value = n[:length % 3 or 3]
        return f"{unit_value}{units[unit_index]}"

while True:
    try:
        n = input()
        result = judge(n)
        print(result)
    except EOFError:   
        break