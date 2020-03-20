import sys
from PyQt5.QtWidgets import QDialog, QApplication

from checkBoxPizza import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxExtraCheese.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxExtraOlives.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxExtraSausages.stateChanged.connect(self.dispPrice)
        #End main UI code
        self.show()
        
    def dispPrice(self):
        total = 10
        if self.ui.checkBoxExtraCheese.isChecked() == True:
            total += 1
        if self.ui.checkBoxExtraOlives.isChecked() == True:
            total += 1
        if self.ui.checkBoxExtraSausages.isChecked() == True:
            total += 2
        
        self.ui.totalPrice.setText("Total amount for pizza is {0}".format(total))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())