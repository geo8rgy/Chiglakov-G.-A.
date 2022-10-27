def A(n):
    ch = 0
    for i in range(1000):
        kv = ch*ch
        if n>kv:
            print(kv)
        ch+=1
print(A(22))