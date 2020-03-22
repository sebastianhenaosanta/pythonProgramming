# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smallCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 353)
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(40, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFirstNumber.setFont(font)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(40, 130, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelSecondNumber.setFont(font)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(140, 230, 41, 25))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(250, 50, 221, 31))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(250, 140, 221, 31))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonSubstract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubstract.setGeometry(QtCore.QRect(200, 230, 41, 25))
        self.pushButtonSubstract.setObjectName("pushButtonSubstract")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(260, 230, 41, 25))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(330, 230, 41, 25))
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(80, 290, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter first number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter second number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubstract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "x"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))

