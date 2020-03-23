import sys
from PyQt5.QtWidgets import QDialog, QApplication
#from PyQt5 import QtCore
from classGui import Ui_Dialog

from student import Student

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonClickMe.clicked.connect(self.dispmessage)
        #End main UI code
        self.show()
        
    def dispmessage(self):
        studentObj = Student(self.ui.lineEditName.text())
        self.ui.labelResponse.setText("Hello {0}".format(studentObj.printName()))
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())