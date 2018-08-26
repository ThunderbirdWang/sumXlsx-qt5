# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import xlsproc,_thread

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(580, 278)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pickBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pickBtn.setGeometry(QtCore.QRect(30, 50, 131, 41))
        self.pickBtn.setObjectName("pickBtn")
        self.pickBtn.clicked.connect(self.pickFile)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 50, 361, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.sumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sumBtn.setGeometry(QtCore.QRect(210, 140, 171, 41))
        self.sumBtn.setObjectName("sumBtn")
        self.sumBtn.clicked.connect(self.procXlsx)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 36))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "多表汇总"))
        self.pickBtn.setText(_translate("mainWindow", "选取xlsx文件"))
        self.sumBtn.setText(_translate("mainWindow", "汇总"))

    def pickFile(self):
        sourcePath, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;Excle Files (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.lineEdit.setText(sourcePath)

    def procXlsx(self):
        if self.lineEdit.text()=='' or self.lineEdit.text()=='请选取需要汇总的xlsx文件':
            self.lineEdit.setText('请选取需要汇总的xlsx文件')
        else:
            sourcePath=self.lineEdit.text()
            defaultDistPath=sourcePath[:-5]+'已汇总.xlsx'
            wb=xlsproc.pro_xls(sourcePath)
            distPath, ok2 = QFileDialog.getSaveFileName(self.centralwidget,
                                                        "文件保存",
                                                        defaultDistPath,
                                                        "All Files (*);;Excle Files (*.xlsx)")
            wb.save(distPath)
