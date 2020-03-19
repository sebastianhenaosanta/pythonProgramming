# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkBoxPizza.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 270)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBoxExtraCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxExtraCheese.setGeometry(QtCore.QRect(310, 110, 131, 23))
        self.checkBoxExtraCheese.setObjectName("checkBoxExtraCheese")
        self.checkBoxExtraOlives = QtWidgets.QCheckBox(Dialog)
        self.checkBoxExtraOlives.setGeometry(QtCore.QRect(310, 140, 131, 23))
        self.checkBoxExtraOlives.setObjectName("checkBoxExtraOlives")
        self.checkBoxExtraSausages = QtWidgets.QCheckBox(Dialog)
        self.checkBoxExtraSausages.setGeometry(QtCore.QRect(310, 170, 151, 23))
        self.checkBoxExtraSausages.setObjectName("checkBoxExtraSausages")
        self.totalPrice = QtWidgets.QLabel(Dialog)
        self.totalPrice.setGeometry(QtCore.QRect(40, 210, 241, 31))
        self.totalPrice.setText("")
        self.totalPrice.setObjectName("totalPrice")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
        self.checkBoxExtraCheese.setText(_translate("Dialog", "Extra Cheese $1"))
        self.checkBoxExtraOlives.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxExtraSausages.setText(_translate("Dialog", "Extra Sausages $2"))

