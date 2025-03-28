# PD
while True:
    try:
        numbers = list(map(int, input().split()))
        total = 1
        for number in numbers:
            total *= number
        for _ in range(total):
            print("Hello World")
        print()
    except EOFError:
        break

#split:string.split(separator, maxsplit) separator:分隔符號(預設是空白)  maxsplit:分割次數(預設無限制)
#map:當只有單個變數時,只會保存map物件本身,不會解包,想查看內容的話要用list()轉換
#map:當有多個變數時,會解包,可以直接使用
#map:map(函數,可迭代物件) 會將可迭代物件的每個元素依序傳入函數中,並將結果以map物件返回
#常見的可迭代物件包含list, tuple, dict, set, str, range, file, generator