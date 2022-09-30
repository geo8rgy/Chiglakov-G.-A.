m=int(input())

if (m < 1440):
    s=m*60
    h=s / 3600 % 24
    m1=s / 60 % 60 / 10
    m2=s / 60 % 60 % 10
    print(h, " ", m1, m2)
else:
    print("Умер от кринжа")
    
