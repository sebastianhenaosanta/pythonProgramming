import sys
from PyQt5.QtWidgets import QDialog, QApplication

from processBar import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStart.clicked.connect(self.updateBar)
        #End main UI code
        self.show()
        
    def updateBar(self):
        x = 0.0
        while x < 100:
            x +=0.000001
            self.ui.progressBar1.setValue(x)
            

            
        
           
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())