# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloWorldPyQt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(511, 263)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(90, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelResponse.setFont(font)
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(290, 170, 141, 41))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 160, 81, 61))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(240, 90, 221, 31))
        self.lineEditName.setObjectName("lineEditName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelResponse.setText(_translate("Dialog", "Enter your name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label.setText(_translate("Dialog", "TextLabel"))

