#! /usr/bin/env python3

import sys,os,vlc,time

from PyQt6.QtCore import QSize, QRect, QTimer, Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
	QApplication,
	QMainWindow,
	QFrame,
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QPushButton,
	QSlider
)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# VLC

		self.vlc_instance = vlc.Instance()
		self.player = self.vlc_instance.media_player_new()
		self.player.audio_set_volume(50)

		self.video_is_paused = False
		self.filename = 'file:///home/user/Desktop/project/VIDEO/LeSkunk/SkunkWebSpin20mb.mov'

		# WINDOW

		self.setWindowTitle("PTL Player")
		self.setFixedSize(QSize(800,600))
		self.move(750,200)

		# CONTAINER

		self.container = QWidget()
		self.setCentralWidget(self.container)

		# FRAME

		self.video_layout = QVBoxLayout(self.container)
		
		self.videoframe = QFrame()
		self.videoframe.setStyleSheet("background: black;")
		self.video_layout.addWidget(self.videoframe)

		# CONTROL

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

		# TIMER

		self.timer = QTimer(self)
		self.timer.setInterval(100)# millis
		#self.timer.timeout.connect(self.update_ui)

		# PLAY

		self.media = self.vlc_instance.media_new(self.filename)
		self.player.set_media(self.media)
		self.player.set_xwindow(int(self.videoframe.winId()))
		self.video_play_pause()

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

	def mspf(self):
		return int(1000 // (self.player.get_fps() or 25))

	def video_prev(self):
		next_frame_time = self.player.get_time() + self.mspf() 
		self.player.set_time(next_frame_time)

	def video_next(self):
		next_frame_time = self.player.get_time() - self.mspf()
		self.player.set_time(next_frame_time)

	def video_screen(self):
		print("VOUT: " + str(self.player.has_vout()))
		self.player.video_take_snapshot(0,'/home/user/Desktop/project/debug.jpg', 0 , 0)

	def slider_press(self):		
		self.slider_is_pressed = True

	def slider_release(self):
		self.slider_is_pressed = False

# MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
