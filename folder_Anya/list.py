#!/usr/bin/env python3
# -*- coding: utf-8 -*-

students = []


def list():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Номер телефона",
            "Дата рождения"
        )
    )
    print(line)

    for idx, worker in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('number', ''),
                worker.get('month', 0)
            )
        )

    print(line)
