import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

from src.elo_rating_system import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.k = competition()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 624)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn1_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn1_right.setGeometry(QtCore.QRect(160, 490, 141, 51))
        self.btn1_right.setObjectName("btn1_right")
        self.btn1_right.clicked.connect(lambda: self.click_left())

        self.btn2_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn2_left.setGeometry(QtCore.QRect(650, 490, 141, 51))
        self.btn2_left.setObjectName("btn2_left")
        self.btn2_left.clicked.connect(lambda: self.click_left())

        self.btn3_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_left.setGeometry(QtCore.QRect(405, 490, 141, 51))
        self.btn3_left.setObjectName("btn2_left")
        self.btn3_left.clicked.connect(lambda: self.click_center())

        self.showRand = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.showRand.setGeometry(QtCore.QRect(810, 550, 131, 41))
        self.showRand.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.showRand.setObjectName("showRand")
        self.showRand.clicked.connect(lambda: self.cilck_showall())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 50, 321, 401))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 321, 401))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beautiful Girl——竞技排名算法ELO实现和可视化"))
        self.showRand.setText(_translate("MainWindow", "查看排行"))
        iconn = QIcon('src/icon.png')
        MainWindow.setWindowIcon(iconn)
        self.btn1_right.setText(_translate("MainWindow", "LIKE♥"))
        self.btn2_left.setText(_translate("MainWindow", "LIKE♥"))
        self.btn3_left.setText(_translate("MainWindow", "♥LIKEALL♥"))
        self.setUpde()

    def setUpde(self):
        self.pix = QPixmap(self.k.contestants[0].pothopath)
        self.pix2 = QPixmap(self.k.contestants[1].pothopath)
        self.label.setScaledContents(True)
        self.label.setPixmap(self.pix)  # 显示图片
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(self.pix2)  # 显示图片
        print(self.k.contestants[0].get(),">",self.k.contestants[1].get())

    def click_left(self):
        action.left_btn(self.k)
        self.k = competition()
        self.setUpde()

    def click_right(self):
        action.rigth_btn(self.k)
        self.k = competition()
        self.setUpde()

    def click_center(self):
        action.cen_btn(self.k)
        self.k=competition()
        self.setUpde()

    def cilck_showall(self):
        from src import index
        index.main()

class action():

    @staticmethod
    def left_btn(k):
        ELO.elo(k.contestants, (1, 0))
        action.put(k)

    @staticmethod
    def rigth_btn(k):
        ELO.elo(k.contestants, (0, 1))
        action.put(k)

    @staticmethod
    def cen_btn(k):
        ELO.elo(k.contestants, (0.5, 0.5))
        action.put(k)

    @staticmethod
    def put(k):
        #将数据向数据库更新
        k.update_db()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
