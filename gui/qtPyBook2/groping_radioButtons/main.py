import sys
from PyQt5.QtWidgets import QDialog, QApplication

from groupRadButton import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioSizeM.toggled.connect(self.dispPrice)
        self.ui.radioSizeL.toggled.connect(self.dispPrice)
        self.ui.radioSizeXL.toggled.connect(self.dispPrice)
        self.ui.radioSizeXXL.toggled.connect(self.dispPrice)
        self.ui.radioCreditAndDebit.toggled.connect(self.dispPrice)
        self.ui.radioNetBanking.toggled.connect(self.dispPrice)
        self.ui.radioCash.toggled.connect(self.dispPrice)
        #End main UI code
        self.show()
        
    def dispPrice(self):
        paySelected = ""
        sizeSelected = ""
        if self.ui.radioSizeM.isChecked() == True:
            sizeSelected = "Medium"
        elif self.ui.radioSizeL.isChecked() == True:
            sizeSelected = "Large"
        elif self.ui.radioSizeXL.isChecked() == True:
            sizeSelected = "Extra Large"
        elif self.ui.radioSizeXXL.isChecked() == True:
            sizeSelected = "Extra Extra Large"
        if self.ui.radioCreditAndDebit.isChecked() == True:
            paySelected = "Debit/Credit Card"
        elif self.ui.radioNetBanking.isChecked() == True:
            paySelected = "NetBanking"
        elif self.ui.radioCash.isChecked() == True:
            paySelected = "Cash On Delivery"
        self.ui.textTotalPrice.setText("Chosen shirt size is {0} and payment methos as {1}".format(sizeSelected,\
                                           paySelected))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())