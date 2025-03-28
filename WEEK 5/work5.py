while True:
    try:
        n = int(input())
        if n <= 1:
            print("Not prime")
        else:
            for i in range(2, int(n**0.5) + 1):  # 检查是否有因数
                if n % i == 0:
                    print("Not prime")  # 有因数，说明是合数
                    break
            else:
                print("prime")  # 没有因数，说明是素数
    except EOFError:
        break
