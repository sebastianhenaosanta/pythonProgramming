import sys
from PyQt5.QtWidgets import QDialog, QApplication

from groupCheckBoxes import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxMintChocolate.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxCookieDough.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxChocolateAlmond.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxRockyRoad.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxCoffee.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxSoda.stateChanged.connect(self.dispPrice)
        self.ui.checkBoxTea.stateChanged.connect(self.dispPrice)
        #End main UI code
        self.show()
        
    def dispPrice(self):
        total = 0
        if self.ui.checkBoxMintChocolate.isChecked() == True:
            total += 4
        if self.ui.checkBoxCookieDough.isChecked() == True:
            total += 2
        if self.ui.checkBoxChocolateAlmond.isChecked() == True:
            total += 2
        if self.ui.checkBoxCoffee.isChecked() == True:
            total += 2
        if self.ui.checkBoxSoda.isChecked() == True:
            total += 3
        if self.ui.checkBoxTea.isChecked() == True:
            total +=1
        self.ui.priceTextLabel.setText("Total amount is {0}".format(total))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())