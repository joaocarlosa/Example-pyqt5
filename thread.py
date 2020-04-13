from PyQt5 import QtCore, QtGui, QtWidgets
from view import design
import sys
import threading

## para converter arquivo .ui para .py use:   
## pyuic5 design.ui > design.py


class processo(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(processo, self).__init__()        
        self.setupUi(self)

        #Metodos a serem inicializados
        self.label_2.setText("ola mundo")

        #chamada dos metodos
        processo.funcaoQualquer(self)

    def funcaoQualquer(self):
        self.label_4.setText("ola")
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = processo()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()