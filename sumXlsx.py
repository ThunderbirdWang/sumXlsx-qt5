# -*- coding: utf-8 -*-

import sys
import win
# import sip
# import PyQt5.sip #windows下用pyinstaller打包取消此行注释
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = win.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())