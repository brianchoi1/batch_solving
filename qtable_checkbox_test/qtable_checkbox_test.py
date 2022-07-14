import numpy
from PyQt5 import QtCore, QtWidgets, QtGui
Qt = QtCore.Qt


class NumpyModel(QtCore.QAbstractTableModel):
    def __init__(self, narray, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._array = narray.point
        self.test = narray.enabled
        self.header_icon = None
        self.setHeaderIcon()

    def rowCount(self, _parent=None):
        return self._array.shape[0]

    def columnCount(self, _parent=None):
        return self._array.shape[1] + 1

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if (index.column() == 3):
            value = ''
        else:
            value = QtCore.QVariant(
                "%.5f" % self._array[index.row(), index.column()])
        if role == QtCore.Qt.EditRole:
            return value
        elif role == QtCore.Qt.DisplayRole:
            return value
        elif role == QtCore.Qt.CheckStateRole:
            if index.column() == 3:
                if self.test[index.row()]:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return QtCore.QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole and index.column() == 3:
            if value == Qt.Checked:
                self.test[index.row()] = True
            else:
                self.test[index.row()] = False
            self.setHeaderIcon()

        elif role == Qt.EditRole and index.column() != 3:
            row = index.row()
            col = index.column()
            if value.isdigit():
                self._array[row, col] = value
    
        return True

    def flags(self, index):
        if not index.isValid():
            return None

        if index.column() == 3:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def headerData(self, index, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DecorationRole:
            if index == 3:
                return QtCore.QVariant(QtGui.QPixmap(self.header_icon).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if index != 3:
                return QtCore.QVariant(index+1)

        return QtCore.QVariant()

    def toggleCheckState(self, index):
        if index == 3:
            if numpy.all(self.test == False):
                self.test.fill(True)
            else:
                self.test.fill(False)
            
            topLeft =self.index(0, 3)
            bottomRight = self.index(self.rowCount(), 3)
            self.dataChanged.emit(topLeft, bottomRight)
            self.setHeaderIcon()

    def setHeaderIcon(self):
        if numpy.all(self.test == True):
            self.header_icon = 'checked.png'
        elif numpy.all(self.test == False):
            self.header_icon = 'unchecked.png'
        else:
            self.header_icon = 'intermediate.png'
        self.headerDataChanged.emit(Qt.Horizontal, 3, 3)

if __name__ == "__main__":
    a = QtWidgets.QApplication([])
    w = QtWidgets.QTableView()

    d = numpy.rec.array([([1., 2., 3.], True), ([4., 5., 6.], False), ([7., 8., 9.], True)],
                        dtype=[('point', 'f4', 3), ('enabled', '?')])
    m = NumpyModel(d)
    w.setModel(m)
    w.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    w.setAlternatingRowColors(True)
    w.verticalHeader().setVisible(False)
    w.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    w.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
    w.horizontalHeader().setMinimumSectionSize(40)
    w.horizontalHeader().setDefaultSectionSize(40)

    header = w.horizontalHeader()
    header.sectionPressed.connect(m.toggleCheckState)
    w.show()
    a.exec_()