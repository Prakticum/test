# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLCD.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1114, 480)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 70, 901, 261))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumber.setDigitCount(8) # Fix this from 5-8 
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
