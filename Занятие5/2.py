def A(n):
    if n >=2:
        for i in range(1,100000000000):
            if (n%i==0) and (i!=1):
                print(i)
                break
print(A(7))