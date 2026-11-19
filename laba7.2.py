# -*- coding: cp1251 -*-
import turtle as tr
from random import uniform
from math import sqrt

def in_region(x, y):
    """Проверка попадания точки в заштрихованную область"""
    if (x >= abs(y)) and (y >= (x - 2)**2 - 3):
        return True
    return False

def draw_axes(x_min, x_max, y_min, y_max):
    """Рисование осей координат"""
    tr.color("black")
    tr.width(1)
    
    # Ось X
    tr.up()
    tr.goto(x_min, 0)
    tr.down()
    tr.goto(x_max, 0)
    tr.up()
    tr.goto(x_max, 0)
    tr.down()
    tr.goto(x_max - 0.3, 0.15)
    tr.up()
    tr.goto(x_max, 0)
    tr.down()
    tr.goto(x_max - 0.3, -0.15)
    tr.up()
    tr.goto(x_max + 0.2, -0.4)
    tr.write("X", font=("Arial", 12, "bold"))
    
    # Ось Y
    tr.up()
    tr.goto(0, y_min)
    tr.down()
    tr.goto(0, y_max)
    tr.up()
    tr.goto(0, y_max)
    tr.down()
    tr.goto(0.15, y_max - 0.3)
    tr.up()
    tr.goto(0, y_max)
    tr.down()
    tr.goto(-0.15, y_max - 0.3)
    tr.up()
    tr.goto(0.3, y_max + 0.1)
    tr.write("Y", font=("Arial", 12, "bold"))
    
    # Деления
    for x in range(int(x_min), int(x_max) + 1):
        if x != 0:
            tr.up()
            tr.goto(x, 0)
            tr.down()
            tr.goto(x, -0.15)
            tr.up()
            tr.goto(x, -0.5)
            tr.write(str(x), align="center", font=("Arial", 9))
    
    for y in range(int(y_min), int(y_max) + 1):
        if y != 0:
            tr.up()
            tr.goto(0, y)
            tr.down()
            tr.goto(-0.15, y)
            tr.up()
            tr.goto(-0.5, y)
            tr.write(str(y), align="right", font=("Arial", 9))

def main():
    # Описывающий прямоугольник
    x_min, x_max = -1, 6
    y_min, y_max = -4, 6
    
    N = 10000  # Число испытаний
    
    # Настройка окна
    Dx = 700
    Dy = 700
    tr.setup(Dx, Dy)
    tr.reset()
    tr.tracer(0, 0)
    tr.setworldcoordinates(x_min - 0.3, y_min - 0.3, x_max + 0.3, y_max + 0.3)
    tr.title("ЛР7 Задание 2 - Метод Монте-Карло (Вариант 20)")
    tr.ht()
    
    # Рисуем оси
    draw_axes(x_min, x_max, y_min, y_max)
    
    # Генерация точек
    tr.width(2)
    N_in = 0  # Число попавших точек
    
    for n in range(N):
        x = uniform(x_min, x_max)
        y = uniform(y_min, y_max)
        
        if in_region(x, y):
            tr.up()
            tr.goto(x, y)
            tr.dot(3, "green")
            N_in += 1
        else:
            tr.up()
            tr.goto(x, y)
            tr.dot(2, "red")
    
    # Площадь описывающего прямоугольника
    S_rect = (x_max - x_min) * (y_max - y_min)
    
    # Площадь по методу Монте-Карло
    S_mc = S_rect * N_in / N
    
    # Точная площадь
    S_exact = 7 * sqrt(21) / 2 + 5 * sqrt(5) / 6
    
    # Относительная погрешность
    error = abs(S_mc - S_exact) / S_exact * 100
    
    # Вывод результатов на экран
    tr.up()
    tr.goto(0.5, y_max - 1.5)
    msg = (f"N = {N}\n"
           f"N_pop = {N_in}\n"
           f"S_mc = {S_mc:.4f}\n"
           f"S_exact = {S_exact:.4f}\n"
           f"Error = {error:.2f}%")
    tr.write(msg, font=("Arial", 11, "bold"))
    
    tr.update()
    
    print(f"Число испытаний: {N}")
    print(f"Попало в область: {N_in}")
    print(f"Площадь (Монте-Карло): {S_mc:.4f}")
    print(f"Площадь (точная): {S_exact:.4f}")
    print(f"Погрешность: {error:.2f}%")
    
    tr.mainloop()

if __name__ == "__main__":
    main()