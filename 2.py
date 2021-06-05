#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':

    def circle(r):
        return r*r*math.pi

    def cylinder(h, r):
        print("Что вы хотите вычислить? (нажмите цифру)\n1. Полная площадь цилиндра\n2. Площадь боковой поверхности "
              "цилиндра")
        ans = int(input())
        if ans == 1:
            print(2*circle(r) + 2*r*h*math.pi)
        elif ans == 2:
            print(2*r*h*math.pi)
        else:
            print("Допустимы цифры 1 или 2.")

    r = int(input("Введите радиус цилиндра: "))
    h = int(input("Введите высоту цилиндра: "))
    cylinder(h, r)