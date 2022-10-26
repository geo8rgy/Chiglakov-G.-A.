def A(z, x, c, v):
    if (z+x+c+v) % 2 == 0:
        print("Да")
    else:
        print("Нет")
print(A(7, 1, 4, 9))