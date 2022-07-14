import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QProgressBar, QHeaderView, QStyledItemDelegate, QStyleOptionProgressBar, QStyle, QStyleOptionButton,\
     QPushButton, QCheckBox, QTableWidgetItem, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 800, 400)
        self.setWindowTitle('sdfsdf')

        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(800, 400)
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(9)
        
        table_column=['' , 'ID' , 'Filename', 'NCPU', 'Run Command', '', 'Status', 'Scratch', '']
        self.tablewidget.setHorizontalHeaderLabels(table_column)      
        self.tablewidget.setColumnWidth(0, 10)
        self.tablewidget.setColumnWidth(8, 10)
        self.tablewidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.tablewidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        # self.tablewidget.horizontalHeader().setSectionResizeMode(8, QHeaderView.ResizeToContents)
        # self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.tablewidget.setHorizontalHeaderItem(0, QTableWidgetItem(''))
        # self.tablewidget.setHorizontalHeaderItem(1, QTableWidgetItem('ID'))
        # self.tablewidget.setHorizontalHeaderItem(2, QTableWidgetItem('Filename'))

        progressbar = self.progress_bar()
        # chkbox = self.chkbox()
        ckbox2 = self.InsertTable()
        pshbtn = self.pshbtn()
        
    
    def progress_bar(self):
        pbar = QProgressBar(self.tablewidget)
        pbar.setValue(20)    
        pbar.setAlignment(Qt.AlignCenter)
        self.tablewidget.setCellWidget(0, 6, pbar)
    
    def chkbox(self):
        ckbox = QCheckBox()
        ckbox.setCheckState(Qt.Checked)
        self.tablewidget.setCellWidget(0, 0, ckbox)
    
    def pshbtn(self):
        btn1 = QPushButton("X")
        self.tablewidget.setCellWidget(0, 8, btn1)

    def InsertTable(self):                    
    
        self.checkBoxList = []
        for i in range(self.numRow):
            ckbox = QCheckBox()
            self.checkBoxList.append(ckbox)

        for i in range(self.numRow):              
            cellWidget = QWidget()
            layoutCB = QHBoxLayout(cellWidget)
            layoutCB.addWidget(self.checkBoxList[i])
            layoutCB.setAlignment(QtCore.Qt.AlignCenter)            
            layoutCB.setContentsMargins(0,0,0,0)
            cellWidget.setLayout(layoutCB)

            self.tableWidget.setCellWidget(i,0,cellWidget)            
            
        
        self.tableWidget.move(0,0)   
         
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
