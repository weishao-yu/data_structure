while True:
    try:
        N, R = map(int, input().split())
        returned = list(map(int, input().split()))
        if N == R:
            print("*")
        else:
            not_returned = []
            for i in range(1, N+1):
                if i not in returned:
                    not_returned.append(i)
            not_returned.sort()
            
            result = " ".join(map(str,not_returned))
            print(result)
    except EOFError:
        break
            
