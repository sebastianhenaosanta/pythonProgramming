import sys
from PyQt5.QtWidgets import QDialog, QApplication
#from PyQt5 import QtCore
from demoStudent import Ui_Dialog, QtCore

from student import Student

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showLcd)
        timer.start(1000)
        self.ui.pushButtonClickMe.clicked.connect(self.dispmessage)
        #End main UI code
        self.show()
        
    def dispmessage(self):
        studentObj = Student(self.ui.lineEditCode.text(),self.ui.lineEditName.text())
        self.ui.labelResponse.setText("Code:{0}, Name:{1}".format(studentObj.getCode(),\
                                                                 studentObj.getName()))
    def showLcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.lcdNumber.display(text)    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())