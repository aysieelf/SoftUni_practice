# exercise 1

n = float(input())
part1 = ''
part2 = ''
if n == 0:
    part2 = "zero"
elif n > 0:
    part2 = "positive"
else:
    part2 = "negative"

if abs(n) < 1:
    part1 = 'small'
elif abs(n) > 1000000:
    part1 = 'large'

if len(part1) > 0:
    print(f"{part1} {part2}")
else:
    print(part2)

# exercise 2

n1, n2, n3 = int(input()), int(input()), int(input())

print(max(n1, n2, n3))

#