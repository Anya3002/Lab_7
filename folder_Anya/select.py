#!/usr/bin/env python3
# -*- coding: utf-8 -*-

students = []
command = input(">>> ").lower()


def select():
    parts = command.split(' ', maxsplit=2)
    sel = (parts[1])

    count = 0
    for student in students:
        if student.get('month') == sel:
            count += 1
            print(
                '{:>4} {}'.format(count, student.get('name', '')),

            )

    if count == 0:
        print('У этого человека нет в этом месяце дня рождения')
