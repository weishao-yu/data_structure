# PC
T = int(input().strip())  

for _ in range(T):
    try:
        n = int(input().strip()) 
        for _ in range(n):
            print("Hello World")
        if _ < T - 1:
            print() 
    except EOFError:
        break
#strip() 方法用於移除字串頭尾指定的字元（預設為空格或換行符）或字符ß
#因為變數的作用域在 Python 中是基於程式塊（block）的，因此內層和外層的變數名稱可以相同，但是它們是不同的變數，分別存在於各自的程式塊中。
#另外,range的範圍為0~n-1