# -*- coding: cp1251 -*-
from math import sqrt
import turtle as tr

def MyFun(x):
    """Функция из ЛР2 Задание 1 вариант 20"""
    if x <= 0:
        y = -x / 2
    elif x > 0 and x <= 2:
        y = 2 - sqrt(4 - x**2)
    elif x > 2 and x <= 4:
        y = sqrt(4 - (x - 2)**2)
    else:
        y = -x / 2 + 2
    return y

def draw_axis(x_min, x_max, y_min, y_max, step_x=1, step_y=1):
    """Рисование осей координат с делениями"""
    tr.color("black")
    tr.width(1)
    
    # Ось X
    tr.up()
    tr.goto(x_min, 0)
    tr.down()
    tr.goto(x_max, 0)
    
    # Стрелка на оси X
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
    
    # Стрелка на оси Y
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
    
    # Деления на оси X
    tr.width(1)
    x = int(x_min)
    while x <= int(x_max):
        if x != 0:
            tr.up()
            tr.goto(x, 0)
            tr.down()
            tr.goto(x, -0.15)
            tr.up()
            tr.goto(x, -0.5)
            tr.write(str(x), align="center", font=("Arial", 9))
        x += step_x
    
    # Деления на оси Y
    y = int(y_min)
    while y <= int(y_max):
        if y != 0:
            tr.up()
            tr.goto(0, y)
            tr.down()
            tr.goto(-0.15, y)
            tr.up()
            tr.goto(-0.5, y)
            tr.write(str(y), align="right", font=("Arial", 9))
        y += step_y

def main():
    # Границы графика
    x_min, x_max = -6, 8
    y_min, y_max = -2, 4
    
    # Настройка окна
    Dx = 900
    Dy = 500
    tr.setup(Dx, Dy)
    tr.reset()
    tr.tracer(0, 0)  # Отключаем анимацию для скорости
    tr.setworldcoordinates(x_min - 0.5, y_min - 0.5, x_max + 0.5, y_max + 0.5)
    tr.title("ЛР7 Задание 1 - Вариант 20")
    tr.ht()
    
    # Рисуем оси
    draw_axis(x_min, x_max, y_min, y_max)
    
    # Рисуем график функции
    tr.color("blue")
    tr.width(2)
    tr.up()
    
    N = 1000  # Число точек
    dx = (x_max - x_min) / N
    x = x_min
    y = MyFun(x)
    tr.goto(x, y)
    tr.down()
    
    while x <= x_max:
        x += dx
        y = MyFun(x)
        tr.goto(x, y)
    
    # Заголовок
    tr.up()
    tr.goto(0, y_max - 0.3)
    tr.write("График функции (Вариант 20)", align="center", 
             font=("Arial", 12, "bold"))
    
    tr.update()
    tr.mainloop()

if __name__ == "__main__":
    main()