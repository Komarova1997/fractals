'''
Developers:
Komarova E.
Baidalakova B.
'''

from turtle import *


def eazy_fractal():
    '''Первый фрактал - упражнение'''


def bintree():
    '''Построение двоичного дерева'''


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
    
    
