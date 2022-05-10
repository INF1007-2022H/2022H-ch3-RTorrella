#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return square_root(a)


def square(a: float) -> float:
    return a ** 2


def average(a: float, b: float, c: float) -> float:
    list([a,b,c])
    return sum(list)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    dd= angle_degs + angle_mins/60 + angle_secs/3600
    r=(dd*pi)/180
    return r


def to_degrees(angle_rads: float) -> tuple:
    dd=(angle_rads*180)/pi
    d=int(dd)
    m=(dd-d)*60
    s=(dd-d-m/60)*3600
    return d, m, s


def to_celsius(temperature: float) -> float:
    c= (f-32)/
    return 0.0


def to_farenheit(temperature: float) -> float:
    f= temperature*1.8 + 32
    return f


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
