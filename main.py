# https://stackoverflow.com/questions/56949297/how-to-fix-importerror-unable-to-find-qt5core-dll-on-path-after-pyinstaller-b
import fix_qt_import_error

import sys
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow

# change "TestUI" to the name of the .py file  created by pyuic5 command
from UI_main import *


#make sure the class parameter is matched with the form type created by designer
class MyForm(QMainWindow):
# class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        # self.ui = Ui_Dialog()
        
        self.ui.setupUi(self)
        
        # self.ui.pushButtonAdd.clicked.connect(self.dispSum)
        
        
        
        self.show()

    # def fnTest(self):
        # self.ui.pushBtn1.setText("Hello PyQt5")
    
    # def dispSum(self):
    #     numb1=self.ui.lineEditFirstNumb.text()
    #     numb2=self.ui.lineEditSecondNumb.text()
    #     x=int(numb1)
    #     y=int(numb2)
    #     z=x+y
    #     self.ui.labelResponse.setText("Sum is "+str(z))
 

if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    
    