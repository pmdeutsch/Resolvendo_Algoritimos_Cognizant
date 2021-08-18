n = int(input())
a = 0
b = 1
lis = [0, 1]
lisx = []
fib_str = []
if n == 1:
    print(lis[0])
elif n > 46:
    quit()
else:
    for i in range(0, n - 2):
        c = a + b
        a = b
        b = c
        lis.append(c)

    for i in lis:
        x = str(i)
        lisx.append(x)
    fib_str = ' '.join(lisx)
    print(fib_str)
