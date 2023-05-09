#!/usr/bin/python3

for i in range(10):
    for j in range(i, 10):
        if i == j or (i == 8 and j == 9):
            continue
        print("{first}{sec}, ".format(first=i, sec=j, end=''), end='')
print(89)
