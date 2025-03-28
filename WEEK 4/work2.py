def value(x):
    units = ["kuti", "lakh", "hajar", "shata"]
    values = [10000000, 100000, 1000, 100]

    def convert_to_bangla(num):
        if num == 0:
            return ""

        result = []
        for unit, value in zip(units, values):
            if num >= value:
                result.append(f"{num // value} {unit}")
                num %= value
        if num > 0:
            result.append(str(num))
        return ' '.join(result)

    def convert_recursive(num):
        if num == 0:
            return "0"

        parts = []
        kuti_part = num // 10000000
        remainder = num % 10000000

        if kuti_part > 0:
            parts.append(f"{convert_recursive(kuti_part)} kuti")

        if remainder > 0:
            parts.append(convert_to_bangla(remainder))

        return ' '.join(parts).strip()

    return convert_recursive(x)


case_number = 1
while True:
    try:
        x = input().strip()
        if not x:
            continue  

        number = int(x)
        bangla_text = value(number)
        print(f"{case_number:4d}. {bangla_text}")
        case_number += 1
    except EOFError:
        break  

#zip() function is used to combine two lists. It takes two lists and returns an iterator of tuples.
