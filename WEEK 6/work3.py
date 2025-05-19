words = set()  # 用來儲存不同的單字

while True:
    try:
        line = input()
        word = ''
        for c in line:
            if c.isalpha():  # 如果是英文字母
                word += c.lower()
            else:
                if word:
                    words.add(word)
                    word = ''
        if word:  # 處理行尾的單字
            words.add(word)
    except EOFError:
        break

for w in sorted(words):
    print(w)
