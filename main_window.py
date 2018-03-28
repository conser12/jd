import sched
import traceback

import time

import logging
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from jd import spider_main, price_monitor, data_storager


class MainWindow(QtWidgets.QWidget, price_monitor.Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.obj_spider = spider_main.SpiderMain()
        self.database = data_storager.DataStorage()
        self.urls = []
        self.schedule = sched.scheduler(time.time, time.sleep)
        # self.schedule.enter(1, 1, self.start, ())
        self.load_data()

    def load_data(self):
        data = self.database.retrieve()
        self.urls = data
        self.start()

    def add_monitor(self):
        url = self.urlEdit.text()
        target_price = self.priceEdit.text()
        data = {
            'url': url,
            'target_price': target_price
        }
        self.database.store(data)
        self.new_row(url, target_price)

    def new_row(self, url, target_price):
        if url is None:
            return

        data = self.obj_spider.craw(url)
        row_count = self.tableWidget.rowCount()
        index = 0
        if row_count == 0:
            self.tableWidget.setRowCount(1)
        else:
            index = 1
            self.tableWidget.insertRow(1)

        price = data['price']
        item = QTableWidgetItem(data['url'])
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(index, 0, item)

        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item = QTableWidgetItem("京东")
        self.tableWidget.setItem(index, 1, item)

        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item = QTableWidgetItem(data['title'])
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(index, 2, item)

        item = QTableWidgetItem(str(target_price))
        item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(index, 3, item)
        item = QTableWidgetItem(price)
        if float(price) < float(target_price):
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(index, 4, item)

    def start(self):
        logging.debug("start monitor price")
        urls = self.urls

        index = 0
        for url_dict in urls:
            try:
                self.new_row(url_dict['url'], url_dict['target_price'])
            except RuntimeError as err:
                str = traceback.format_exc()
                print("RuntimeError:", str)
            except Exception as err:
                str = traceback.format_exc()
                print("Exception:", str)

        # self.schedule.enter(5, 1, self.start, ())
        # self.schedule.run()

    # 定义槽函数
    def start_monitor(self):
        # s.enter(delay, priority, func1, (arg1, arg2, ...))
        self.schedule.run()

    def save_price(self, item):
        print("save price")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())