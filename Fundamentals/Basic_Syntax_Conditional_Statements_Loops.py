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

# exercise 3

word = input()
print(word[::-1])

# exercise 4
#
# Write a program that receives a number n on the first line.
# On the following n lines, it receives different integer numbers.
# If the program receives an odd number, print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even.".

n = int(input())

x = False
for _ in range(n):
    num = int(input())
    if num % 2 == 1:
        print(f"{num} is odd!")
        x = True

if not x:
    print("All numbers are even.")

