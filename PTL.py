#!/usr/bin/python3
#
# PTL Metadata toolkit
#

import subprocess,sys,os

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
	QVBoxLayout,
	QGridLayout,
	QGroupBox,
	QPushButton,
	QLineEdit,
	QTextEdit,
	QLabel
)

BASE = '/home/user/Desktop/project'

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

		self.groupVideoWidget = QGroupBox()
		self.groupVideoLayout = QGridLayout(self.groupVideoWidget)

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
		self.artist_icon_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.FieldRole, self.artist_icon_text)
		self.artist_picture = QLabel("Picture", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.LabelRole, self.artist_picture)
		self.artist_picture_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.FieldRole, self.artist_picture_text)
		self.artist_video = QLabel("Video", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.LabelRole, self.artist_video)
		self.artist_video_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.FieldRole, self.artist_video_text)
		self.artist_location = QLabel("Location", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.LabelRole, self.artist_location)
		self.artist_location_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.FieldRole, self.artist_location_text)
		self.artist_group = QLabel("Group", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(8, QFormLayout.ItemRole.LabelRole, self.artist_group)
		self.artist_group_text = QLineEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(8, QFormLayout.ItemRole.FieldRole, self.artist_group_text)
		self.artist_meta = QLabel("Meta", self.formLayoutWidget_1)
		self.formLayout_1.setWidget(9, QFormLayout.ItemRole.LabelRole, self.artist_meta)
		self.artist_meta_text = QTextEdit(self.formLayoutWidget_1)
		self.formLayout_1.setWidget(9, QFormLayout.ItemRole.FieldRole, self.artist_meta_text)

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

		self.formLayout_3.addRow(self.groupVideoWidget)

		self.video_GetMetaButton = QPushButton("Get Metadata")
		self.groupVideoLayout.addWidget(self.video_GetMetaButton, 0, 0, 1, 5)
		self.video_GetScreenshot = QLabel("Start")
		self.video_GetScreenshotEdit = QLineEdit()
		self.video_GetScreenshotButton = QPushButton("Get Screen")
		self.groupVideoLayout.addWidget(self.video_GetScreenshot , 1, 0)
		self.groupVideoLayout.addWidget(self.video_GetScreenshotEdit , 1, 1, 1, 3)
		self.groupVideoLayout.addWidget(self.video_GetScreenshotButton , 1, 4)
		self.video_GetAudioStart = QLabel("Start")
		self.video_GetAudioStartEdit = QLineEdit()
		self.video_GetAudioEnd = QLabel("End")
		self.video_GetAudioEndEdit = QLineEdit()
		self.video_GetAudioButton = QPushButton("Get Audio")
		self.groupVideoLayout.addWidget(self.video_GetAudioStart, 2, 0)
		self.groupVideoLayout.addWidget(self.video_GetAudioStartEdit , 2, 1)
		self.groupVideoLayout.addWidget(self.video_GetAudioEnd, 2, 2)
		self.groupVideoLayout.addWidget(self.video_GetAudioEndEdit , 2, 3)
		self.groupVideoLayout.addWidget(self.video_GetAudioButton , 2, 4)

		self.video_GetMetaButton.clicked.connect(self.get_meta)
		self.video_GetScreenshotButton.clicked.connect(self.get_screen)
		self.video_GetAudioButton.clicked.connect(self.get_audio)


	def file_find(self, name):
		for root, dirs, files in os.walk(BASE + '/VIDEO/'):
			if name in files:
				return os.path.join(root, name)

	def get_metaDialog(self, fn, text):
		self.dlg = QDialog()
		self.dlg.setWindowTitle(fn + ' - Metadata')
		layout = QVBoxLayout() 
		message = QLabel(text)		
		layout.addWidget(message)
		self.dlg.setLayout(layout)
		self.dlg.show()

	def get_meta(self):
		if self.video_name_text.text():
			fn = self.file_find(self.video_name_text.text())
			if fn:
				FFPROBE_METADATA = ['ffprobe', '-hide_banner', fn]
				try:
					proc = subprocess.run(FFPROBE_METADATA, text=True, capture_output=True)
					self.get_metaDialog(self.video_name_text.text(), proc.stderr)
				except:
					print('[error] ffmpeg meta: ' + fn)

	def get_screen(self):
		if self.video_name_text.text():
			fn = self.file_find(self.video_name_text.text())
			frame = self.video_GetScreenshotEdit.text()
			out = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn)) + self.video_name_text.text() + '.jpg'
		
			if fn and frame:
				FFMPEG_SCREEN = ['ffmpeg','-v','error','-y','-i',fn,'-ss',frame,'-frames:v','1',out]
				try:
					proc = subprocess.run(FFMPEG_SCREEN)
				except:
					print('[error] ffmpeg screen: ' + fn)

	def get_audio(self):
		if self.video_name_text.text():
			fn = self.file_find(self.video_name_text.text())
			frame_start = self.video_GetAudioStartEdit.text()
			frame_stop = self.video_GetAudioEndEdit.text()
			out = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn)) + self.video_name_text.text() + '.mp3'

			if fn and frame_start and frame_stop:
				FFMPEG_AUDIO = ['ffmpeg','-v','error','-y','-i',fn,'-ss',frame_start,'-t',frame_stop,out]
				try:
					proc = subprocess.run(FFMPEG_AUDIO)
				except:
					print('[error] ffmpeg audio: ' + fn)

	def file_open(self):
		fn = QFileDialog.getOpenFileName(self, "Open File", BASE + '/YAML/', "MD (*.md)")
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
					if 'nickname' in yml: self.artist_nickname_text.setText(yml['nickname'])
					if 'altname' in yml: self.artist_altname_text.setPlainText("\n".join(yml['altname']))
					if 'name' in yml: self.artist_name_text.setText(yml['name'])
					if 'id' in yml: self.artist_id_text.setText(yml['id'])
					if 'icon' in yml: self.artist_icon_text.setText(yml['icon'])
					if 'picture' in yml: self.artist_picture_text.setText(yml['picture'])
					if 'video' in yml: self.artist_video_text.setPlainText("\n".join(yml['video']))
					if 'location' in yml: self.artist_location_text.setText(yml['location'])
					if 'group' in yml: self.artist_group_text.setText(yml['group'])
					if 'meta' in yml: self.artist_meta_text.setPlainText("\n".join(yml['meta']))
					self.tab.setCurrentIndex(0)
				case "group":
					if 'name' in yml: self.group_name_text.setText(yml['name'])
					if 'artist' in yml: self.group_artist_text.setPlainText("\n".join(yml['artist']))
					if 'location' in yml: self.group_location_text.setText(yml['location'])
					if 'country' in yml: self.group_country_text.setText(yml['country'])
					if 'meta' in yml: self.group_meta_text.setPlainText("\n".join(yml['meta']))
					self.tab.setCurrentIndex(1)
				case "video":
					if 'name' in yml: self.video_name_text.setText(yml['name'])
					if 'screenshot' in yml: self.video_screenshot_text.setText(yml['screenshot'])
					if 'date' in yml: self.video_date_text.setText(yml['date'])
					if 'size' in yml: self.video_size_text.setText(yml['size'])
					if 'duration' in yml: self.video_duration_text.setText(yml['duration'])
					if 'music' in yml: self.video_music_text.setPlainText("\n".join(yml['music']))
					if 'artist' in yml: self.video_artist_text.setPlainText("\n".join(yml['artist']))
					if 'meta' in yml: self.video_meta_text.setPlainText("\n".join(yml['meta']))
					self.tab.setCurrentIndex(2)
	
	def file_save(self):
		fn, fn_base = None, None
		yml = {}
		match self.tab.currentIndex():
			case 0:
				if self.artist_nickname_text.text():
					yml['nickname'] = self.artist_nickname_text.text()
					if self.artist_altname_text.toPlainText(): yml['altname'] = self.artist_altname_text.toPlainText().splitlines()
					if self.artist_name_text.text(): yml['name'] = self.artist_name_text.text()
					if self.artist_id_text.text(): yml['id'] = self.artist_id_text.text()
					if self.artist_icon_text.text(): yml['icon'] = self.artist_icon_text.text()
					if self.artist_picture_text.text(): yml['picture'] = self.artist_picture_text.text()
					if self.artist_video_text.toPlainText(): yml['video'] = self.artist_video_text.toPlainText().splitlines()
					if self.artist_location_text.text(): yml['location'] = self.artist_location_text.text()
					if self.artist_group_text.text(): yml['group'] = self.artist_group_text.text()
					if self.artist_meta_text.toPlainText(): yml['meta'] = self.artist_meta_text.toPlainText().splitlines()
					fn_base = BASE + '/YAML/artist/'
					fn = fn_base + self.artist_nickname_text.text() + '.md'
			case 1:
				if self.group_name_text.text():
					yml['name'] = self.group_name_text.text()
					if self.group_artist_text.toPlainText(): yml['artist'] = self.group_artist_text.toPlainText().splitlines()
					if self.group_location_text.text(): yml['location'] = self.group_location_text.text()
					if self.group_country_text.text(): yml['country'] = self.group_country_text.text()
					if self.group_meta_text.toPlainText(): yml['meta'] = self.group_meta_text.toPlainText().splitlines()
					fn_base = BASE + '/YAML/group/'
					fn = fn_base + self.group_name_text.text() + '.md'

			case 2:
				if self.video_name_text.text():
					yml['name'] = self.video_name_text.text()
					if self.video_screenshot_text.text(): yml['screenshot'] = self.video_screenshot_text.text()
					if self.video_date_text.text(): yml['date'] = self.video_date_text.text()
					if self.video_size_text.text(): yml['size'] = self.video_size_text.text()
					if self.video_duration_text.text(): yml['duration'] = self.video_duration_text.text()
					if self.video_music_text.toPlainText(): yml['music'] = self.video_music_text.toPlainText().splitlines()
					if self.video_artist_text.toPlainText(): yml['artist'] = self.video_artist_text.toPlainText().splitlines()
					if self.video_meta_text.toPlainText(): yml['meta'] = self.video_meta_text.toPlainText().splitlines()
					fn_base = BASE + '/YAML/video/'
					fn = fn_base + self.video_name_text.text() + '.md'

		if not os.path.isfile(fn):
			fn_tup = QFileDialog.getSaveFileName(self, "Save File", fn_base, "MD (*.md)")
			if os.path.splitext(fn[0]) != 'yml': fn = fn_tup[0] + '.md'

		with open(fn, 'w') as f:
        		f.write(safe_dump(yml, sort_keys=False, explicit_start=True, explicit_end=True))

# MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
