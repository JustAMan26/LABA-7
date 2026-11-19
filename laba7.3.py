# -*- coding: cp1251 -*-
from math import atan, pi
import turtle as tr

def arctg_series(x, eps=1e-3):
    """Вычисление arctg(x) через ряд Тейлора с точностью eps"""
    if abs(x) > 1:
        return None  # Ряд расходится
    
    an = x          # Первый член ряда
    S = an          # Сумма
    n = 0           # Номер члена
    
    while abs(an) >= eps:
        # Рекуррентная формула: a_{n+1} = -a_n * x^2 * (2n+1) / (2n+3)
        k = -x**2 * (2*n + 1) / (2*n + 3)
        an = an * k
        S += an
        n += 1
    
    return S

def draw_axes(x_min, x_max, y_min, y_max, step_x=0.2, step_y=0.2):
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
    tr.goto(x_max - 0.05, 0.03)
    tr.up()
    tr.goto(x_max, 0)
    tr.down()
    tr.goto(x_max - 0.05, -0.03)
    tr.up()
    tr.goto(x_max + 0.05, -0.08)
    tr.write("X", font=("Arial", 11, "bold"))
    
    # Ось Y
    tr.up()
    tr.goto(0, y_min)
    tr.down()
    tr.goto(0, y_max)
    tr.up()
    tr.goto(0, y_max)
    tr.down()
    tr.goto(0.03, y_max - 0.05)
    tr.up()
    tr.goto(0, y_max)
    tr.down()
    tr.goto(-0.03, y_max - 0.05)
    tr.up()
    tr.goto(0.05, y_max + 0.03)
    tr.write("Y", font=("Arial", 11, "bold"))
    
    # Деления на оси X
    x = -1.0
    while x <= 1.0 + 1e-9:
        if abs(x) > 1e-9:
            tr.up()
            tr.goto(x, 0)
            tr.down()
            tr.goto(x, -0.03)
            tr.up()
            tr.goto(x, -0.1)
            tr.write(f"{x:.1f}", align="center", font=("Arial", 8))
        x += step_x
    
    # Деления на оси Y
    y = -1.0
    while y <= 1.0 + 1e-9:
        if abs(y) > 1e-9:
            tr.up()
            tr.goto(0, y)
            tr.down()
            tr.goto(-0.03, y)
            tr.up()
            tr.goto(-0.1, y)
            tr.write(f"{y:.1f}", align="right", font=("Arial", 8))
        y += step_y

def main():
    x_min, x_max = -1.2, 1.2
    y_min, y_max = -1.2, 1.2
    eps = 1e-3
    
    Dx = 700
    Dy = 700
    tr.setup(Dx, Dy)
    tr.reset()
    tr.tracer(0, 0)
    tr.setworldcoordinates(x_min, y_min, x_max, y_max)
    tr.title("ЛР7 Задание 3 - Ряд arctg(x), eps=1e-3 (Вариант 20)")
    tr.ht()
    
    # Рисуем оси
    draw_axes(x_min, x_max, y_min, y_max)
    
    # Рисуем график функции через ряд (синий)
    tr.color("blue")
    tr.width(2)
    tr.up()
    
    N = 500
    dx = (x_max - x_min) / N
    x = x_min
    
    # Находим первую допустимую точку
    while x <= 1.0 and abs(x) > 1.0:
        x += dx
    
    if abs(x) <= 1.0:
        y = arctg_series(x, eps)
        if y is not None:
            tr.goto(x, y)
            tr.down()
    
    while x <= 1.0:
        y = arctg_series(x, eps)
        if y is not None:
            tr.goto(x, y)
        else:
            tr.up()
        x += dx
    
    # Рисуем точный график arctg(x) для сравнения (красный пунктир)
    tr.color("red")
    tr.width(1)
    tr.up()
    x = x_min
    while x <= 1.0:
        if abs(x) <= 1.0:
            y = atan(x)
            tr.goto(x, y)
            tr.down()
        x += dx
    
    # Заголовок и легенда
    tr.up()
    tr.goto(0, 1.05)
    tr.write("arctg(x): ряд (синий), точное (красный)", 
             align="center", font=("Arial", 10, "bold"))
    
    tr.update()
    
    # Тестовые значения
    print("Сравнение ряда и точного значения arctg(x):")
    print(f"{'x':>6} {'Ряд':>10} {'Точное':>10} {'Разность':>10}")
    for x_test in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y_row = arctg_series(x_test, eps)
        y_exact = atan(x_test)
        print(f"{x_test:6.2f} {y_row:10.6f} {y_exact:10.6f} {abs(y_row-y_exact):10.6f}")
    
    tr.mainloop()

if __name__ == "__main__":
    main()