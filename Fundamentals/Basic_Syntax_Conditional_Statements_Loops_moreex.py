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
