# PA
while True:
    try:
        name = input()
        if name.isdigit():
            print("Hello World")
    except EOFError:
        break
#想讓測資無限輸入，但是又要有結束的條件，所以用try except來判斷是否有輸入，如果沒有輸入就break
#.isdigit() 判斷是否為數字 (須為string)