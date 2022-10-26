def A(n, m, k):
    if (n*m>=k) and ((k % n == 0) or k % m == 0):
        print("Да")
    else:
        print("Нет")
print(A(2, 4, 2))