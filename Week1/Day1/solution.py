import math

W, R = map(int, input().split())
RM = W * (1 + R/30)
print(math.trunc(RM))