def A(x,y):
    den = 0
    for i in range(1,100000):
        x = x*1.1
        den+=1
        if y <= x:
            print(den)
            break
print(A(9,72))