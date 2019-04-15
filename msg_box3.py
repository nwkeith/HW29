# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_box.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led = LED(23)

led_pin=24
GPIO.setup(led_pin, GPIO.OUT)
pwm=GPIO.PWM(led_pin, 100)
pwm.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
        #ledButton["text"] = "Turn LED on"
    else:
        led.on()
        #ledButton["text"] = "Turn LED off"

def btn_clicked():
    #print("Button Pressed")
    #QMessageBox.information(MainWindow, 'Welcome', 'PyQt5 + Raspberry PI')
    ledToggle()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 210, 191, 131))
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        self.verticalSlider.setGeometry(QtCore.QRect(120, 200, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "Toggle LED"))
        self.pushButton.clicked.connect(btn_clicked)
        self.verticalSlider.valueChanged.connect(self.sliderMov)
    def sliderMov(self):
        value=self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)

import sys
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

