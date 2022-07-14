import sys
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QStyledItemDelegate, QHBoxLayout, QStyle, \
                            QStyleOptionProgressBar, QStyleOptionButton

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(650, 240)

        self.model = QStandardItemModel(5, 6)   # 1
        # for row in range(6):
        #     for column in range(6):
        #         item = QStandardItem(f'({row}, {column})')
        #         self.model.setItem(row, column, item)

        self.table = QTableView()
        self.table.setModel(self.model)
        # self.table.horizontalHeader().setStretchLastSection(True)

        delegate_demo = DelegateDemo()          # 2
        self.table.setItemDelegate(delegate_demo)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table)
        self.setLayout(h_layout)


class DelegateDemo(QStyledItemDelegate):
    def __init__(self):
        super(DelegateDemo, self).__init__()

    def paint(self, painter, option, index):
        if index.row() == 0 and index.column() == 0:        # 1
            progress_style = QStyleOptionProgressBar()
            progress_style.rect = option.rect
            progress_style.minimum = 0
            progress_style.maximum = 100
            progress_style.progress = 50
            QApplication.style().drawControl(QStyle.CE_ProgressBar, progress_style, painter)

        elif index.row() == 0 and index.column() == 1:      # 2
            check_style = QStyleOptionButton()
            check_style.rect = option.rect
            if index.data():
                check_style.state = QStyle.State_Enabled | QStyle.State_On
            else:
                check_style.state = QStyle.State_Enabled | QStyle.State_Off
            QApplication.style().drawControl(QStyle.CE_CheckBox, check_style, painter)

        else:
            return super(DelegateDemo, self).paint(painter, option, index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())