#! /usr/bin/python3


def callee(arg1):
    print(arg1)


def caller():
    callee("hello")


if __name__ == "__main__":
    caller()
