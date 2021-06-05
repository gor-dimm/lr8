#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def negative():
        print("Число отрицательное.")

    def positive():
        print("Число положительное.")

    def test():
        x = int(input("Введите целое число: "))
        if x > 0:
            positive()
        else:
            negative()

    test()