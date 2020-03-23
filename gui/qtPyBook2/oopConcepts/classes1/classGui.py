# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 331)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 140, 281, 31))
        self.labelResponse.setObjectName("labelResponse")
        self.pushButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.pushButtonClickMe.setGeometry(QtCore.QRect(160, 190, 161, 61))
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
        self.lineEditName.setGeometry(QtCore.QRect(210, 70, 231, 25))
        self.lineEditName.setObjectName("lineEditName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label.setText(_translate("Dialog", "Enter your name"))

