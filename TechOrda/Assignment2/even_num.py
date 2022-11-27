a = int(input())
b = int(input())
res = [x for x in range(a, b + 1) if x % 2 == 0]
print(' '.join(map(str, res)))