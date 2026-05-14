#!/usr/bin/python3
	
import sys

from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
	QApplication,
	QWidget,
	QTabWidget,
	QFormLayout,
	QMainWindow,
	QMenuBar,
	QMenu,
	QLineEdit,
	QTextEdit,
	QLabel
)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		## WINDOW

		self.setWindowTitle("PTL Metadata toolkit")
		self.setFixedSize(QSize(341,602))

		## CONTAINER

		self.container = QWidget()
		self.setCentralWidget(self.container)

		## MENU

		self.menubar = QMenuBar()
		self.menubar.setGeometry(QRect(0, 0, 341, 22))
		self.menuSoubor = QMenu(self.menubar)
		self.menuSoubor.setTitle("Soubor")
		self.menubar.addMenu(self.menuSoubor)

		self.menuVideo = QMenu(self.menubar)
		self.menuVideo.setTitle("Video")
		self.menubar.addMenu(self.menuVideo)

		self.actionOpen = QAction()
		self.actionOpen.setText("Open")
		self.menuSoubor.addAction(self.actionOpen)

		self.setMenuBar(self.menubar)

		## TAB

		self.tab = QTabWidget(self.container)
		self.tab.setGeometry(QRect(10, 10, 321, 561))
		self.tab_1 = QWidget()
		self.tab.addTab(self.tab_1, "Artist")
		self.tab_2 = QWidget()
		self.tab.addTab(self.tab_2, "Group")
		self.tab_3 = QWidget()
		self.tab.addTab(self.tab_3, "Video")

		## LAYOUT

		self.formLayoutWidget = QWidget(self.tab_1)
		self.formLayoutWidget.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout = QFormLayout(self.formLayoutWidget)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayoutWidget_2 = QWidget(self.tab_2)
		self.formLayoutWidget_2.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
		self.formLayout_2.setContentsMargins(0, 0, 0, 0)
		self.formLayoutWidget_3 = QWidget(self.tab_3)
		self.formLayoutWidget_3.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
		self.formLayout_3.setContentsMargins(0, 0, 0, 0)

		## TAB 1

		self.label = QLabel(self.formLayoutWidget)
		self.label.setText("Nickname")
		self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)
		self.lineEdit = QLineEdit(self.formLayoutWidget)
		self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

		## TAB 2

		## TAB 3

## MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
