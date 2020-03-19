import sys
from PyQt5.QtWidgets import QDialog, QApplication

from demoRadioButton import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()
    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked() == True:
            fare = 150
        elif self.ui.radioButtonBusinessClass.isChecked() == True:
            fare = 125
        elif self.ui.radioButtonEconomyClass.isChecked() == True:
            fare = 100
        self.ui.labelFare.setText("Air Fare is {0}".format(fare))
        
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
