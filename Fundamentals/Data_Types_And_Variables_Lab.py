# 1 Concat Names

name1 = input()
name2 = input()
delimiter = input()
print(f"{name1}{delimiter}{name2}")


# 2 convert meters to kilometers

meters_dist = int(input())
kilometers_dist = meters_dist / 1000
print(f"{kilometers_dist:.2f}")

# 3 pounds to dollars

pounds = int(input())
dollars = pounds * 1.31
print(f"{dollars:.3f}")

# 4 centuries to minutes

centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

# 5 special numbers

n = int(input())

for num in range(1, n+1):
    x = False
    ttl = 0
    for digit in str(num):
        ttl += int(digit)
    if ttl == 5 or ttl == 7 or ttl == 11:
        x = True
    print(f"{num} -> {x}")

# 6 happy year

year = int(input())
while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        print(year)
        break
