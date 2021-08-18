n = int(input())
if n < 0:
    quit()
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)