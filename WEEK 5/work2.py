while True:
    try:
        a = input().strip()
        b = input().strip()

        freq_a = {}
        freq_b = {}

        for char in a:
            freq_a[char] = freq_a.get(char, 0) + 1

        for char in b:
            freq_b[char] = freq_b.get(char, 0) + 1

        common_chars = []
        for char in sorted(freq_a.keys()):
            if char in freq_b:
                common_chars.append(char * min(freq_a[char], freq_b[char]))

        print("".join(common_chars))

    except EOFError:
        break
