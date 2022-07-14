from PyQt5 import QtGui
from PyQt5 import QtWidgets

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.DirectoryOnly)

        for view in self.findChildren((QtWidgets.QListView, QtWidgets.QTreeView)):
            if isinstance(view.model(), QtWidgets.QFileSystemModel):
                view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = FileDialog()
    ex.show()
    ex.exec_()
    print(ex.selectedFiles())
    sys.exit(app.exec_())