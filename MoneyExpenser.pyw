#!/usr/bin/env python

import sys
from PyQt4 import QtGui


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    import MainWindow
    window = MainWindow.MainWindow()
    window.show()
    
    app.exec_()
