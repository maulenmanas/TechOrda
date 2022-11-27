s = input()
res = 0
for i in s:
    res <<= 1
    res += ord(i) - 48
print(res)