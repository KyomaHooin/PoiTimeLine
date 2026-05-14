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

		self.actionOpen = QAction()
		self.actionOpen.setText("Open")
		self.menuSoubor.addAction(self.actionOpen)
		self.actionSave = QAction()
		self.actionSave.setText("Save..")
		self.menuSoubor.addAction(self.actionSave)
		self.actionSaveAs = QAction()
		self.actionSaveAs.setText("SaveAs..")
		self.menuSoubor.addAction(self.actionSaveAs)
		self.actionClose = QAction()
		self.actionClose.setText("Close")
		self.menuSoubor.addAction(self.actionClose)

		self.menuVideo = QMenu(self.menubar)
		self.menuVideo.setTitle("Video")
		self.menubar.addMenu(self.menuVideo)

		self.actionGetMeta = QAction()
		self.actionGetMeta.setText("GetMeta..")
		self.menuVideo.addAction(self.actionGetMeta)
		self.actionGetScreen = QAction()
		self.actionGetScreen.setText("GetScreen..")
		self.menuVideo.addAction(self.actionGetScreen)
		self.actionGetAudio = QAction()
		self.actionGetAudio.setText("GetAudio..")
		self.menuVideo.addAction(self.actionGetAudio)

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

		## TAB LAYOUT

		self.formLayoutWidget_1 = QWidget(self.tab_1)
		self.formLayoutWidget_1.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout_1 = QFormLayout(self.formLayoutWidget_1)
		self.formLayout_1.setContentsMargins(0, 0, 0, 0)

		self.formLayoutWidget_2 = QWidget(self.tab_2)
		self.formLayoutWidget_2.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
		self.formLayout_2.setContentsMargins(0, 0, 0, 0)

		self.formLayoutWidget_3 = QWidget(self.tab_3)
		self.formLayoutWidget_3.setGeometry(QRect(9, 9, 301, 511))
		self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
		self.formLayout_3.setContentsMargins(0, 0, 0, 0)

		## TAB 1

		self.artist_nickname = QLabel(self.formLayoutWidget_1)
		self.artist_nickname.setText("Nickname")
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.artist_nickname)
		self.artist_nickname_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.artist_nickname_text)

		self.artist_altname = QLabel(self.formLayoutWidget_1)
		self.artist_altname.setText("Altname")
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.artist_altname)
		self.artist_altname_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.artist_altname_text)

		self.artist_id = QLabel(self.formLayoutWidget_1)
		self.artist_id.setText("ID")
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.LabelRole, self.artist_id)
		self.artist_id_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.FieldRole, self.artist_id_text)

		self.artist_icon = QLabel(self.formLayoutWidget_1)
		self.artist_icon.setText("Icon")
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.LabelRole, self.artist_icon)
		self.artist_icon_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.FieldRole, self.artist_icon_text)

		self.artist_location = QLabel(self.formLayoutWidget_1)
		self.artist_location.setText("Location")
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.LabelRole, self.artist_location)
		self.artist_location_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.FieldRole, self.artist_location_text)

		self.artist_group = QLabel(self.formLayoutWidget_1)
		self.artist_group.setText("Group")
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.LabelRole, self.artist_group)
		self.artist_group_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.FieldRole, self.artist_group_text)

		self.artist_meta = QLabel(self.formLayoutWidget_1)
		self.artist_meta.setText("Meta")
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.LabelRole, self.artist_meta)
		self.artist_meta_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.FieldRole, self.artist_meta_text)

		## TAB 2

		self.group_name = QLabel(self.formLayoutWidget_2)
		self.group_name.setText("Name")
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.group_name)
		self.group_name_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.group_name_text)

		self.group_artist = QLabel(self.formLayoutWidget_2)
		self.group_artist.setText("Artist")
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.group_artist)
		self.group_artist_text = QTextEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.group_artist_text)

		self.group_location = QLabel(self.formLayoutWidget_2)
		self.group_location.setText("Location")
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.group_location)
		self.group_location_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.group_location_text)

		self.group_country = QLabel(self.formLayoutWidget_2)
		self.group_country.setText("Country")
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.group_country)
		self.group_country_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.group_country_text)

		## TAB 3

		self.video_name = QLabel(self.formLayoutWidget_3)
		self.video_name.setText("Name")
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.video_name)
		self.video_name_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.video_name_text)

		self.video_screenshot = QLabel(self.formLayoutWidget_3)
		self.video_screenshot.setText("Screenshot")
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.video_screenshot)
		self.video_screenshot_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.video_screenshot_text)

		self.video_date = QLabel(self.formLayoutWidget_3)
		self.video_date.setText("Date")
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.video_date)
		self.video_date_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.video_date_text)

		self.video_size = QLabel(self.formLayoutWidget_3)
		self.video_size.setText("Size")
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.video_size)
		self.video_size_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.video_size_text)

		self.video_duration = QLabel(self.formLayoutWidget_3)
		self.video_duration.setText("Duration")
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.video_duration)
		self.video_duration_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.video_duration_text)

		self.video_music = QLabel(self.formLayoutWidget_3)
		self.video_music.setText("Music")
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.video_music)
		self.video_music_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.video_music_text)

		self.video_artist = QLabel(self.formLayoutWidget_3)
		self.video_artist.setText("Artist")
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.LabelRole, self.video_artist)
		self.video_artist_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.FieldRole, self.video_artist_text)

		self.video_meta = QLabel(self.formLayoutWidget_3)
		self.video_meta.setText("Meta")
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.LabelRole, self.video_meta)
		self.video_meta_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.FieldRole, self.video_meta_text)

## MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
