def Bin(m):
    if m == 0:
        return "0", 0
    res = ""
    parity = 0
    while m > 0:
        bit = m % 2
        res = str(bit) + res
        if bit == 1:
            parity += 1
        m = m // 2
    return res, parity



while True:
    m = int(input())
    if m == 0:
        break
    res, sum = Bin(m)
    print (f"The parity of {res} is {sum} (mod 2).")
