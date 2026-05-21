#! /usr/bin/env python3

import sys,os,vlc

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
		#self.pause_button.clicked.connect(self.video_play_pause)
		self.video_control_layout.addWidget(self.video_pause_play_button)
		self.video_prev_button = QPushButton("Prev")
		#self.video_prev_button.clicked.connect(self.video_prev)
		self.video_control_layout.addWidget(self.video_prev_button)
		self.video_next_button = QPushButton("Prev")
		#self.video_next_button.clicked.connect(self.video_next)
		self.video_control_layout.addWidget(self.video_next_button)

		self.video_progress = QSlider(Qt.Orientation.Horizontal)
		self.video_progress.setRange(0, 1000)
		self.video_progress.sliderPressed.connect(self.slider_press)
		self.video_progress.sliderReleased.connect(self.slider_release)
		self.video_control_layout.addWidget(self.video_progress)

		self.timer = QTimer(self)
		self.timer.setInterval(100)
		#self.timer.timeout.connect(self.update_ui)

		def video_play_pause(self):
			if self.player.is_playing():
				self.player.pause()
				self.self.video_pause_play_button.setText("Play")
				self.is_paused = True
				self.timer.stop()
			else:
				self.mediaplayer.play()
				self.self.video_pause_play_button.setText("Pause")
				self.timer.start()
				self.is_paused = False

	def slider_press(self):		
		self.slider_is_pressed = True

	def slider_release(self):
		self.slider_is_pressed = False

# MAIN

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
