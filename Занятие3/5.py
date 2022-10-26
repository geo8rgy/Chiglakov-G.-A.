def A(x, y, z):
    if y >= x <= z:
        print(x)
    elif x >= y <= z:
        print(y)
    else:
        print(z)
print(A(1, -8, 5))