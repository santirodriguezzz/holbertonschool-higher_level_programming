#!/usr/bin/python3
" program that prints the result of the addition of all arguments"
if __name__ == "__main__":
    import sys
    add = 0
    for addend in sys.argv[1:]:
        sum += int(addend)
    print (sum)
