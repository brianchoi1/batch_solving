from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QApplication, QTextEdit, QDialog, QLabel, QLineEdit, QGridLayout
import os


class Ui_MainWindow(object):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui = Ui_MainWindow()
    # ui.show()
    sys.exit(app.exec_())