#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 13. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по алфавиту ; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение

import sys
from folder_Anya import add, list, select, help

if __name__ == '__main__':

    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add.add()

        elif command == 'list':
            list.list()

        elif command.startswith('select '):
            select.select()

        elif command == 'help':
            help.help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
