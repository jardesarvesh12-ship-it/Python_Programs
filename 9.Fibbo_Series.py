x = 0
y = 1
num = int(input("enter a number :"))


if num == 1:
    print(x)


else:
    print(x)
    print(y)
    for i in range(1, num+1):
        z = x + y
        x = y
        y = z

        print(z)