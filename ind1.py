#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 15. Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата рождения (список из
# трех чисел). Написать программу, выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть упорядочены по датам рождения; вывод на экран информации о людях,
# родившихся под знаком, название которого введено с клавиатуры; если таких нет, выдать на дисплей соответствующее
# сообщение.

import sys
import json

if __name__ == '__main__':
    # Функции:
    def add():
        name = input("Фамилия и имя? ")
        zod = input("Знак Зодиака? ")
        birth = input("Дата рождения? ")

        # Создать словарь:
        people = {
            'name': name,
            'zod': zod,
            'birth': birth,
        }

        # Добавить словарь в список:
        peoples.append(people)
        # Отсортировать список в случае необходимости.
        if len(peoples) > 1:
            peoples.sort(key=lambda item: item.get('birth', ''))


    def list():
        # Заголовок таблицы.
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
                "Фамилия и имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех людях:
        for idx, people in enumerate(peoples, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    people.get('name', ''),
                    people.get('zod', ''),
                    people.get('birth', 0)
                )
            )

        print(line)


    def select():
        parts = command.split(' ', maxsplit=2)
        sel = (parts[1])

        count = 0
        for people in peoples:
            if people.get('zod') == sel:
                count = "Знак Зодиака"
                print('{:>4}: {}'.format(count, people.get('zod', ''))
                )
                print('Фамилия и имя:', peoples.get('name', ''))
                print('Дата рождения:', peoples.get('birth', ''))

        if count == 0:
            print("Люди с данным знаком Зодиака не найдены.")


    def help():
        # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("add - добавить человека;")
        print("list - вывести список людей;")
        print("select <знак зодиака> - запросить людей с знаком Зодиака;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")

    # Список людей.
    peoples = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ", ).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
            help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
