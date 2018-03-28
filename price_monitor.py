# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'price_monitor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 556)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 941, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.beginBtn = QtWidgets.QPushButton(Form)
        self.beginBtn.setGeometry(QtCore.QRect(580, 460, 113, 32))
        self.beginBtn.setObjectName("beginBtn")
        self.stopBtn = QtWidgets.QPushButton(Form)
        self.stopBtn.setGeometry(QtCore.QRect(580, 500, 113, 32))
        self.stopBtn.setObjectName("stopBtn")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 440, 421, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label.setObjectName("label")
        self.urlEdit = QtWidgets.QLineEdit(self.groupBox)
        self.urlEdit.setGeometry(QtCore.QRect(70, 20, 331, 31))
        self.urlEdit.setText("")
        self.urlEdit.setObjectName("urlEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.priceEdit = QtWidgets.QLineEdit(self.groupBox)
        self.priceEdit.setGeometry(QtCore.QRect(70, 60, 101, 31))
        self.priceEdit.setObjectName("priceEdit")
        self.addBtn = QtWidgets.QPushButton(self.groupBox)
        self.addBtn.setGeometry(QtCore.QRect(310, 60, 91, 32))
        self.addBtn.setObjectName("addBtn")
        self.beginBtn.raise_()
        self.stopBtn.raise_()
        self.groupBox.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Form)
        self.beginBtn.clicked.connect(Form.start_monitor)
        self.stopBtn.clicked.connect(Form.close)
        self.addBtn.clicked.connect(Form.add_monitor)
        self.tableWidget.itemChanged['QTableWidgetItem*'].connect(Form.save_price)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "价格监控软件"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "地址"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商家"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "目标价格"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "实际价格"))
        self.beginBtn.setText(_translate("Form", "开始"))
        self.stopBtn.setText(_translate("Form", "退出"))
        self.groupBox.setTitle(_translate("Form", "新增商品"))
        self.label.setText(_translate("Form", "网址"))
        self.label_2.setText(_translate("Form", "目标价格"))
        self.addBtn.setText(_translate("Form", "新增"))
