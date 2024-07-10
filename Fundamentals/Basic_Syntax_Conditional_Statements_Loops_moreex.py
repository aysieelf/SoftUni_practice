# exercise 1

number_lst = [int(x) for x in input()]
sorted_lst = sorted(number_lst, reverse=True)
print(*sorted_lst, sep='')

# exercise 2

word = input()

indexes_lst = []
for i in range(len(word)):
    if word[i].isupper():
        indexes_lst.append(i)

print(indexes_lst)

# exercise 3

sheep = input().split(", ")
sorted_sheep = sheep[::-1]

if sorted_sheep[0] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(sorted_sheep)):
        if sorted_sheep[i] == 'wolf':
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")

# exercise 4

string = input()
string = string.lower()

count = 0
sand = "sand"
water = "water"
fish = "fish"
sun = "sun"
for i in range(len(string) - len(sun)):
    part = string[i:i + len(sand)]
    if sand == part:
        count += 1
    part = string[i:i+len(water)]
    if water == part:
        count += 1
    part = string[i:i+len(fish)]
    if fish == part:
        count += 1
    part = string[i:i+len(sun)]
    if sun == part:
        count += 1

print(count)