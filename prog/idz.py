#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Для своего варианта лабораторной работы 2.17 добавьте возможность хранения файла данных
#в домашнем каталоге пользователя. Для выполнения операций с файлами необходимо
#использовать модуль pathlib .

#Использовать словарь, содержащий следующие ключи: название начального пункта
#маршрута; название конечного пункта маршрута; номер маршрута. Написать программу,
#выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
#словарей заданной структуры; записи должны быть упорядочены по номерам маршрутов;
#вывод на экран информации о маршрутах, которые начинаются или оканчиваются в пункте,
#название которого введено с клавиатуры; если таких маршрутов нет, выдать на дисплей
#соответствующее сообщение.


import json
import argparse
from pathlib import Path

# Получаем путь к домашнему каталогу пользователя
home_dir = str(Path.home())

# Создаем путь к файлу данных в домашнем каталоге пользователя
file_path = Path(home_dir) / "idz.json"

# Функция для ввода данных о маршрутах
def add_route(routes, start, end, number):
    route = {
        "start": start,
        "end": end,
        "number": number
    }
    routes.append(route)
    return routes

# Функция для вывода информации о маршруте по номеру
def find_route(routes, number):
    found = False
    for route in routes:
        if route["number"] == number:
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True
            break
    if not found:
        print("Маршрут с таким номером не найден.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Управление маршрутами')
    parser.add_argument('--add', action='store_true', help='Добавить новый маршрут')
    parser.add_argument('--number', type=str, help='Номер маршрута для поиска')

    args = parser.parse_args()

    try:
        with open(file_path, "r") as file:
            routes = json.load(file)
    except FileNotFoundError:
        routes = []

    if args.add:
        start = input("Введите начальный пункт маршрута: ")
        end = input("Введите конечный пункт маршрута: ")
        number = input("Введите номер маршрута: ")
        routes = add_route(routes, start, end, number)

    if args.number:
        find_route(routes, args.number)

    # Сохраняем данные в файл JSON после ввода информации
    with open(file_path, "w") as file:
        json.dump(routes, file)
