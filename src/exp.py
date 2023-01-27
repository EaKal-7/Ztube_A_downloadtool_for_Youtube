# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitlednUjACL.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledNhSYDk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import json

from pytube import YouTube
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1MHOmam.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1njtTWh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 784)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setEnabled(True)
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 731, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.textview = QLabel(self.verticalLayoutWidget)
        self.textview.setObjectName(u"textview")
        font = QFont()
        font.setPointSize(14)
        self.textview.setFont(font)

        self.horizontalLayout_4.addWidget(self.textview)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 35))
        self.textEdit.setFont(font)

        self.horizontalLayout_4.addWidget(self.textEdit)

        self.Button = QPushButton(self.verticalLayoutWidget)
        self.Button.setObjectName(u"Button")
        self.Button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.Button, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 1800, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.result = QLabel(self.verticalLayoutWidget)
        self.result.setObjectName(u"result")

        self.verticalLayout.addWidget(self.result)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 600))

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.clean)
        self.Button.clicked.connect(self.show)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textview.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7f51\u5740", None))
        self.Button.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


    def clean(self):
        self.tableWidget.clear()

    def show(self):
        url = self.textEdit.toPlainText()
        result={}
        print(url)
        # try:
        #     # ,proxies={"https":"127.0.0.1:7890","http":"127.0.0.1:7890"}
        #     yt = YouTube(url)
        # except Exception as e:
        #     return {"error": str(e)}
        # result["title"] = yt.title
        # result["streams"] = []
        # result["pic"] = yt.thumbnail_url
        # result["views"] = yt.views
        # result["keyword"] = yt.keywords
        # temp={}
        # for i in yt.streams.filter(file_extension='mp4',progressive=True):
        #     temp["itag"] = i.itag
        #     try:
        #         temp["resolution"] = i.resolution
        #     except:
        #         temp["resolution"] = "None"
        #     temp["fps"] = i.fps
        #     temp["vcodec"] = i.video_codec
        #     temp["filesize"] = i.filesize_mb
        #     temp["download_url"] = i.url
        #     result["streams"].append(temp.copy())
        with open ("new.json","r") as f:
            result=json.load(f)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        titlelist=["itag","resolution","fps","vcodec","filesize","download_url"]
        self.tableWidget.setHorizontalHeaderLabels(titlelist)
        # print(result["streams"])
        sum=0
        for i in result["streams"]:
            self.tableWidget.insertRow(sum)
            self.tableWidget.setItem(sum,0,QTableWidgetItem(str(i["itag"])))
            print(str(i["itag"]))
            self.tableWidget.setItem(sum,1,QTableWidgetItem(str(i["resolution"])))
            self.tableWidget.setItem(sum,2,QTableWidgetItem(str(i["fps"])))
            self.tableWidget.setItem(sum,3,QTableWidgetItem(str(i["vcodec"])))
            self.tableWidget.setItem(sum,4,QTableWidgetItem(str(i["filesize"])))
            self.tableWidget.setItem(sum,5,QTableWidgetItem(str(i["download_url"])))
            sum+=1



if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    MainWindow = QMainWindow()
    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    
    # 结束QApplication
    sys.exit(app.exec_())
    # 注意，在PySide6中，需要使用app.exec()
    # sys.exit(app.exec())