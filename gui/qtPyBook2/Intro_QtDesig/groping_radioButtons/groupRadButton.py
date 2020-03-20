# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupRadButton.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(664, 366)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 156, 211, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 16, 161, 21))
        self.label_2.setObjectName("label_2")
        self.textTotalPrice = QtWidgets.QLabel(Dialog)
        self.textTotalPrice.setGeometry(QtCore.QRect(50, 300, 591, 51))
        self.textTotalPrice.setText("")
        self.textTotalPrice.setObjectName("textTotalPrice")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 160, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioSizeM = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioSizeM.setObjectName("radioSizeM")
        self.verticalLayout.addWidget(self.radioSizeM)
        self.radioSizeL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioSizeL.setObjectName("radioSizeL")
        self.verticalLayout.addWidget(self.radioSizeL)
        self.radioSizeXL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioSizeXL.setObjectName("radioSizeXL")
        self.verticalLayout.addWidget(self.radioSizeXL)
        self.radioSizeXXL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioSizeXXL.setObjectName("radioSizeXXL")
        self.verticalLayout.addWidget(self.radioSizeXXL)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 190, 181, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioCreditAndDebit = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioCreditAndDebit.setObjectName("radioCreditAndDebit")
        self.verticalLayout_2.addWidget(self.radioCreditAndDebit)
        self.radioNetBanking = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioNetBanking.setObjectName("radioNetBanking")
        self.verticalLayout_2.addWidget(self.radioNetBanking)
        self.radioCash = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioCash.setObjectName("radioCash")
        self.verticalLayout_2.addWidget(self.radioCash)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose your payment method"))
        self.label_2.setText(_translate("Dialog", "Choose your Shirt Size"))
        self.radioSizeM.setText(_translate("Dialog", "M"))
        self.radioSizeL.setText(_translate("Dialog", "L"))
        self.radioSizeXL.setText(_translate("Dialog", "XL"))
        self.radioSizeXXL.setText(_translate("Dialog", "XXL"))
        self.radioCreditAndDebit.setText(_translate("Dialog", "Debit/Credit Card"))
        self.radioNetBanking.setText(_translate("Dialog", "NetBanking"))
        self.radioCash.setText(_translate("Dialog", "Cash On Delivery"))

