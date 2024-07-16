# # 1 exchange integers
#
# a = int(input())
# b = int(input())
#
# print(f"""Before:
# a = {a}
# b = {b}""")
#
# a, b = b, a
#
# print(f"""After:
# a = {a}
# b = {b}""")
#
#
# # 2 prime number checker
#
# def is_prime(n):
#     if n > 1:
#         for i in range(2, (n // 2) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     return False
#
#
# print(is_prime(int(input())))
#
# # 3 decrypting
#
# key = int(input())
# n = int(input())
# output = ''
# for _ in range(n):
#     letter = input()
#     new_letter = chr(ord(letter) + key)
#     output += new_letter
#
# print(output)

# 4 balanced brackets

n = int(input())
balance = 0
x = True

prev = input()
if prev == '(':
    balance += 1
elif prev == ')':
    x = False


for _ in range(n-1):
    el = input()
    if el == prev:
        x = False
        break
    if el == '(':
        balance += 1
    elif el == ')':
        balance -= 1
    prev = el

if balance != 0 or not x:
    print("UNBALANCED")
else:
    print("BALANCED")