#!/usr/bin/env python3
# -*- coding: utf-8 -*-

students = []


def add():
    name = input("Фамилия и инициалы? ")
    number = input("Номер телефона? ")
    print("Дата рождения:")
    day = input("день")
    month = input("Месяц")
    year = input("Год")

    student = {
        'name': name,
        'number': number,
        'day': day,
        'month': month,
        'year': year,
    }

    students.append(student)
    if len(student) > 1:
        students.sort(key=lambda item: item.get('name', ''))
