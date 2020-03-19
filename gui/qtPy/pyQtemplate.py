#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:37:24 2020

@author: sebastian
"""



import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        subwidget = qtw.QWidget(self, toolTip='This is my widget')
        subwidget.setToolTip('This is YOUR widget')
        print(subwidget.toolTip())
        label = qtw.QLabel('<b>Hello Widgets!</b>', self, margin=10)
        
        
         ################
        # Size Control #
        ################

        # setting a fixed size
        # Fix at 150 pixels wide by 40 pixels high
        label.setFixedSize(150, 40)

        
        """
        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText='Type here',
            clearButtonEnabled=True,
            maxLength=20
        )
        
        #End main UI code
        self.show()
        
        """
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())