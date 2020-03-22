# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(606, 300)
        self.progressBar1 = QtWidgets.QProgressBar(Dialog)
        self.progressBar1.setGeometry(QtCore.QRect(160, 120, 261, 71))
        self.progressBar1.setProperty("value", 0)
        self.progressBar1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar1.setObjectName("progressBar1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(190, 230, 211, 41))
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.pushButtonStart.setText(_translate("Dialog", "Start Downloading"))

