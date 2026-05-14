# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PTLMetaToolkitKcPUkr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(341, 602)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionGetScreen = QAction(MainWindow)
        self.actionGetScreen.setObjectName(u"actionGetScreen")
        self.actionGetAudio = QAction(MainWindow)
        self.actionGetAudio.setObjectName(u"actionGetAudio")
        self.actionGetMeta = QAction(MainWindow)
        self.actionGetMeta.setObjectName(u"actionGetMeta")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 321, 561))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(9, 9, 301, 511))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.textEdit = QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEdit)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.textEdit_2 = QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_2)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_4)

        self.textEdit_3 = QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.textEdit_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget_2 = QWidget(self.tab_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(9, 9, 301, 511))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.textEdit_4 = QTextEdit(self.formLayoutWidget_2)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.textEdit_4)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayoutWidget_3 = QWidget(self.tab_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(9, 10, 301, 511))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_13 = QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_14 = QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_15 = QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_16 = QLabel(self.formLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)

        self.textEdit_5 = QTextEdit(self.formLayoutWidget_3)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.textEdit_5)

        self.label_17 = QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.textEdit_6 = QTextEdit(self.formLayoutWidget_3)
        self.textEdit_6.setObjectName(u"textEdit_6")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.textEdit_6)

        self.textEdit_7 = QTextEdit(self.formLayoutWidget_3)
        self.textEdit_7.setObjectName(u"textEdit_7")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.textEdit_7)

        self.label_18 = QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_19)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 341, 22))
        self.menuSoubor = QMenu(self.menubar)
        self.menuSoubor.setObjectName(u"menuSoubor")
        self.menuVideo = QMenu(self.menubar)
        self.menuVideo.setObjectName(u"menuVideo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSoubor.menuAction())
        self.menubar.addAction(self.menuVideo.menuAction())
        self.menuSoubor.addAction(self.actionOpen)
        self.menuSoubor.addAction(self.actionSave)
        self.menuSoubor.addAction(self.actionSave_as)
        self.menuSoubor.addAction(self.actionClose)
        self.menuVideo.addAction(self.actionGetScreen)
        self.menuVideo.addAction(self.actionGetAudio)
        self.menuVideo.addAction(self.actionGetMeta)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PTL Meta Toolkit", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save..", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as..", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionGetScreen.setText(QCoreApplication.translate("MainWindow", u"GetScreen", None))
        self.actionGetAudio.setText(QCoreApplication.translate("MainWindow", u"GetAudio", None))
        self.actionGetMeta.setText(QCoreApplication.translate("MainWindow", u"GetMeta", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"AltNme", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Meta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Meta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Video", None))
        self.menuSoubor.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuVideo.setTitle(QCoreApplication.translate("MainWindow", u"Video", None))
    # retranslateUi

