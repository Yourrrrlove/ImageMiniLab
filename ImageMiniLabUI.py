# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageMiniLabUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageMiniLabUI(object):
    def setupUi(self, ImageMiniLabUI):
        ImageMiniLabUI.setObjectName("ImageMiniLabUI")
        ImageMiniLabUI.resize(1681, 892)
        self.centralwidget = QtWidgets.QWidget(ImageMiniLabUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.LabCtrlWidget = QtWidgets.QWidget(self.centralwidget)
        self.LabCtrlWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.LabCtrlWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.LabCtrlWidget.setObjectName("LabCtrlWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LabCtrlWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.LabCtrlWidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ExpTypeComboBox = QtWidgets.QComboBox(self.LabCtrlWidget)
        self.ExpTypeComboBox.setObjectName("ExpTypeComboBox")
        self.horizontalLayout_2.addWidget(self.ExpTypeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.LabCtrlWidget)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ExpImgLineEdit = QtWidgets.QLineEdit(self.LabCtrlWidget)
        self.ExpImgLineEdit.setEnabled(True)
        self.ExpImgLineEdit.setObjectName("ExpImgLineEdit")
        self.horizontalLayout_3.addWidget(self.ExpImgLineEdit)
        self.SelectImgPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.SelectImgPushButton.setObjectName("SelectImgPushButton")
        self.horizontalLayout_3.addWidget(self.SelectImgPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.LabCtrlWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget = QtWidgets.QStackedWidget(self.LabCtrlWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadTestDataPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.LoadTestDataPushButton.setObjectName("LoadTestDataPushButton")
        self.horizontalLayout.addWidget(self.LoadTestDataPushButton)
        self.GoExpPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.GoExpPushButton.setObjectName("GoExpPushButton")
        self.horizontalLayout.addWidget(self.GoExpPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.LabCtrlWidget, 0, 0, 1, 1)
        self.ImgShowWidget = QtWidgets.QWidget(self.centralwidget)
        self.ImgShowWidget.setObjectName("ImgShowWidget")
        self.SrcImgShowLabel = QtWidgets.QLabel(self.ImgShowWidget)
        self.SrcImgShowLabel.setGeometry(QtCore.QRect(35, 11, 120, 16))
        self.SrcImgShowLabel.setObjectName("SrcImgShowLabel")
        self.DstImgShowLabel = QtWidgets.QLabel(self.ImgShowWidget)
        self.DstImgShowLabel.setGeometry(QtCore.QRect(130, 100, 120, 16))
        self.DstImgShowLabel.setObjectName("DstImgShowLabel")
        self.gridLayout.addWidget(self.ImgShowWidget, 0, 1, 1, 1)
        ImageMiniLabUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageMiniLabUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1681, 26))
        self.menubar.setObjectName("menubar")
        ImageMiniLabUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageMiniLabUI)
        self.statusbar.setObjectName("statusbar")
        ImageMiniLabUI.setStatusBar(self.statusbar)

        self.retranslateUi(ImageMiniLabUI)
        QtCore.QMetaObject.connectSlotsByName(ImageMiniLabUI)

    def retranslateUi(self, ImageMiniLabUI):
        _translate = QtCore.QCoreApplication.translate
        ImageMiniLabUI.setWindowTitle(_translate("ImageMiniLabUI", "ImageMiniLab"))
        self.label_2.setText(_translate("ImageMiniLabUI", "实验类型："))
        self.label_3.setText(_translate("ImageMiniLabUI", "实验图片："))
        self.SelectImgPushButton.setText(_translate("ImageMiniLabUI", "选择"))
        self.label.setText(_translate("ImageMiniLabUI", "实验参数："))
        self.LoadTestDataPushButton.setText(_translate("ImageMiniLabUI", "载入测试数据"))
        self.GoExpPushButton.setText(_translate("ImageMiniLabUI", "进行实验"))
        self.SrcImgShowLabel.setText(_translate("ImageMiniLabUI", "SrcImgShowLabel"))
        self.DstImgShowLabel.setText(_translate("ImageMiniLabUI", "DstImgShowLabel"))


