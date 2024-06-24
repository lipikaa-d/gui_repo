# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import gui_2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 771))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 40))
        self.tabWidget.setStyleSheet("/* Main Window Style */\n"
"QWidget {\n"
"    background-color: rgb(255, 204, 255);  /* Pinkish background */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, -1, 568, 44))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Number_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Number_label.sizePolicy().hasHeightForWidth())
        self.Number_label.setSizePolicy(sizePolicy)
        self.Number_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Number_label.setStyleSheet("/* Title Label Style */\n"
"QLabel#Number_label {\n"
"    background-color:rgb(44, 120, 127);  /* Bluish background */\n"
"    color: white;               /* Font color for the text */\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 10px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}\n"
"")
        self.Number_label.setObjectName("Number_label")
        self.horizontalLayout.addWidget(self.Number_label)
        self.text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text.setStyleSheet("\n"
"QLabel#text{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: bold 17pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"\n"
"")
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 751, 509))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 12, 3, 1, 1)
        self.text_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_11.setStyleSheet("QLabel#text_11{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;               \n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_11.setObjectName("text_11")
        self.gridLayout.addWidget(self.text_11, 6, 5, 1, 1)
        self.text_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_12.setStyleSheet("\n"
"QLabel#text_12{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_12.setObjectName("text_12")
        self.gridLayout.addWidget(self.text_12, 5, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 10, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setStyleSheet("QLineEdit#lineEdit_6{\n"
"background-color: #ffffff;\n"
"border: 2px solid #000;\n"
"border-radius: 6px;                   /* Rounded corners */\n"
"  \n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 7, 1, 1)
        self.text_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_4.setStyleSheet("\n"
"QLabel#text_4{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 17pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_4.setObjectName("text_4")
        self.gridLayout.addWidget(self.text_4, 9, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 3, 1, 1)
        self.text_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_10.setStyleSheet("\n"
"QLabel#text_10{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_10.setObjectName("text_10")
        self.gridLayout.addWidget(self.text_10, 3, 7, 1, 1)
        self.text_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_3.setStyleSheet("\n"
"QLabel#text_3{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 17pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_3.setObjectName("text_3")
        self.gridLayout.addWidget(self.text_3, 6, 2, 1, 1)
        self.text_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_7.setStyleSheet("\n"
"QLabel#text_7{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_7.setObjectName("text_7")
        self.gridLayout.addWidget(self.text_7, 2, 5, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setStyleSheet("QLineEdit#lineEdit_4{\n"
"background-color: #ffffff;\n"
"border: 2px solid #000;\n"
"border-radius: 6px;                   /* Rounded corners */\n"
"  \n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 5, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #000;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 10, 2, 1, 1)
        self.text_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_2.sizePolicy().hasHeightForWidth())
        self.text_2.setSizePolicy(sizePolicy)
        self.text_2.setStyleSheet("\n"
"QLabel#text_2{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 17pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_2.setObjectName("text_2")
        self.gridLayout.addWidget(self.text_2, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 6, 1, 1)
        self.text_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_14.setStyleSheet("QLabel#text_14{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_14.setObjectName("text_14")
        self.gridLayout.addWidget(self.text_14, 6, 7, 1, 1)
        self.text_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_13.setStyleSheet("QLabel#text_13{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;              \n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_13.setObjectName("text_13")
        self.gridLayout.addWidget(self.text_13, 5, 7, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setStyleSheet("QLineEdit#lineEdit_5{\n"
"background-color: #ffffff;\n"
"border: 2px solid #000;\n"
"border-radius: 6px;                   /* Rounded corners */\n"
"  \n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 3, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #000;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 4, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #000;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 7, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 3, 1, 1)
        self.text_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_6.setStyleSheet("\n"
"QLabel#text_6\n"
"{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 17pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_6.setObjectName("text_6")
        self.gridLayout.addWidget(self.text_6, 12, 2, 1, 1)
        self.text_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_9.setStyleSheet("\n"
"QLabel#text_9{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_9.setObjectName("text_9")
        self.gridLayout.addWidget(self.text_9, 2, 7, 1, 1)
        self.text_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_8.setStyleSheet("\n"
"QLabel#text_8{\n"
"background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_8.setObjectName("text_8")
        self.gridLayout.addWidget(self.text_8, 3, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 13, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setStyleSheet("QLineEdit#lineEdit_7{\n"
"background-color: #ffffff;\n"
"border: 2px solid #000;\n"
"border-radius: 6px;                   /* Rounded corners */\n"
"  \n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 7, 7, 1, 1)
        self.text_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.text_16.setStyleSheet("\n"
"QLabel#text_16{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 17pt  \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}")
        self.text_16.setObjectName("text_16")
        self.gridLayout.addWidget(self.text_16, 14, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 14, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(30, 590, 701, 121))
        self.textBrowser.setStyleSheet("QTextBrowser#textBrowser{\n"
" background-color: white;\n"
"}\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 551, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Number_label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Number_label_2.sizePolicy().hasHeightForWidth())
        self.Number_label_2.setSizePolicy(sizePolicy)
        self.Number_label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Number_label_2.setStyleSheet("/* Title Label Style */\n"
"QLabel#Number_label_2{\n"
"    background-color:rgb(44, 120, 127);  /* Bluish background */\n"
"    color: white;               /* Font color for the text */\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 10px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}\n"
"")
        self.Number_label_2.setObjectName("Number_label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Number_label_2)
        self.text_5 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_5.sizePolicy().hasHeightForWidth())
        self.text_5.setSizePolicy(sizePolicy)
        self.text_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_5.setStyleSheet("\n"
"QLabel#text_5{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: bold 17pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"\n"
"")
        self.text_5.setObjectName("text_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.text_5)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("\n"
"QLabel#label{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: bold 17pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 280, 451, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #000;\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_2.addWidget(self.lineEdit_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(167, 255, 200);  /* Bluish background */\n"
"    color: rgb(148, 0, 111);               /* Font color for the text */\n"
"    font: bold 8pt \"MS Shell Dlg 2\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;                   /* Rounded corners */\n"
"    border: 2px solid rgb(85, 0, 127);           \n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.text_15 = QtWidgets.QLabel(self.tab_2)
        self.text_15.setGeometry(QtCore.QRect(30, 230, 251, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_15.sizePolicy().hasHeightForWidth())
        self.text_15.setSizePolicy(sizePolicy)
        self.text_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_15.setStyleSheet("\n"
"QLabel#text_15{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: bold 17pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"\n"
"")
        self.text_15.setObjectName("text_15")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 551, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("\n"
"QLabel#label_2{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: 12pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 441, 61))
        self.label_3.setStyleSheet("\n"
"QLabel#label_3{\n"
" background-color: rgb(255, 204, 255);\n"
"color: black;                /* Font color */\n"
"font: bold 17pt \"Arial Narrow\";\n"
" font-weight: normal;\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 380, 431, 199))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_1.setStyleSheet("\n"
"\n"
"QCheckBox#checkBox_1 {\n"
"    background-color: rgb(255, 204, 255); \n"
"    color: black;                       \n"
"    font: normal 17pt \"Arial Narrow\";   \n"
"}\n"
"\n"
"QCheckBox#checkBox_1::indicator {\n"
"background-color: white; \n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"QCheckBox#checkBox_1::indicator:unchecked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/unchecked.svg\"); \n"
"}\n"
"\n"
"QCheckBox#checkBox_1::indicator:checked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/checked.svg\"); \n"
"}")
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setStyleSheet("QCheckBox#checkBox_2 {\n"
"    background-color: rgb(255, 204, 255); \n"
"    color: black;                       \n"
"    font: normal 17pt \"Arial Narrow\";   \n"
"}\n"
"\n"
"QCheckBox#checkBox_2::indicator {\n"
"background-color: white; \n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"QCheckBox#checkBox_2::indicator:unchecked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/unchecked.svg\"); \n"
"}\n"
"\n"
"QCheckBox#checkBox_2::indicator:checked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/checked.svg\"); \n"
"}\n"
"")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setStyleSheet("QCheckBox#checkBox_3 {\n"
"    background-color: rgb(255, 204, 255); \n"
"    color: black;                       \n"
"    font: normal 17pt \"Arial Narrow\";   \n"
"}\n"
"\n"
"QCheckBox#checkBox_3::indicator {\n"
"background-color: white; \n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"QCheckBox#checkBox_3::indicator:unchecked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/unchecked.svg\"); \n"
"}\n"
"\n"
"QCheckBox#checkBox_3::indicator:checked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/checked.svg\"); \n"
"}\n"
"")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setStyleSheet("QCheckBox#checkBox_4{\n"
"    background-color: rgb(255, 204, 255); \n"
"    color: black;                       \n"
"    font: normal 17pt \"Arial Narrow\";   \n"
"}\n"
"\n"
"QCheckBox#checkBox_4::indicator {\n"
"background-color: white; \n"
"    width: 40px; \n"
"    height: 40px; \n"
"}\n"
"\n"
"QCheckBox#checkBox_4::indicator:unchecked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/unchecked.svg\"); \n"
"}\n"
"\n"
"QCheckBox#checkBox_4::indicator:checked {\n"
"    image: url(\"C:/Users/Lipika Dudeja/Downloads/checked.svg\"); \n"
"}")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 730, 751, 121))
        self.textBrowser_2.setStyleSheet("QTextBrowser#textBrowser{\n"
" background-color: white;\n"
"}\n"
"\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 590, 701, 121))
        self.textBrowser_3.setStyleSheet("QTextBrowser#textBrowser_3{\n"
" background-color: white;\n"
"}\n"
"\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 780, 781, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Number_label.setText(_translate("MainWindow", " 1"))
        self.text.setText(_translate("MainWindow", "Scale the Stresses and Modify the Temperature      "))
        self.pushButton_5.setText(_translate("MainWindow", "Submit"))
        self.text_11.setText(_translate("MainWindow", "Multiplier"))
        self.text_12.setText(_translate("MainWindow", "Stress"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.text_4.setText(_translate("MainWindow", "TMF Input file (Required for TMF)"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.text_10.setText(_translate("MainWindow", "Adder"))
        self.text_3.setText(_translate("MainWindow", "Global xml file"))
        self.text_7.setText(_translate("MainWindow", "Stress"))
        self.text_2.setText(_translate("MainWindow", "Local xml file"))
        self.text_14.setText(_translate("MainWindow", "Adder"))
        self.text_13.setText(_translate("MainWindow", "Temp"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.text_6.setText(_translate("MainWindow", "Merge Local xml into Global xml"))
        self.text_9.setText(_translate("MainWindow", "Temp"))
        self.text_8.setText(_translate("MainWindow", "Multiplier"))
        self.text_16.setText(_translate("MainWindow", "Local xml + Global xml & Run TMF"))
        self.pushButton_6.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.Number_label_2.setText(_translate("MainWindow", "2"))
        self.text_5.setText(_translate("MainWindow", "Convert xml file from M_MPa Unit "))
        self.label.setText(_translate("MainWindow", "System to mm_MPa Unit System"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.text_15.setText(_translate("MainWindow", "xml file in M MPa Unit"))
        self.label_2.setText(_translate("MainWindow", "Nodal coordinates scaled by 1.0E3, Nodal Stresses scaled by 1.0E-6"))
        self.label_3.setText(_translate("MainWindow", "Select the box if the given xml file has :"))
        self.checkBox_1.setText(_translate("MainWindow", "Nodal Temperature"))
        self.checkBox_2.setText(_translate("MainWindow", "Nodal Coordinates"))
        self.checkBox_3.setText(_translate("MainWindow", "Element Connectivities"))
        self.checkBox_4.setText(_translate("MainWindow", "Nodal Stresses"))

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QFileDialog, QTextBrowser, QWidget, QProgressBar
from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt

# Add the AddnRefresh method to QTextBrowser
def AddnRefresh(self, content):
    self.append(content)
    self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

QTextBrowser.AddnRefresh = AddnRefresh

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("gui_2.ui", self)

        # Define our widgets
        self.line_edit_1 = self.findChild(QLineEdit, "lineEdit_8")
        self.line_edit_2 = self.findChild(QLineEdit, "lineEdit_2")
        self.line_edit_3 = self.findChild(QLineEdit, "lineEdit_3")
        self.line_edit_4 = self.findChild(QLineEdit, "lineEdit_9")

        # Connect each browse button to a common method
        self.pushButton_1 = self.findChild(QPushButton, "pushButton")
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")

        self.pushButton_1.clicked.connect(lambda: self.browse_file(self.line_edit_1))
        self.pushButton_2.clicked.connect(lambda: self.browse_file(self.line_edit_2))
        self.pushButton_3.clicked.connect(lambda: self.browse_file(self.line_edit_3))
        self.pushButton_4.clicked.connect(lambda: self.browse_file(self.line_edit_4))

        # Find the text browser
        self.text_browser = self.findChild(QTextBrowser, "textBrowser")

        # Add initial long text to test scrollbar
        self.text_browser.AddnRefresh("Initial long log entry \n" * 50)

        # Find the submit buttons
        self.submit_button_1 = self.findChild(QPushButton, "pushButton_5")
        self.submit_button_2 = self.findChild(QPushButton, "pushButton_6")

        # Set the initial style and disable the submit buttons
        self.submit_button_1.setEnabled(False)
        self.submit_button_1.setStyleSheet("background-color: gray; color: white;")
        self.submit_button_2.setEnabled(False)
        self.submit_button_2.setStyleSheet("background-color: gray; color: white;")

        # Connect textChanged signals to the check_files method
        self.line_edit_1.textChanged.connect(self.check_files)
        self.line_edit_2.textChanged.connect(self.check_files)
        self.line_edit_3.textChanged.connect(self.check_files)
        self.line_edit_4.textChanged.connect(self.check_files)

        # Initialize the progress bar
        self.progress_bar = self.findChild(QProgressBar, "progressBar")
        self.progress_bar.setMaximum(100)
        self.progress_bar.hide()

        # Show the app
        self.show()

    def browse_file(self, line_edit):
        # Show blur effect
        self.show_blur_effect()

        # Open File Dialog
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "L:\\Internship", "All Files (*)")

        # Hide blur effect
        self.hide_blur_effect()

        # Output filename to specified QLineEdit
        if fname:
            line_edit.setText(fname)
            self.log_action(f"Selected file for {line_edit.objectName()}: {fname}")
            # Show and reset progress bar, then start upload simulation
            self.progress_bar.show()
            self.progress_bar.setValue(0)
            self.upload_file(fname)

    def upload_file(self, fname):
        self.simulate_upload(0, fname)

    def simulate_upload(self, value, fname):
        if value < 100:
            value += 10
            self.progress_bar.setValue(value)
            QTimer.singleShot(200, lambda: self.simulate_upload(value, fname))
        else:
            self.progress_bar.hide()
            self.log_action(f"Upload complete for file: {fname}")

    def show_blur_effect(self):
        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.overlay.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.overlay.show()

    def hide_blur_effect(self):
        self.overlay.hide()

    def log_action(self, message):
        self.text_browser.AddnRefresh(message)
        print(message)  # Add debug print to log actions

    def check_files(self):
        # Check and log the state of each line edit
        print(f"line_edit_1: {self.line_edit_1.text()}")
        print(f"line_edit_2: {self.line_edit_2.text()}")
        print(f"line_edit_3: {self.line_edit_3.text()}")
        print(f"line_edit_4: {self.line_edit_4.text()}")

        # Check if all line edits have text for the first submit button
        if self.line_edit_1.text() and self.line_edit_2.text() :
            self.submit_button_1.setEnabled(True)
            self.submit_button_1.setStyleSheet("background-color: rgb(167, 255, 200); color: rgb(148, 0, 111);")
        else:
            self.submit_button_1.setEnabled(False)
            self.submit_button_1.setStyleSheet("background-color: gray; color: white;")

        # Check if all line edits have text for the second submit button
        if self.line_edit_1.text() and self.line_edit_2.text() and self.line_edit_3.text():
            self.submit_button_2.setEnabled(True)
            self.submit_button_2.setStyleSheet("background-color: rgb(167, 255, 200); color: rgb(148, 0, 111);")
        else:
            self.submit_button_2.setEnabled(False)
            self.submit_button_2.setStyleSheet("background-color: gray; color: white;")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())
