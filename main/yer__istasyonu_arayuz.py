# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Son.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1546, 956)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1541, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_8 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_8.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_8.setObjectName("widget_8")
        self.label_17 = QtWidgets.QLabel(self.widget_8)
        self.label_17.setGeometry(QtCore.QRect(170, 10, 121, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget_8)
        self.graphicsView_8.setGeometry(QtCore.QRect(10, 30, 431, 241))
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.horizontalLayout.addWidget(self.widget_8)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget_9 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_9.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_9.setObjectName("widget_9")
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        self.label_16.setGeometry(QtCore.QRect(150, 10, 161, 16))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.widget_9)
        self.graphicsView_7.setGeometry(QtCore.QRect(0, 30, 450, 241))
        self.graphicsView_7.setMaximumSize(QtCore.QSize(450, 16777215))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.horizontalLayout.addWidget(self.widget_9)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.widget_10 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_10.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_10.setObjectName("widget_10")
        self.label_18 = QtWidgets.QLabel(self.widget_10)
        self.label_18.setGeometry(QtCore.QRect(130, 10, 181, 20))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.widget_10)
        self.graphicsView_9.setGeometry(QtCore.QRect(0, 30, 441, 241))
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.horizontalLayout.addWidget(self.widget_10)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 290, 1201, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget_2)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 351, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.widget_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(160, 10, 47, 13))
        self.label.setObjectName("label")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_2.setGeometry(QtCore.QRect(5, 30, 351, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.widget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(5, 30, 351, 192))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(160, 10, 47, 13))
        self.label_4.setObjectName("label_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.widget_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 30, 351, 192))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_3.addWidget(self.widget_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.widget_5 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 61, 16))
        self.label_5.setObjectName("label_5")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.widget_5)
        self.graphicsView_5.setGeometry(QtCore.QRect(10, 30, 341, 191))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_3.addWidget(self.widget_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.widget_6 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_6.setObjectName("widget_6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(170, 10, 47, 13))
        self.label_6.setObjectName("label_6")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.widget_6)
        self.graphicsView_6.setGeometry(QtCore.QRect(10, 31, 341, 191))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1210, 290, 331, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget_7.setAutoFillBackground(False)
        self.widget_7.setObjectName("widget_7")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(80, 30, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_7)
        self.label_9.setGeometry(QtCore.QRect(0, 150, 331, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setGeometry(QtCore.QRect(0, 170, 331, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.widget_7)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        self.label_11.setGeometry(QtCore.QRect(50, 220, 61, 21))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        self.label_12.setGeometry(QtCore.QRect(0, 300, 331, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_7)
        self.label_13.setGeometry(QtCore.QRect(0, 330, 331, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_7)
        self.label_14.setGeometry(QtCore.QRect(20, 370, 221, 16))
        self.label_14.setObjectName("label_14")
        self.checkBox = QtWidgets.QCheckBox(self.widget_7)
        self.checkBox.setGeometry(QtCore.QRect(110, 400, 91, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 430, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_15 = QtWidgets.QLabel(self.widget_7)
        self.label_15.setGeometry(QtCore.QRect(0, 460, 331, 16))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.widget_7)
        self.label_19.setGeometry(QtCore.QRect(0, 490, 331, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_7)
        self.label_20.setGeometry(QtCore.QRect(20, 520, 131, 21))
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 520, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_21 = QtWidgets.QLabel(self.widget_7)
        self.label_21.setGeometry(QtCore.QRect(20, 570, 121, 21))
        self.label_21.setObjectName("label_21")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 570, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_22 = QtWidgets.QLabel(self.widget_7)
        self.label_22.setGeometry(QtCore.QRect(0, 600, 331, 16))
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.widget_7)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 770, 1201, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.verticalLayoutWidget_3)
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.verticalLayout_3.addWidget(self.graphicsView_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1546, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_17.setText(_translate("MainWindow", "Gyro Verileri"))
        self.label_16.setText(_translate("MainWindow", "Anlık Görüntü"))
        self.label_18.setText(_translate("MainWindow", "Koordinat Bilgileri"))
        self.label_2.setText(_translate("MainWindow", "Sıcaklık"))
        self.label.setText(_translate("MainWindow", "Basınç"))
        self.label_3.setText(_translate("MainWindow", "Yükseklik"))
        self.label_4.setText(_translate("MainWindow", "Pil Gerilim"))
        self.label_5.setText(_translate("MainWindow", "GPS Altidute"))
        self.label_6.setText(_translate("MainWindow", "Hız"))
        self.label_7.setText(_translate("MainWindow", "Takım No:"))
        self.label_8.setText(_translate("MainWindow", "39175"))
        self.label_9.setText(_translate("MainWindow", "----------------------------------------------------------------------------------"))
        self.label_10.setText(_translate("MainWindow", "------------Video Aktarımı------------------------------------------------------"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "Dosya Seç "))
        self.pushButton_2.setText(_translate("MainWindow", "Gönder"))
        self.label_12.setText(_translate("MainWindow", "------------------------------------------------------------------------------------"))
        self.label_13.setText(_translate("MainWindow", "------------Ayrılma Komutu---------------------------------------------------"))
        self.label_14.setText(_translate("MainWindow", "Modülleri ayırmak istediğinize emin misiniz ?"))
        self.checkBox.setText(_translate("MainWindow", "Evet, Eminim"))
        self.pushButton_3.setText(_translate("MainWindow", "Ayrıl!"))
        self.label_15.setText(_translate("MainWindow", "---------------------------------------------------------------------------------------"))
        self.label_19.setText(_translate("MainWindow", "-----------Aktif İniş Sistemi---------------------------------------------------"))
        self.label_20.setText(_translate("MainWindow", "Aktif İniş Sistemini Çalıştır"))
        self.pushButton_4.setText(_translate("MainWindow", "Güç Ver"))
        self.label_21.setText(_translate("MainWindow", "Aktif İniş Sistemini Durdur"))
        self.pushButton_5.setText(_translate("MainWindow", "Gücü Kes"))
        self.label_22.setText(_translate("MainWindow", "------------------------------------------------------------------------------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

