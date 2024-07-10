# exercise 1

n = float(input())
part1 = ''
part2 = ''

if n == 0:
    part2 = "zero"
elif n!= 0:
    if 0 < abs(n) < 1:
        part1 = 'small'
    elif abs(n) > 1000000:
        part1 = 'large'

    if n > 0:
        part2 = "positive"
    elif n < 0:
        part2 = "negative"

if len(part1) > 0:
    print(f"{part1} {part2}")
else:
    print(part2)

# exercise 2

n1, n2, n3 = int(input()), int(input()), int(input())

print(max(n1, n2, n3))

# exercise 3

word = input()
print(word[::-1])

# exercise 4

n = int(input())
x = False
for _ in range(n):
    num = int(input())
    if num % 2 == 1:
        print(f"{num} is odd!")
        x = True
        break

if not x:
    print("All numbers are even.")

# exercise 5

num = 0

while num < 1 or num > 100:
    num = float(input())

print(f"The number {num} is between 1 and 100")

# exercise 6

budget = float(input())
spend = 0
while True:
    price = input()
    if price == "End":
        print("You bought everything needed.")
        break

    spend += float(price)

    if spend > budget:
        print("You went in overdraft!")
        break

# exercise 7

n = int(input())

for i in range(1, n+1):
    print('*'*i)

for ii in range(n-1, 0, -1):
    print('*'*ii)
