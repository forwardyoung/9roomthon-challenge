N = int(input())
T, M = map(int, input().split())

for _ in range(N):
	i = int(input())
	M += i
if T + M //60 < 24:
	print(T + M // 60, M % 60)
else:
	if (T + M //60) % 24 == 0:
		print(0, M % 60)
	else:
		print((T + M //60) % 24, M % 60)