import sys
from PyQt5.QtWidgets import QDialog, QApplication

from spinBox import Ui_Dialog

class MainWindow(QDialog):
    
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.totalBook = 0
        self.totalSugar = 0
        #Main UI code goes here
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.valueChanged.connect(self.resultBooksQ)
        self.ui.spinBoxBookQty.editingFinished.connect(self.resultBooksQ)
        self.ui.doubleSpinBoxSugarWeight.valueChanged.connect(self.resultSugarW)
        self.ui.pushButtonTotal.clicked.connect(self.allResults)
        self.show()
    
    def resultBooksQ(self):
        
        if len(self.ui.lineEditBookPrice.text()) != 0 and self.ui.lineEditBookPrice.text().isdigit():
            bookPrice = int(self.ui.lineEditBookPrice.text())
            self.ui.lineEditBookAmount.setText(str(self.ui.spinBoxBookQty.value()))
            self.totalBook = bookPrice*self.ui.spinBoxBookQty.value()
        else:
            self.totalBook = 0
            self.ui.lineEditBookAmount.setText(str(0))
        
    def resultSugarW(self):
        if len(self.ui.lineEditSugarPrice.text()) != 0 and self.ui.lineEditSugarPrice.text().isdigit():
            sugarPrice = int(self.ui.lineEditSugarPrice.text())
            self.ui.lineEditSugarAmount.setText(str(self.ui.doubleSpinBoxSugarWeight.value()))
            self.totalSugar = sugarPrice * self.ui.doubleSpinBoxSugarWeight.value()
        else:
            self.totalSugar = 0
            self.ui.lineEditSugarAmount.setText(str(0))
    
    def allResults(self):
        
        self.ui.labelTotalAmount.setText("the total price of Sugar is: {0} and the total price of Books are: {1}".format(self.totalSugar,self.totalBook))
                                         
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())