import sys
from PyQt5.QtWidgets import QDialog, QApplication

from smallCalculator import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.sum2Numbers)
        self.ui.pushButtonSubstract.clicked.connect(self.substrack2Numbers)
        self.ui.pushButtonMultiply.clicked.connect(self.multiply2Numbers)
        self.ui.pushButtonDivide.clicked.connect(self.divide2Numbers)
        self.show()
        
    def sum2Numbers(self):
       
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        
        self.ui.labelResult.setText("Addition: {0}".format(a+b))
        
    def substrack2Numbers(self):
        
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        self.ui.labelResult.setText("Substraction: {0}".format(a-b))
        
    def multiply2Numbers(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        self.ui.labelResult.setText("Multiplication: {0}".format(a*b))
    
    def divide2Numbers(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
            
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        self.ui.labelResult.setText("Division: {0}".format(a/b))
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())