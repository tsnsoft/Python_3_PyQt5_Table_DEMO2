#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        Метод для кнопки "Заполнить случайными числами"
        Случайные числа от 1 до 100
        """
        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

    def solve(self):
        """
        Метод для кнопки "Выполнить задание"
        """
        result = find_max_min_sum(self.tableWidget)
        self.label_info.setText(result.__str__())

        max_num = result[0]
        row_max_number = result[1]
        col_max_number = result[2]
        min_num = result[3]
        row_min_number = result[4]
        col_min_number = result[5]
        sum_table = result[6]

        if sum_table > 1000:
            self.tableWidget.setItem(row_max_number, col_max_number, QTableWidgetItem(str(min_num)))
            self.tableWidget.setItem(row_min_number, col_min_number, QTableWidgetItem(str(max_num)))


def find_max_min_sum(table_widget):
    """
    Поиск максимума, минимума и суммы в таблице
    :param table_widget: таблица
    :return: список с данными: max_num, row_max_number, col_max_number,
            min_num, row_min_number, col_min_number,
            sum_table
    """
    row_max_number = 0
    col_max_number = 0
    row_min_number = 0
    col_min_number = 0
    sum_table = 0
    max_num = float(table_widget.item(row_max_number, col_max_number).text())
    min_num = max_num

    row = 0
    col = 0
    while row < table_widget.rowCount():
        while col < table_widget.columnCount():
            number = float(table_widget.item(row, col).text())
            if number > max_num:
                max_num = number
                row_max_number = row
                col_max_number = col
            if number < min_num:
                min_num = number
                row_min_number = row
                col_min_number = col
            sum_table = sum_table + number
            col += 1
        row += 1
        col = 0
    return [max_num, row_max_number, col_max_number,
            min_num, row_min_number, col_min_number,
            sum_table]


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
