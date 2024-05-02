target = int(input())
even_sum = 0
for n in range(0, target + 1, 2):
    even_sum += n
print(even_sum)
