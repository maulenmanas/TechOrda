a = int(input())
res = a * 45
res += (a // 2) * 5
a = a - 1
res += (a // 2) * 15
print(9 + res // 60, res % 60)