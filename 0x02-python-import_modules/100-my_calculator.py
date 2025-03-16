#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add,sub,mul,div
    from sys import argv, exit

operators = ["+", "-", "*", "/"]
functions = [add, sub, mul, div]

if not len(argv) - 1 == 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if not argv[2] in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
# elif argv[2] == operators[0]:
#     print("{} {} {} = {}".format(argv[1], argv[2], argv[3], add(int(argv[1]), int(argv[3]))))


for i in range(len(operators)):
    if argv[2] == operators[i]:
        # print(functions[i])
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], functions[i](int(argv[1]), int(argv[3]))))