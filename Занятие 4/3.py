def F(a, b):
    if a>b:
        for i in range(a, b - 1, -1):
            if i%2==0:
                pass
            else:
                print(i)
    else:
        print("Не по условию")
print(F(20,8))