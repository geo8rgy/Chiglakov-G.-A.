x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print(3)
elif x == y or y == z or x == z:
    print(2)
else:
    print(0)