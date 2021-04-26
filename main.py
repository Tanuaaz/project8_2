'''
Данная функция рекурсивно рисует Броуновские острова
'''
from turtle import penup, pendown, goto, speed, mainloop
from random import random
from math import sqrt

def brown (x0,y0,x1,y1, disp, p, n=12, m=400):
     ''' Рекурсивная функция построения Броуновского моста.
     Параметры:
     x0, y0, x1, y1 - координаты двух точек
     disp -дисперсия
     p - плавность
     n - глубина рекурсии
     m - масштаб
     xm, ym - координаты середины
     delta_x - смещение для y
     delta_y - смещение для x
     '''

     if n==0:
          penup()
          goto(x0*m-m/2,y0*m-m/2)
          pendown()
          goto(x1*m-m/2,y1*m-m/2)
          return
     xm = (x0 + x1) / 2.0
     ym = (y0 + y1) / 2.0
     delta_1 = random() * sqrt(disp)
     delta_2 = random() * sqrt(disp)
     brown(x0, y0, xm + delta_2, ym + delta_1, disp / p, p, n - 1)
     brown(xm + delta_2, ym + delta_1, x1, y1, disp / p, p, n - 1)
     speed("fastest")

def main():
     speed("fastest")
     h=float(input())
     a = 2.0**(2.0*h)
     brown(0, 0, 0, 0, 0.5, a)
     mainloop()

if __name__ == '__main__':
    main()
