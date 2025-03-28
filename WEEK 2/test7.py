while True:
    try:
        # 讀取 n，若 n 不是數字則跳過
        n = input().strip()
        if not n.isdigit():
            continue
        n = int(n)

        letter_count = {}

        # 讀取 n 行文字
        for _ in range(n):
            line = input().strip()

            for char in line:
                if char.isalpha():  # 只處理英文字母
                    char = char.upper()  # 統一轉成大寫
                    letter_count[char] = letter_count.get(char, 0) + 1

        # 定義排序函數
        def sort_key(item):
            char, count = item
            return (-count, char)  # 次數降序，字母升序

        # 排序: 先依次數降序，再依字母升序
        sorted_letters = sorted(letter_count.items(), key=sort_key)

        # 輸出結果
        for letter, count in sorted_letters:
            print(letter, count)

        for i in range(n - 1):
            print()

    except EOFError:
        break  # 讀到檔案結尾 (EOF) 就停止
