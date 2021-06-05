#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getInput():
    return input()


def testInput(a):
    try:
        val = int(a)
    except ValueError:
        return False
    return True


def strToInt(a):
    return int(a)


def printInt(a):
    print(a)


if __name__ == '__main__':
    a = getInput()
    isIntable = testInput(a)
    if isIntable:
        printInt(strToInt(a))
    else:
        print("Значение не может быть преобразовано к целому числу.")
