def F(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)
print(F(9,2))