N = int(input())
persons = input().split()

lowest_pos = 0
for i in range(N):
    if i == 0:
        lowest = persons[i]
        if persons[i] < lowest:
            lowest = persons[i]
            lowest_pos = i
    elif persons[i] < lowest:
        lowest = persons[i]
        lowest_pos = i
print(lowest_pos + 1)
