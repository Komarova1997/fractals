'''
Developers:
Komarova E.
Baidalakova B.
'''

from turtle import *


def eazy_fractal(size, n):
    '''Первый фрактал - упражнение'''
    if n == 0:
        return
    turtle.right(20)
    turtle.up()
    turtle.forward(size/4)
    turtle.down()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    return eazy_fractal(size * 0.9, n - 1)


def bintree(height, angle):
    '''Построение двоичного дерева: параметры - высота и угол'''
    if angle == 0:
        return
    forward(height)
    right(45)
    m(0.9*height,angle-1)
    left(90)
    m(0.9*height,angle-1)
    right(45)
    bk(height)


def branch():
    '''Ветка'''


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)


# Для функции koch
'''def main():
    up()
    goto(-100,0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)

main()'''


def ice_koch():
    '''Снежинка Коха'''


def minkowski():
    '''Кривая Миновского'''


def ice_fractal_1():
    '''Ледаяной фрактал 1'''


def ice_fractal_2():
    '''Ледаяной фрактал 2'''


def levi():
    '''Кривая Леви'''


def dragon():
    '''Фрактал Дракон Хартера-Хейтуэя'''
