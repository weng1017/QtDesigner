# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 20, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 20, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.menu.addAction(self.actionquit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.comboBox.setItemText(0, _translate("MainWindow", "一月"))
        self.comboBox.setItemText(1, _translate("MainWindow", "二月"))
        self.comboBox.setItemText(2, _translate("MainWindow", "三月"))
        self.comboBox.setItemText(3, _translate("MainWindow", "四月"))
        self.comboBox.setItemText(4, _translate("MainWindow", "五月"))
        self.comboBox.setItemText(5, _translate("MainWindow", "六月"))
        self.comboBox.setItemText(6, _translate("MainWindow", "七月"))
        self.comboBox.setItemText(7, _translate("MainWindow", "八月"))
        self.comboBox.setItemText(8, _translate("MainWindow", "九月"))
        self.comboBox.setItemText(9, _translate("MainWindow", "十月"))
        self.comboBox.setItemText(10, _translate("MainWindow", "十一月"))
        self.comboBox.setItemText(11, _translate("MainWindow", "十二月"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "进驻部门"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "交易中心"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionquit.setText(_translate("MainWindow", "quit"))

