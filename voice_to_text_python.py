# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılım ile ilgili herşey/ses kaydetme programı/voice_to_text.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pencere/Bokehlicia-Captiva-Sound-recorder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Kaydetmek = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kaydetmek.setGeometry(QtCore.QRect(10, 330, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Kaydetmek.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/kaydet/discet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Kaydetmek.setIcon(icon1)
        self.pushButton_Kaydetmek.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_Kaydetmek.setObjectName("pushButton_Kaydetmek")
        self.pushButton_mikrafon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mikrafon.setGeometry(QtCore.QRect(510, 10, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_mikrafon.setFont(font)
        self.pushButton_mikrafon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mic/microphone-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mikrafon.setIcon(icon2)
        self.pushButton_mikrafon.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_mikrafon.setObjectName("pushButton_mikrafon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 30, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 551, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_cevir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cevir.setGeometry(QtCore.QRect(340, 330, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_cevir.setFont(font)
        self.pushButton_cevir.setIcon(icon1)
        self.pushButton_cevir.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_cevir.setObjectName("pushButton_cevir")
        self.textEdit_c = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_c.setGeometry(QtCore.QRect(570, 100, 551, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_c.setFont(font)
        self.textEdit_c.setObjectName("textEdit_c")
        self.pushButton_cevir_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cevir_2.setGeometry(QtCore.QRect(580, 280, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_cevir_2.setFont(font)
        self.pushButton_cevir_2.setIcon(icon1)
        self.pushButton_cevir_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_cevir_2.setObjectName("pushButton_cevir_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(560, 270, 21, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 261, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Kaydetmek.setText(_translate("MainWindow", "Save audio"))
        self.label.setText(_translate("MainWindow", "Ready"))
        self.pushButton_cevir.setText(_translate("MainWindow", "Translate"))
        self.pushButton_cevir_2.setText(_translate("MainWindow", "Save translation as audio"))
        self.commandLinkButton.setText(_translate("MainWindow", "batuhanokmen.com"))
        self.comboBox.setCurrentText(_translate("MainWindow", "choose language"))
        self.comboBox.setItemText(0, _translate("MainWindow", "choose language"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Türkçe"))
        self.comboBox.setItemText(2, _translate("MainWindow", "English"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Español"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Deutsch"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Português"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Polski"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Italiano"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Hrvatski"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Nederlands"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Dansk"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Lietuvių"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Eesti"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Français"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Arabic (United Arab Emirates)"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Japanese (Japan)"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Korean (South Korea)"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Russian (Russia)"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Chinese, Mandarin (Simplified, China)"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Bulgarian"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Czech"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Danish"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Greek"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Finnish"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Hebrew (Israel)"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Hindi (India)"))
        self.comboBox.setItemText(26, _translate("MainWindow", "Croatian"))
        self.comboBox.setItemText(27, _translate("MainWindow", "Indonesian"))
        self.comboBox.setItemText(28, _translate("MainWindow", "Romanian"))
        self.comboBox.setItemText(29, _translate("MainWindow", "Serbian"))
        self.comboBox.setItemText(30, _translate("MainWindow", "Swedish"))
        self.comboBox.setItemText(31, _translate("MainWindow", "Ukrainian"))
        self.comboBox.setItemText(32, _translate("MainWindow", "Vietnamese"))
        self.comboBox.setItemText(33, _translate("MainWindow", "Afrikaans (South Africa)"))
        self.comboBox.setItemText(34, _translate("MainWindow", "Azerbaijani "))
        self.comboBox.setItemText(35, _translate("MainWindow", "Persian"))
        self.comboBox.setItemText(36, _translate("MainWindow", "Filipino"))
        self.comboBox.setItemText(37, _translate("MainWindow", "Swahili (Kenya)"))
        self.comboBox.setItemText(38, _translate("MainWindow", "Arabic (Saudi Arabia)"))
        self.comboBox.setItemText(39, _translate("MainWindow", "Arabic (Qatar)"))
        self.comboBox.setItemText(40, _translate("MainWindow", "Arabic (Kuwait)"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "choose language"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "choose language"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Türkçe"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "English"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Español"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Deutsch"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Português"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Polski"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Italiano"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Hrvatski"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Nederlands"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Dansk"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Lietuvių"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Eesti"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Français"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Arabic (United Arab Emirates)"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Japanese (Japan)"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Korean (South Korea)"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Russian (Russia)"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Chinese, Mandarin (Simplified, China)"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Bulgarian"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "Czech"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "Danish"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "Greek"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "Finnish"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "Hebrew (Israel)"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "Hindi (India)"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "Croatian"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "Indonesian"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "Romanian"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "Serbian"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "Swedish"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "Ukrainian"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "Vietnamese"))
        self.comboBox_2.setItemText(33, _translate("MainWindow", "Afrikaans (South Africa)"))
        self.comboBox_2.setItemText(34, _translate("MainWindow", "Azerbaijani "))
        self.comboBox_2.setItemText(35, _translate("MainWindow", "Persian"))
        self.comboBox_2.setItemText(36, _translate("MainWindow", "Filipino"))
        self.comboBox_2.setItemText(37, _translate("MainWindow", "Swahili (Kenya)"))
        self.comboBox_2.setItemText(38, _translate("MainWindow", "Arabic (Saudi Arabia)"))
        self.comboBox_2.setItemText(39, _translate("MainWindow", "Arabic (Qatar)"))
        self.comboBox_2.setItemText(40, _translate("MainWindow", "Arabic (Kuwait)"))

import icons_rc
