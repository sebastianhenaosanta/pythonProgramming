#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:04:19 2020

@author: sebastian
"""




from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget(windowTitle = 'Hello Qt')
window.show()
app.exec()