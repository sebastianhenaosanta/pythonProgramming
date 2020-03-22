import sys
from PyQt5.QtWidgets import QDialog, QApplication

from copyPaste import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #End main UI code
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())