#!/usr/bin/python3
import sys
from calculator_1 import *


if len(sys.argv) != 4:
    print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
    exit(1)

my_lib = {}
my_lib['+'] = add(int(sys.argv[1]), int(sys.argv[3]))
my_lib['-'] = sub(int(sys.argv[1]), int(sys.argv[3]))
my_lib[r"'*'"] = mul(int(sys.argv[1]), int(sys.argv[3]))
my_lib[r"\*"] = mul(int(sys.argv[1]), int(sys.argv[3]))
my_lib["*"] = mul(int(sys.argv[1]), int(sys.argv[3]))
my_lib['/'] = div(int(sys.argv[1]), int(sys.argv[3]))

if sys.argv[2] not in my_lib.keys():
    print("{}".format("Unknown operator. Available operators: +, -, * and /"))
    exit(1)
else:
    print("{first} {operator} {second} = {result}".format(
        first=sys.argv[1], second=sys.argv[3], operator=sys.argv[2],
        result=my_lib[sys.argv[2]]))
