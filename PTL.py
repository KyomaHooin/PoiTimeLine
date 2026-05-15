#!/usr/bin/python3
#
# PTL Metadata toolkit
#

import sys,os.path

from yaml import safe_dump,safe_load

from PyQt6.QtCore import QSize, QRect
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
	QApplication,
	QMainWindow,
	QWidget,
	QMenuBar,
	QMenu,
	QFileDialog,
	QDialog,
	QTabWidget,
	QFormLayout,
	QLineEdit,
	QTextEdit,
	QLabel
)

BASE='/home/user/Desktop/project/YAML/'#[artist|group|video[/assets/]]

TPL_ARTIST={
	'nickname':None,
	'altname':None,
	'name':None,
	'id':None,
	'icon':None,
	'location':None,
	'group':None,
	'meta':None
}

TPL_GROUP={
	'name':None,
	'artist':None,
	'location':None,
	'coutry':None,
	'meta':None,
}

TPL_VIDEO={
	'name':None,
	'screenshot':None,
	'date':None,
	'size':None,
	'duration':None,
	'music':None,
	'artist':None,
	'meta':None,
}

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# WINDOW
		self.setWindowTitle("PTL Metadata toolkit")
		self.setFixedSize(QSize(341,602))
		self.move(750,200)

		# CONTAINER
		self.container = QWidget()
		self.setCentralWidget(self.container)

		# MENU
		self.menubar = QMenuBar()
		self.menubar.setGeometry(QRect(0, 0, 341, 22))

		self.menuSoubor = QMenu(self.menubar)
		self.menuSoubor.setTitle("File")
		self.menubar.addMenu(self.menuSoubor)

		self.actionOpen = QAction("Open")
		self.actionOpen.setShortcut(QKeySequence("Ctrl+o"))
		self.actionOpen.triggered.connect(self.file_open)
		self.menuSoubor.addAction(self.actionOpen)
		self.actionSave = QAction("Save..")
		self.actionSave.setShortcut(QKeySequence("Ctrl+s"))
		self.actionSave.triggered.connect(self.file_save)
		self.menuSoubor.addAction(self.actionSave)
		self.actionSaveAs = QAction("SaveAs..")
		self.actionSaveAs.setShortcut(QKeySequence("Shift+Ctrl+s"))
		self.actionSaveAs.triggered.connect(self.file_save)
		self.menuSoubor.addAction(self.actionSaveAs)
		self.actionClose = QAction("Close")
		self.actionClose.setShortcut(QKeySequence("Ctrl+q"))
		self.actionClose.triggered.connect(self.close)
		self.menuSoubor.addAction(self.actionClose)

		self.menuVideo = QMenu(self.menubar)
		self.menuVideo.setTitle("Video")
		self.menubar.addMenu(self.menuVideo)

		self.actionGetMeta = QAction("GetMeta..")
		self.menuVideo.addAction(self.actionGetMeta)
		self.actionGetScreen = QAction("GetScreen..")
		self.menuVideo.addAction(self.actionGetScreen)
		self.actionGetAudio = QAction("GetAudio..")
		self.menuVideo.addAction(self.actionGetAudio)

		self.setMenuBar(self.menubar)
		
		# TAB
		self.tab = QTabWidget(self.container)
		self.tab.setGeometry(QRect(10, 10, 321, 561))
		self.tab_1 = QWidget()
		self.tab.addTab(self.tab_1, "Artist")
		self.tab_2 = QWidget()
		self.tab.addTab(self.tab_2, "Group")
		self.tab_3 = QWidget()
		self.tab.addTab(self.tab_3, "Video")

		# TAB LAYOUT
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

		# TAB 1
		self.artist_nickname = QLabel("Nickname", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.artist_nickname)
		self.artist_nickname_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.artist_nickname_text)
		self.artist_altname = QLabel("Altname", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.artist_altname)
		self.artist_altname_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.artist_altname_text)
		self.artist_name = QLabel("Name", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(2, QFormLayout.ItemRole.LabelRole, self.artist_name)
		self.artist_name_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(2, QFormLayout.ItemRole.FieldRole, self.artist_name_text)
		self.artist_id = QLabel("ID", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.LabelRole, self.artist_id)
		self.artist_id_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.FieldRole, self.artist_id_text)
		self.artist_icon = QLabel("Icon", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.LabelRole, self.artist_icon)
		self.artist_icon_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.FieldRole, self.artist_icon_text)
		self.artist_location = QLabel("Location", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.LabelRole, self.artist_location)
		self.artist_location_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.FieldRole, self.artist_location_text)
		self.artist_group = QLabel("Group", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.LabelRole, self.artist_group)
		self.artist_group_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.FieldRole, self.artist_group_text)
		self.artist_meta = QLabel("Meta", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.LabelRole, self.artist_meta)
		self.artist_meta_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.FieldRole, self.artist_meta_text)

		# TAB 2
		self.group_name = QLabel("Name", self.formLayoutWidget_2)
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.group_name)
		self.group_name_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.group_name_text)
		self.group_artist = QLabel("Artist", self.formLayoutWidget_2)
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.group_artist)
		self.group_artist_text = QTextEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.group_artist_text)
		self.group_location = QLabel("Location", self.formLayoutWidget_2)
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.group_location)
		self.group_location_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.group_location_text)
		self.group_country = QLabel("Country", self.formLayoutWidget_2)
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.group_country)
		self.group_country_text = QLineEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.group_country_text)
		self.group_meta = QLabel("Meta", self.formLayoutWidget_2)
		self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.group_meta)
		self.group_meta_text = QTextEdit(self.formLayoutWidget_2)
		self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.group_meta_text)

		# TAB 3
		self.video_name = QLabel("Name", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.video_name)
		self.video_name_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.video_name_text)
		self.video_screenshot = QLabel("Screenshot", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.video_screenshot)
		self.video_screenshot_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.video_screenshot_text)
		self.video_date = QLabel("Date", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.video_date)
		self.video_date_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.video_date_text)
		self.video_size = QLabel("Size", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.video_size)
		self.video_size_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.video_size_text)
		self.video_duration = QLabel("Duration", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.video_duration)
		self.video_duration_text = QLineEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.video_duration_text)
		self.video_music = QLabel("Music", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.video_music)
		self.video_music_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.video_music_text)
		self.video_artist = QLabel("Artist", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.LabelRole, self.video_artist)
		self.video_artist_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.FieldRole, self.video_artist_text)
		self.video_meta = QLabel("Meta", self.formLayoutWidget_3)
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.LabelRole, self.video_meta)
		self.video_meta_text = QTextEdit(self.formLayoutWidget_3)
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.FieldRole, self.video_meta_text)

	def file_open(self):
		fn = QFileDialog.getOpenFileName(self, "Open File", BASE, "YML (*.yml)")
		yml = None
		if os.path.isfile(fn[0]):
			with open(fn[0], 'r') as stream:
				try:
					yml = safe_load(stream)
				except:
					print("[error] Failed to parse: " + fn[0])
					return

		if yml:
			match os.path.basename(os.path.dirname(fn[0])):
				case "artist":
					self.artist_nickname_text.text(TPL.nickname)
					self.tab.setCurrentIndex(0)
				case "group":
					self.tab.setCurrentIndex(1)
				case "video":
					self.tab.setCurrentIndex(2)
	
	def file_save(self):
		fn = None
		match self.tab.currentIndex():
			case 0:
				if self.artist_nickname_text.text():
					fn = BASE + 'artist/' + self.artist_nickname_text.text() + '.yml'
			case 1:
				if self.group_name_text.text():
					fn = BASE + 'group/' + self.group_name_text.text() + '.yml'
			case 2:
				if self.video_name_text.text():
					fn = BASE + 'video/' + self.video_name_text.text() + '.yml'

		if not os.path.isfile(fn):
			fn_tup = QFileDialog.getSaveFileName(self, "Save File", BASE, "YML (*.yml)")
			if os.path.splitext(fn[0]) != 'yml': fn = fn_tup[0] + '.yml'

		with open(fn, 'w') as f:
        		f.write(safe_dump(
				TPL_ARTIST,
				sort_keys=False,
				explicit_start=True,
				explicit_end=True
			))

## MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
