#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    if len(sys.argv) - 1 == 1:
        print("{}".format("1 argument."))
        print("{index}: {param}".format(index=1, param=sys.argv[1]))
    elif len(sys.argv) - 1 == 0:
        print("{}".format("0 arguments."))

    if len(sys.argv) - 1 > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{index}: {param}".format(index=i, param=sys.argv[i]))
