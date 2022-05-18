def create(m, n):
    if m == "Max":
        return lambda v: v < n
    elif m == "Min":
        return lambda v: v > n

max = create("Max", 31)

print(max(15))
print(max(32))