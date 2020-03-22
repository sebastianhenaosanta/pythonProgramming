# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 233)
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(340, 50, 81, 26))
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(340, 100, 81, 26))
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setEnabled(True)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(150, 50, 142, 23))
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(150, 100, 142, 23))
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(460, 50, 142, 23))
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(460, 100, 142, 23))
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(156, 156, 441, 41))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.pushButtonTotal = QtWidgets.QPushButton(Dialog)
        self.pushButtonTotal.setGeometry(QtCore.QRect(30, 150, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButtonTotal.setFont(font)
        self.pushButtonTotal.setObjectName("pushButtonTotal")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))
        self.pushButtonTotal.setText(_translate("Dialog", "total"))

