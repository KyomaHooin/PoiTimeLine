#!/usr/bin/python3
#
# PTL Metadata toolkit
#

import subprocess,random,json,vlc,sys,os,re

from yaml import safe_dump,safe_load

from PyQt6.QtCore import QSize, QRect, QTimer, Qt
from PyQt6.QtGui import QAction, QKeySequence, QPixmap
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
		self.player.audio_set_volume(60)

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
		self.video_layout = QGridLayout(self.videoWidget)
		
		self.videoframe = QFrame()
		self.videoframe.setStyleSheet("background: black;")
		self.video_layout.addWidget(self.videoframe, 0, 0, 1, 6)

		# VIDEO CONTROL

		self.video_pause_play_button = QPushButton("Pause")
		self.video_pause_play_button.clicked.connect(self.video_play_pause)
		self.video_layout.addWidget(self.video_pause_play_button, 1, 0)
		self.video_prev_button = QPushButton("Prev")
		self.video_prev_button.clicked.connect(self.video_prev)
		self.video_layout.addWidget(self.video_prev_button, 1, 1)
		self.video_next_button = QPushButton("Next")
		self.video_next_button.clicked.connect(self.video_next)
		self.video_layout.addWidget(self.video_next_button, 1, 2)
		self.video_screen_button = QPushButton("Screen")
		self.video_screen_button.clicked.connect(self.video_screen)
		self.video_layout.addWidget(self.video_screen_button, 1, 3)

		self.video_progress = QSlider(Qt.Orientation.Horizontal)
		self.video_progress.setRange(0, 1000)
		self.video_progress.sliderPressed.connect(self.slider_press)
		self.video_progress.sliderReleased.connect(self.slider_release)
		self.video_layout.addWidget(self.video_progress, 1, 4)

		self.video_play_duration_text = QLabel('00:00:00')
		self.video_layout.addWidget(self.video_play_duration_text, 1, 5)

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
		self.artist_altname_text.setAcceptRichText(0)
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
		self.artist_video_text.setAcceptRichText(0)
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
		self.artist_meta_text.setAcceptRichText(0)
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
		self.group_artist_text.setAcceptRichText(0)
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
		self.group_meta_text.setAcceptRichText(0)
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
		self.video_screenshot_text = QTextEdit()
		self.video_screenshot_text.setAcceptRichText(0)
		self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.video_screenshot_text)
		self.video_PreviewButton = QPushButton("Preview")
		self.video_PreviewButton.clicked.connect(self.video_screen_preview)
		self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.video_PreviewButton)
		self.video_date = QLabel("Date")
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.video_date)
		self.video_date_text = QLineEdit()
		self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.video_date_text)
		self.video_size = QLabel("Size")
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.video_size)
		self.video_size_text = QLineEdit()
		self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.video_size_text)
		self.video_duration = QLabel("Duration")
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.video_duration)
		self.video_duration_text = QLineEdit()
		self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.video_duration_text)
		self.video_music = QLabel("Music")
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.LabelRole, self.video_music)
		self.video_music_text = QTextEdit()
		self.video_music_text.setAcceptRichText(0)
		self.formLayout_3.setWidget(6, QFormLayout.ItemRole.FieldRole, self.video_music_text)
		self.video_artist = QLabel("Artist")
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.LabelRole, self.video_artist)
		self.video_artist_text = QTextEdit()
		self.video_artist_text.setAcceptRichText(0)
		self.formLayout_3.setWidget(7, QFormLayout.ItemRole.FieldRole, self.video_artist_text)
		self.video_meta = QLabel("Meta")
		self.formLayout_3.setWidget(8, QFormLayout.ItemRole.LabelRole, self.video_meta)
		self.video_meta_text = QTextEdit()
		self.video_meta_text.setAcceptRichText(0)
		self.formLayout_3.setWidget(8, QFormLayout.ItemRole.FieldRole, self.video_meta_text)
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

	def rand_name(self):
		rn = []
		for i in range(3):
			rn.append(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5)))
		return '-'.join(rn)

	def millis_to_duration(self,millis):
		seconds, _  = divmod(millis, 1000)
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

	def video_play(self):
		if self.video_name_text.text() and not (self.player.is_playing() or self.video_is_paused):
			self.media = self.vlc_instance.media_new(self.file_find(self.video_name_text.text()))
			self.player.set_media(self.media)
			self.player.set_xwindow(int(self.videoframe.winId()))# set video output
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
			fn = self.rand_name()
			os.makedirs(fn_base, exist_ok=True)
			self.player.video_take_snapshot(0, fn_base  + fn + '.jpg', 0 , 0)
			self.video_screenshot_text.append(fn + '.jpg')

	def video_screen_preview(self):
		if self.video_name_text.text() and self.video_screenshot_text.toPlainText():
			self.dlg = QDialog()
			self.dlg.setWindowTitle(self.video_name_text.text() + ' - Screen Preview')
			layout = QHBoxLayout()

			fn = self.file_find(self.video_name_text.text())
			fn_base = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn)) + '/'

			for img in self.video_screenshot_text.toPlainText().splitlines():
				label = QLabel()
				px = QPixmap(fn_base + img)
				label.setPixmap(px)
				layout.addWidget(label)

			self.dlg.setLayout(layout)
			self.dlg.show()

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
				self.video_screenshot_text.setPlainText('')
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
		return ''

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
				FFMPEG_AUDIO = ['ffmpeg', '-v', 'error', '-y', '-i', fn, '-ss', frame_start, '-t', frame_stop, fn_base + self.rand_name() + '.mp3']
				try:
					proc = subprocess.run(FFMPEG_AUDIO)
				except:
					print('[error] ffmpeg audio: ' + fn)

	def file_open(self):
		data,fn_base = None, None
		match self.tab.currentIndex():
			case 0:
				fn_base = BASE + '/YAML/artist/'
			case 1:
				fn_base = BASE + '/YAML/group/'
			case 2:
				fn_base = BASE + '/YAML/video/'

		match self.tab.currentIndex():
			case 0 | 1:
				fn, _ = QFileDialog.getOpenFileName(self, "Open File", fn_base, "MD (*.md)")
			case 2:
				fn, _ = QFileDialog.getOpenFileName(self, "Open File", fn_base, "JSON (*.json)")

		if os.path.isfile(fn):
			with open(fn, 'r') as stream:
				try:
					match self.tab.currentIndex():
						case 0 | 1:
							data = safe_load(stream)
						case 2:
							data = json.load(stream)
				except:
					print("[error] Failed to parse: " + fn)
					return

		if data:
			match os.path.basename(os.path.dirname(fn)):
				case "artist":
					self.artist_nickname_text.setText(data['nickname'] if 'nickname' in data else '')
					self.artist_altname_text.setPlainText("\n".join(data['altname']) if 'altname' in data else '')
					self.artist_name_text.setText(data['name'] if 'name' in data else '')
					self.artist_id_text.setText(data['hop'] if 'hop' in data else '')
					self.artist_icon_text.setText(data['icon'] if 'icon' in data else '')
					self.artist_picture_text.setText(data['picture'] if 'picture' in data else '')
					self.artist_video_text.setPlainText("\n".join(data['video']) if 'video' in data else '')
					self.artist_location_text.setText(data['location'] if 'location' in data else '')
					self.artist_group_text.setText(data['group'] if 'group' in data else '')
					self.artist_meta_text.setPlainText("\n".join(data['meta']) if 'meta' in data else '')
					self.tab.setCurrentIndex(0)
				case "group":
					self.group_name_text.setText(data['name'] if 'name' in data else '')
					self.group_artist_text.setPlainText("\n".join(data['artist']) if 'artist' in data else '')
					self.group_location_text.setText(data['location'] if 'location' in data else '')
					self.group_country_text.setText(data['country'] if 'country' in data else '')
					self.group_meta_text.setPlainText("\n".join(data['meta']) if 'meta' in data else '')
					self.tab.setCurrentIndex(1)
				case _:
					self.video_name_text.setText(data['name'] if 'name' in data else '')
					self.video_screenshot_text.setPlainText("\n".join(data['screenshot']) if 'screenshot' in data else '')
					self.video_date_text.setText(data['date'] if 'date' in data else '')
					self.video_size_text.setText(data['filesize'] if 'filesize' in data else '')
					self.video_duration_text.setText(data['duration'] if 'duration' in data else '')
					self.video_music_text.setPlainText("\n".join(data['music']) if 'music' in data else '')
					self.video_artist_text.setPlainText("\n".join(data['artist']) if 'artist' in data else '')
					self.video_meta_text.setPlainText("\n".join(data['meta']) if 'meta' in data else '')
					self.tab.setCurrentIndex(2)
	
	def file_save(self):
		fn, fn_base = None, None
		data = {}
		match self.tab.currentIndex():
			case 0:
				if self.artist_nickname_text.text():
					data['nickname'] = self.artist_nickname_text.text()
					if self.artist_altname_text.toPlainText(): data['altname'] = self.artist_altname_text.toPlainText().splitlines()
					if self.artist_name_text.text(): data['name'] = self.artist_name_text.text()
					if self.artist_id_text.text(): data['hop'] = self.artist_id_text.text()
					if self.artist_icon_text.text(): data['icon'] = self.artist_icon_text.text()
					if self.artist_picture_text.text(): data['picture'] = self.artist_picture_text.text()
					if self.artist_video_text.toPlainText(): data['video'] = self.artist_video_text.toPlainText().splitlines()
					if self.artist_location_text.text(): data['location'] = self.artist_location_text.text()
					if self.artist_group_text.text(): data['group'] = self.artist_group_text.text()
					if self.artist_meta_text.toPlainText(): data['meta'] = self.artist_meta_text.toPlainText().splitlines()
					fn_base = BASE + '/YAML/artist/'
					fn = fn_base + re.sub(r'[\'\-!?.+ \[\]\]\(\)]+', '', self.artist_nickname_text.text()) + '.md'
			case 1:
				if self.group_name_text.text():
					data['name'] = self.group_name_text.text()
					if self.group_artist_text.toPlainText(): data['artist'] = self.group_artist_text.toPlainText().splitlines()
					if self.group_location_text.text(): data['location'] = self.group_location_text.text()
					if self.group_country_text.text(): data['country'] = self.group_country_text.text()
					if self.group_meta_text.toPlainText(): data['meta'] = self.group_meta_text.toPlainText().splitlines()
					fn_base = BASE + '/YAML/group/'
					fn = fn_base + re.sub(r'[\'\-!?.+ \[\]\]\(\)]+', '', self.group_name_text.text()) + '.md'

			case 2:
				if self.video_name_text.text():
					data['name'] = self.video_name_text.text()
					if self.video_screenshot_text.toPlainText(): data['screenshot'] = self.video_screenshot_text.toPlainText().splitlines()
					if self.video_date_text.text(): data['date'] = self.video_date_text.text()
					if self.video_size_text.text(): data['filesize'] = self.video_size_text.text()
					if self.video_duration_text.text(): data['duration'] = self.video_duration_text.text()
					if self.video_music_text.toPlainText(): data['music'] = self.video_music_text.toPlainText().splitlines()
					if self.video_artist_text.toPlainText(): data['artist'] = self.video_artist_text.toPlainText().splitlines()
					if self.video_meta_text.toPlainText(): data['meta'] = self.video_meta_text.toPlainText().splitlines()
					fn = self.file_find(self.video_name_text.text())
					fn_base = BASE + '/YAML/video/' + os.path.basename(os.path.dirname(fn))
					os.makedirs(fn_base, exist_ok=True)
					fn = fn_base + '/' + re.sub(r'[\'\-!?.+ \[\]\]\(\)]+', '', os.path.splitext(self.video_name_text.text())[0]) + '.json'

		if fn:
			if not os.path.isfile(fn):
				match self.tab.currentIndex():
					case 0 | 1:
						fn, _ = QFileDialog.getSaveFileName(self, "Save File", fn_base, "MD (*.md)")
						if os.path.splitext(fn)[1] != '.md': fn = fn + '.md'
					case 2:
						fn, _ = QFileDialog.getSaveFileName(self, "Save File", fn_base, "JSON (*.json)")
						if os.path.splitext(fn)[1] != '.json': fn = fn + '.json'
		if data:
			with open(fn, 'w') as f:
				try:
					match self.tab.currentIndex():
						case 0 | 1:
							f.write(safe_dump(data, sort_keys=False, explicit_start=True, explicit_end=True))
						case 2:
							json.dump(data, f, indent=4)
				except:
					print("[error] Failed to write: " + fn)
					return

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
