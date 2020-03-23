# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoStudent.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 331)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 210, 451, 31))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.pushButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.pushButtonClickMe.setGeometry(QtCore.QRect(160, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonClickMe.setFont(font)
        self.pushButtonClickMe.setObjectName("pushButtonClickMe")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 143, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(220, 130, 231, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(220, 70, 231, 25))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 0, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))

