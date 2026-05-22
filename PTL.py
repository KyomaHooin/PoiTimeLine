#!/usr/bin/python3
#
# PTL Metadata toolkit
#

import subprocess,vlc,sys,os

from yaml import safe_dump,safe_load

from PyQt6.QtCore import QSize, QRect, QTimer, Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
	QApplication,
	QMainWindow,
	QWidget,
	QFrame,
	QMenuBar,
	QMenu,
	QFileDialog,
	QDialog,
	QTabWidget,
	QFormLayout,
	QVBoxLayout,
	QHBoxLayout,
	QGridLayout,
	QGroupBox,
	QPushButton,
	QLineEdit,
	QTextEdit,
	QSlider,
	QLabel,
)

BASE = '/home/user/Desktop/project'

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# VLC

		self.vlc_instance = vlc.Instance()
		self.player = self.vlc_instance.media_player_new()
		self.player.audio_set_volume(50)

		self.video_is_paused = False
		self.video_slider_is_pressed = False

		# WINDOW

		self.setWindowTitle("PTL Metadata toolkit")
		self.setFixedSize(QSize(1400,750))
		self.move(250,150)

		# CONTAINER

		self.container = QWidget()
		self.setCentralWidget(self.container)

		# TOP LAYOUT

		self.top_layout = QGridLayout(self.container)
		self.top_layout.setColumnStretch(0,1)
		self.top_layout.setColumnStretch(1,3)

		# MENU

		self.menubar = QMenuBar()

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
		self.actionClose.triggered.connect(self.PTL_close)
		self.menuSoubor.addAction(self.actionClose)

		self.setMenuBar(self.menubar)

		# FRAME

		self.videoWidget = QWidget()	
		self.video_layout = QVBoxLayout(self.videoWidget)
		
		self.videoframe = QFrame()
		self.videoframe.setStyleSheet("background: black;")
		self.video_layout.addWidget(self.videoframe, 1)

		# VIDEO CONTROL

		self.video_control_layout = QHBoxLayout()
		self.video_layout.addLayout(self.video_control_layout)

		self.video_pause_play_button = QPushButton("Pause")
		self.video_pause_play_button.clicked.connect(self.video_play_pause)
		self.video_control_layout.addWidget(self.video_pause_play_button)
		self.video_prev_button = QPushButton("Prev")
		self.video_prev_button.clicked.connect(self.video_prev)
		self.video_control_layout.addWidget(self.video_prev_button)
		self.video_next_button = QPushButton("Next")
		self.video_next_button.clicked.connect(self.video_next)
		self.video_control_layout.addWidget(self.video_next_button)
		self.video_screen_button = QPushButton("Screen")
		self.video_screen_button.clicked.connect(self.video_screen)
		self.video_control_layout.addWidget(self.video_screen_button)

		self.video_progress = QSlider(Qt.Orientation.Horizontal)
		self.video_progress.setRange(0, 1000)
		self.video_progress.sliderPressed.connect(self.slider_press)
		self.video_progress.sliderReleased.connect(self.slider_release)
		self.video_control_layout.addWidget(self.video_progress)

		self.video_play_duration_text = QLabel('00:00:00')
		self.video_control_layout.addWidget(self.video_play_duration_text)

		# TIMER

		self.timer = QTimer(self)
		self.timer.setInterval(100)# millis
		self.timer.timeout.connect(self.gui_update)

		# TAB

		self.tab = QTabWidget(self.container)
		self.tab_1 = QWidget()
		self.tab.addTab(self.tab_1, "Artist")
		self.tab_2 = QWidget()
		self.tab.addTab(self.tab_2, "Group")
		self.tab_3 = QWidget()
		self.tab.addTab(self.tab_3, "Video")

		# TAB LAYOUT

		self.formLayout_1 = QFormLayout(self.tab_1)
		self.formLayout_2 = QFormLayout(self.tab_2)
		self.formLayout_3 = QFormLayout(self.tab_3)

		self.groupVideoWidget = QGroupBox()
		self.groupVideoLayout = QGridLayout(self.groupVideoWidget)

		# TAB 1

		self.artist_nickname = QLabel("Nickname")
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.artist_nickname)
		self.artist_nickname_text = QLineEdit()
		self.formLayout_1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.artist_nickname_text)
		self.artist_altname = QLabel("Altname")
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.artist_altname)
		self.artist_altname_text = QTextEdit()
		self.formLayout_1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.artist_altname_text)
		self.artist_name = QLabel("Name")
		self.formLayout_1.setWidget(2, QFormLayout.ItemRole.LabelRole, self.artist_name)
		self.artist_name_text = QLineEdit()
		self.formLayout_1.setWidget(2, QFormLayout.ItemRole.FieldRole, self.artist_name_text)
		self.artist_id = QLabel("ID")
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.LabelRole, self.artist_id)
		self.artist_id_text = QLineEdit()
		self.formLayout_1.setWidget(3, QFormLayout.ItemRole.FieldRole, self.artist_id_text)
		self.artist_icon = QLabel("Icon")
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.LabelRole, self.artist_icon)
		self.artist_icon_text = QLineEdit()
		self.formLayout_1.setWidget(4, QFormLayout.ItemRole.FieldRole, self.artist_icon_text)
		self.artist_picture = QLabel("Picture")
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.LabelRole, self.artist_picture)
		self.artist_picture_text = QLineEdit()
		self.formLayout_1.setWidget(5, QFormLayout.ItemRole.FieldRole, self.artist_picture_text)
		self.artist_video = QLabel("Video")
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.LabelRole, self.artist_video)
		self.artist_video_text = QTextEdit()
		self.formLayout_1.setWidget(6, QFormLayout.ItemRole.FieldRole, self.artist_video_text)
		self.artist_location = QLabel("Location")
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.LabelRole, self.artist_location)
		self.artist_location_text = QLineEdit()
		self.formLayout_1.setWidget(7, QFormLayout.ItemRole.FieldRole, self.artist_location_text)
		self.artist_group = QLabel("Group")
		self.formLayout_1.setWidget(8, QFormLayout.ItemRole.LabelRole, self.artist_group)
		self.artist_group_text = QLineEdit()
		self.formLayout_1.setWidget(8, QFormLayout.ItemRole.FieldRole, self.artist_group_text)
		self.artist_meta = QLabel("Meta")
		self.formLayout_1.setWidget(9, QFormLayout.ItemRole.LabelRole, self.artist_meta)
		self.artist_meta_text = QTextEdit()
		self.formLayout_1.setWidget(9, QFormLayout.ItemRole.FieldRole, self.artist_meta_text)
		self.cleanButton_1 = QPushButton("Clear")
		self.cleanButton_1.clicked.connect(self.clean_tab)
		self.formLayout_1.addRow(self.cleanButton_1)

		# TAB 2

		self.group_name = QLabel("Name")
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.group_name)
		self.group_name_text = QLineEdit()
		self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.group_name_text)
		self.group_artist = QLabel("Artist")
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.group_artist)
		self.group_artist_text = QTextEdit()
		self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.group_artist_text)
		self.group_location = QLabel("Location")
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.group_location)
		self.group_location_text = QLineEdit()
		self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.group_location_text)
		self.group_country = QLabel("Country")
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.group_country)
		self.group_country_text = QLineEdit()
		self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.group_country_text)
		self.group_meta = QLabel("Meta")
		self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.group_meta)
		self.group_meta_text = QTextEdit()
		self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.group_meta_text)
		self.cleanButton_2 = QPushButton("Clear")
		self.cleanButton_2.clicked.connect(self.clean_tab)
		self.formLayout_2.addRow(self.cleanButton_2)

		# TAB 3

		self.video_name = QLabel("Name")
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.video_name)
		self.video_name_text = QLineEdit()
		self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.video_name_text)
		self.video_screenshot = QLabel("Screenshot")
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.video_screenshot)
		self.video_screenshot_text = QLineEdit()
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.video_screenshot_text)
		self.video_date = QLabel("Date")
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.video_date)
		self.video_date_text = QLineEdit()
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.video_date_text)
		self.video_size = QLabel("Size")
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.video_size)
		self.video_size_text = QLineEdit()
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.video_size_text)
		self.video_duration = QLabel("Duration")
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.video_duration)
		self.video_duration_text = QLineEdit()
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.video_duration_text)
		self.video_music = QLabel("Music")
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.video_music)
		self.video_music_text = QTextEdit()
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.video_music_text)
		self.video_artist = QLabel("Artist")
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.LabelRole, self.video_artist)
		self.video_artist_text = QTextEdit()
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.FieldRole, self.video_artist_text)
		self.video_meta = QLabel("Meta")
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.LabelRole, self.video_meta)
		self.video_meta_text = QTextEdit()
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.FieldRole, self.video_meta_text)
		self.formLayout_3.addRow(self.groupVideoWidget)

		self.video_PlayButton = QPushButton("Play")
		self.video_PlayButton.clicked.connect(self.video_play)
		self.groupVideoLayout.addWidget(self.video_PlayButton, 0, 0 , 1, 3)
		self.video_StopButton = QPushButton("Stop")
		self.video_StopButton.clicked.connect(self.video_stop)
		self.groupVideoLayout.addWidget(self.video_StopButton, 0, 3, 1, 3)
		self.video_GetMetaButton = QPushButton("Get Metadata")
		self.video_GetMetaButton.clicked.connect(self.get_meta)
		self.groupVideoLayout.addWidget(self.video_GetMetaButton, 1, 0, 1, 6)
		self.video_GetAudioStart = QLabel("Start")
		self.video_GetAudioStartEdit = QLineEdit()
		self.video_GetAudioEnd = QLabel("End")
		self.video_GetAudioEndEdit = QLineEdit()
		self.video_GetAudioButton = QPushButton("Get Audio")
		self.video_GetAudioButton.clicked.connect(self.get_audio)
		self.groupVideoLayout.addWidget(self.video_GetAudioStart, 2, 0)
		self.groupVideoLayout.addWidget(self.video_GetAudioStartEdit , 2, 1)
		self.groupVideoLayout.addWidget(self.video_GetAudioEnd, 2, 2)
		self.groupVideoLayout.addWidget(self.video_GetAudioEndEdit , 2, 3)
		self.groupVideoLayout.addWidget(self.video_GetAudioButton , 2, 4)

		self.cleanButton_3 = QPushButton("Clear")
		self.cleanButton_3.clicked.connect(self.clean_tab)
		self.formLayout_3.addRow(self.cleanButton_3)

		# TOP LAYOUT

		self.top_layout.addWidget(self.tab)
		self.top_layout.addWidget(self.videoWidget)

	def millis_to_duration(self,millis):
		seconds, _  = divmod(millis, 1000)
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return str(hours).zfill(2) + ':' +  str(minutes).zfill(2)  + ':' + str(seconds).zfill(2)

	def video_play(self):
		if self.video_name_text.text() and not (self.player.is_playing() or self.video_is_paused):
			self.media = self.vlc_instance.media_new(self.file_find(self.video_name_text.text()))
			self.player.set_media(self.media)
			self.player.set_xwindow(int(self.videoframe.winId()))# set video output
			self.video_duration = self.player.get_length()
			self.video_play_pause()
			
	def video_stop(self):
		self.player.stop()
		self.videoframe.setStyleSheet("background: black;")
		self.video_progress.setValue(0)
		self.video_play_duration_text.setText("00:00:00")
		self.video_is_paused = False

	def video_play_pause(self):
		if self.player.is_playing():
			self.player.pause()
			self.video_pause_play_button.setText("Play")
			self.video_is_paused = True
			self.timer.stop()
		else:
			self.player.play()
			self.video_pause_play_button.setText("Pause")
			self.timer.start()
			self.video_is_paused = False

	def set_position(self):
		self.timer.stop()
		self.player.set_position(self.video_progress.value() / 1000.0)
		if not self.video_is_paused:
			self.timer.start()

	def mspf(self):
		return int(1000 // (self.player.get_fps() or 25))

	def video_prev(self):
		next_frame_time = self.player.get_time() - self.mspf() 
		self.player.set_time(next_frame_time)

	def video_next(self):
		next_frame_time = self.player.get_time() + self.mspf()
		self.player.set_time(next_frame_time)

	def video_screen(self):
		if self.video_is_paused and self.video_name_text.text():
			fn = self.file_find(self.video_name_text.text())
			fn_base = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn)) + '/'
			os.makedirs(fn_base, exist_ok=True)
			self.player.video_take_snapshot(0, fn_base  + self.video_name_text.text() + '.jpg', 0 , 0)

	def slider_press(self):		
		self.video_slider_is_pressed = True
		self.timer.stop()

	def slider_release(self):
		self.video_slider_is_pressed = False
		self.set_position()
		self.video_play_duration_text.setText(self.millis_to_duration(self.player.get_time()))

	def gui_update(self):
		if self.player.is_playing() and not self.video_slider_is_pressed:
			self.video_progress.setValue(int(self.player.get_position() * 1000))
		if self.player.is_playing():
			self.video_play_duration_text.setText(self.millis_to_duration(self.player.get_time()))

	def clean_tab(self):
		match self.tab.currentIndex():
			case 0:
				self.artist_nickname_text.setText('')
				self.artist_altname_text.setPlainText('')
				self.artist_name_text.setText('')
				self.artist_id_text.setText('')
				self.artist_icon_text.setText('')
				self.artist_picture_text.setText('')
				self.artist_video_text.setPlainText('')
				self.artist_location_text.setText('')
				self.artist_group_text.setText('')
				self.artist_meta_text.setPlainText('')
			case  1:
				self.group_name_text.setText('')
				self.group_artist_text.setPlainText('')
				self.group_location_text.setText('')
				self.group_country_text.setText('')
				self.group_meta_text.setPlainText('')
			case 2:
				self.video_name_text.setText('')
				self.video_screenshot_text.setText('')
				self.video_date_text.setText('')
				self.video_size_text.setText('')
				self.video_duration_text.setText('')
				self.video_music_text.setPlainText('')
				self.video_artist_text.setPlainText('')
				self.video_meta_text.setPlainText('')

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

	def get_audio(self):
		if self.video_name_text.text():
			fn = self.file_find(self.video_name_text.text())
			fn_base = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn)) + '/'
			os.makedirs(fn_base, exist_ok=True)

			frame_start = self.video_GetAudioStartEdit.text()
			frame_stop = self.video_GetAudioEndEdit.text()

			if fn and frame_start and frame_stop:
				FFMPEG_AUDIO = ['ffmpeg', '-v', 'error', '-y', '-i', fn, '-ss', frame_start, '-t', frame_stop, fn_base + self.video_name_text.text() + '.mp3']
				try:
					proc = subprocess.run(FFMPEG_AUDIO)
				except:
					print('[error] ffmpeg audio: ' + fn)

	def file_open(self):
		yml,fn_base = None, None
		match self.tab.currentIndex():
			case 0:
				fn_base = BASE + '/YAML/artist/'
			case 1:
				fn_base = BASE + '/YAML/group/'
			case 2:
				fn_base = BASE + '/YAML/video/'

		fn, _ = QFileDialog.getOpenFileName(self, "Open File", fn_base, "MD (*.md)")

		if os.path.isfile(fn):
			with open(fn, 'r') as stream:
				try:
					yml = safe_load(stream)
				except:
					print("[error] Failed to parse: " + fn)
					return

		if yml:
			match os.path.basename(os.path.dirname(fn)):
				case "artist":
					self.artist_nickname_text.setText(yml['nickname'] if 'nickname' in yml else '')
					self.artist_altname_text.setPlainText("\n".join(yml['altname']) if 'altname' in yml else '')
					self.artist_name_text.setText(yml['name'] if 'name' in yml else '')
					self.artist_id_text.setText(yml['id'] if 'id' in yml else '')
					self.artist_icon_text.setText(yml['icon'] if 'icon' in yml else '')
					self.artist_picture_text.setText(yml['picture'] if 'picture' in yml else '')
					self.artist_video_text.setPlainText("\n".join(yml['video']) if 'video' in yml else '')
					self.artist_location_text.setText(yml['location'] if 'location' in yml else '')
					self.artist_group_text.setText(yml['group'] if 'group' in yml else '')
					self.artist_meta_text.setPlainText("\n".join(yml['meta']) if 'meta' in yml else '')
					self.tab.setCurrentIndex(0)
				case "group":
					self.group_name_text.setText(yml['name'] if 'name' in yml else '')
					self.group_artist_text.setPlainText("\n".join(yml['artist']) if 'artist' in yml else '')
					self.group_location_text.setText(yml['location'] if 'location' in yml else '')
					self.group_country_text.setText(yml['country'] if 'country' in yml else '')
					self.group_meta_text.setPlainText("\n".join(yml['meta']) if 'meta' in yml else '')
					self.tab.setCurrentIndex(1)
				case _:
					self.video_name_text.setText(yml['name'] if 'name' in yml else '')
					self.video_screenshot_text.setText(yml['screenshot'] if 'screenshot' in yml else '')
					self.video_date_text.setText(yml['date'] if 'date' in yml else '')
					self.video_size_text.setText(yml['size'] if 'size' in yml else '')
					self.video_duration_text.setText(yml['duration'] if 'duration' in yml else '')
					self.video_music_text.setPlainText("\n".join(yml['music']) if 'music' in yml else '')
					self.video_artist_text.setPlainText("\n".join(yml['artist']) if 'artist' in yml else '')
					self.video_meta_text.setPlainText("\n".join(yml['meta']) if 'meta' in yml else '')
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
					fn = self.file_find(self.video_name_text.text())
					fn_base = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn))
					os.makedirs(fn_base, exist_ok=True)
					fn = fn_base + '/' + self.video_name_text.text() + '.md'

		if not os.path.isfile(fn):
			fn, _ = QFileDialog.getSaveFileName(self, "Save File", fn_base, "MD (*.md)")
			if os.path.splitext(fn)[1] != '.md': fn = fn + '.md'

		with open(fn, 'w') as f:
        		f.write(safe_dump(yml, sort_keys=False, explicit_start=True, explicit_end=True))

	def PTL_close(self):
		if self.player.is_playing():
			self.player.pause()
			self.player.stop()
		self.close()

# MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
