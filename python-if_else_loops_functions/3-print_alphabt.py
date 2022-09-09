#!/usr/bin/python3
char = "{:c}"
for i in range(97, 123):
    if i == 101:
        continue
    elif i == 113:
        continue
    else:
        print(char.format(i), end="")
