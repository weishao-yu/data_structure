T = int(input())
country_count = {}
for _ in range(T):
    line = input()
    part = line.split()
    country = part[0]


    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

for countrty in sorted(country_count.keys()):
    print(f"{countrty} {country_count[countrty]}")