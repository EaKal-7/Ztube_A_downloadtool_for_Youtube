# -*- coding: utf-8 -*-

################################################################################
## Youtube下载器
################################################################################
import os
import sys
import requests
from moviepy.editor import VideoFileClip,AudioFileClip
from urllib import request, parse, error
import re
import json
from qt_material import apply_stylesheet
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt,QThread,Signal,Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


yt=None
result={}


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 895)
        self.audioflag = False
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setEnabled(True)
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1069, 887))
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.KeywordPlain = QLabel(self.verticalLayoutWidget)
        self.KeywordPlain.setObjectName(u"KeywordPlain")
        font1 = QFont()
        font1.setPointSize(12)
        self.KeywordPlain.setFont(font1)
        self.KeywordPlain.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.KeywordPlain, 2, 1, 1, 1)

        self.PicPlain = QLabel(self.verticalLayoutWidget)
        self.PicPlain.setObjectName(u"PicPlain")
        self.PicPlain.setFont(font1)
        self.PicPlain.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.PicPlain, 3, 1, 1, 1)

        self.ViewsEdit = QLabel(self.verticalLayoutWidget)
        self.ViewsEdit.setObjectName(u"ViewsEdit")
        self.ViewsEdit.setFont(font1)
        self.ViewsEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.ViewsEdit.setWordWrap(False)

        self.gridLayout.addWidget(self.ViewsEdit, 1, 2, 1, 1)

        self.KeywordEdit = QLabel(self.verticalLayoutWidget)
        self.KeywordEdit.setObjectName(u"KeywordEdit")
        self.KeywordEdit.setFont(font1)
        self.KeywordEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.KeywordEdit.setWordWrap(False)

        self.gridLayout.addWidget(self.KeywordEdit, 2, 2, 1, 1)

        self.viewsPlain = QLabel(self.verticalLayoutWidget)
        self.viewsPlain.setObjectName(u"viewsPlain")
        self.viewsPlain.setFont(font1)
        self.viewsPlain.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.viewsPlain, 1, 1, 1, 1)

        self.titleEdit = QLabel(self.verticalLayoutWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setMinimumSize(QSize(600, 0))
        self.titleEdit.setFont(font1)
        self.titleEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.titleEdit.setWordWrap(False)

        self.gridLayout.addWidget(self.titleEdit, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.titlePlain = QLabel(self.verticalLayoutWidget)
        self.titlePlain.setObjectName(u"titlePlain")
        self.titlePlain.setMaximumSize(QSize(60, 16777215))
        self.titlePlain.setFont(font1)
        self.titlePlain.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.titlePlain, 0, 1, 1, 1)

        self.PicEdit = QLabel(self.verticalLayoutWidget)
        self.PicEdit.setObjectName(u"PicEdit")
        self.PicEdit.setFont(font1)
        self.PicEdit.setMinimumSize(QSize(448, 252))
        self.PicEdit.setMaximumSize(QSize(448, 252))
        self.PicEdit.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.PicEdit.setWordWrap(False)

        self.gridLayout.addWidget(self.PicEdit, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.result = QLabel(self.verticalLayoutWidget)
        self.result.setObjectName(u"result")
        self.result.setFont(font)
        self.result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 300))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FlieSelect = QPushButton(self.verticalLayoutWidget)
        self.FlieSelect.setObjectName(u"FlieSelect")

        self.gridLayout_2.addWidget(self.FlieSelect, 1, 2, 1, 1)

        self.DownloadPath = QTextEdit(self.verticalLayoutWidget)
        self.DownloadPath.setObjectName(u"DownloadPath")
        self.DownloadPath.setMaximumSize(QSize(16777215, 40))
        self.DownloadPath.setFont(font)

        self.gridLayout_2.addWidget(self.DownloadPath, 1, 1, 1, 1)

        self.DownloadPathPlain = QLabel(self.verticalLayoutWidget)
        self.DownloadPathPlain.setObjectName(u"DownloadPathPlain")

        self.gridLayout_2.addWidget(self.DownloadPathPlain, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.progressBar)

        self.Downloadresult = QLabel(self.verticalLayoutWidget)
        self.Downloadresult.setObjectName(u"Downloadresult")
        self.Downloadresult.setFont(font)
        self.Downloadresult.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Downloadresult)

        self.verticalSpacer_2 = QSpacerItem(20, 600, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.download)
        self.FlieSelect.clicked.connect(self.openexploer)
        self.Button.clicked.connect(self.show)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ztube——A YouTube Downloader", None))
        self.textview.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7f51\u5740", None))
        self.Button.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.KeywordPlain.setText(QCoreApplication.translate("MainWindow", u"Keyword:", None))
        self.PicPlain.setText(QCoreApplication.translate("MainWindow", u"Pic:", None))
        self.ViewsEdit.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.KeywordEdit.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.viewsPlain.setText(QCoreApplication.translate("MainWindow", u"Views:", None))
        self.titleEdit.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.titlePlain.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.PicEdit.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.FlieSelect.setText(QCoreApplication.translate("MainWindow", u"Select From Explorer", None))
        self.DownloadPathPlain.setText(QCoreApplication.translate("MainWindow", u"DownLoadPath", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DownLoad!!!", None))
        self.Downloadresult.setText(QCoreApplication.translate("MainWindow", u"Null", None))
    # retranslateUi

    #打开文件资源管理器
    def openexploer(self):
        self.DownloadPath.setText(QFileDialog.getExistingDirectory())

    def clean(self):
        self.tableWidget.clear()

    #解析url链接并展示
    def show(self):
        global yt
        global result
        url = self.textEdit.toPlainText()
        self.audioflag = False
        result = {}
        try:
            if url == "":
                self.result.setText("请输入网址")
                return
            self.result.setText("正在获取视频信息...")
            self.analysisThread = AnalysisThread(url)
            self.analysisThread.analysis_proess_signal.connect(self.set_item_value)
            self.analysisThread.start()
        except Exception as e:
            self.result.setText("获取视频信息失败")
            return {"error": str(e)}

    #下载视频
    def download(self):
        global yt
        global result
        print(self.tableWidget.currentRow())
        if len(result) == 0:
            self.Downloadresult.setText("请先获取视频信息")
            return
        if self.DownloadPath.toPlainText() == "":
            self.Downloadresult.setText("请选择下载路径")
            return
        if self.tableWidget.currentRow() == -1:
            self.Downloadresult.setText("请选择下载视频或者等待解析完成")
            return
        the_filesize = requests.get(result["audiourl"], stream=True).headers['Content-Length']
        the_filepath = self.DownloadPath.toPlainText() + "/" + result['title'] + ".m4a"
        the_fileobj = open(the_filepath, 'wb')
        #### 创建下载线程
        self.downloadThread1 = downloadThread(result["audiourl"], the_filesize, the_fileobj, buffer=10240)
        self.downloadThread1.download_proess_signal.connect(self.setprogress)
        self.downloadThread1.start()

        downloadurl = self.tableWidget.item(self.tableWidget.currentRow(), 5).text()
        self.Downloadresult.setText("正在下载")

        the_filesize = requests.get(downloadurl, stream=True).headers['Content-Length']
        the_filepath = self.DownloadPath.toPlainText() + "/" + result['title'] + ".mp4"
        the_fileobj = open(the_filepath, 'wb')
        #### 创建下载线程
        self.downloadThread = downloadThread(downloadurl, the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()

    #下载音频进度条
    def setprogress(self, value):
        if value == 100:
            self.audioflag = True
            self.Downloadresult.setText("下载完成")
            return


    #视频下载以及资源整合
    def set_progressbar_value(self, value):
        global result
        global yt
        self.progressBar.setValue(value)
        self.Downloadresult.setText("正在下载,已完成" + str(value) + "%")
        if value == 100:
            self.Downloadresult.setText("下载完成,正在整合资源")
            if self.audioflag:
                clip1=VideoFileClip(self.DownloadPath.toPlainText()+'/'+result['title']+'.mp4')
                clip2=AudioFileClip(self.DownloadPath.toPlainText()+'/'+result['title']+'.m4a')
                final_clip=clip1.set_audio(clip2)
                final_clip.write_videofile(self.DownloadPath.toPlainText()+'/'+result['title']+'_final.mp4')
                self.Downloadresult.setText("整合完成")
                return

    #展示页面数据
    def set_item_value(self, value):
        global result
        if value == 402:
            # 解析失败
            self.result.setText("解析失败")
            return
        elif value == 10:
            self.titleEdit.setText(result["title"])
            self.result.setText("GET TITLE SUCCESS")
        elif value == 20:
            self.ViewsEdit.setText(str(result["views"]))
            self.result.setText("GET VIEWS SUCCESS")
        elif value == 30:
            self.KeywordEdit.setText(str(result["keyword"]))
            self.result.setText("GET KEYWORD SUCCESS")
        elif value == 40:
            req = requests.get(result['pic'])
            with open('../temp/' + result["url"].split('v=')[-1] + '.jpg', 'wb') as f:
                f.write(req.content)
            self.PicEdit.setPixmap(QPixmap('./temp/' + result["url"].split('v=')[-1] + '.jpg'))
            self.PicEdit.setScaledContents(True)
            self.result.setText("GET PIC SUCCESS,LODING STREAMS NOW")
        elif value == 100:
            self.tableWidget.setRowCount(0)
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(6)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            titlelist = ["itag", "resolution", "fps", "vcodec", "filesize(MB)", "download_url"]
            self.tableWidget.setHorizontalHeaderLabels(titlelist)
            sum = 0
            for i in result["streams"]:
                self.tableWidget.insertRow(sum)
                itag = QTableWidgetItem(str(i["itag"]))
                resolution = QTableWidgetItem(str(i["resolution"]))
                fps = QTableWidgetItem(str(i["fps"]))
                vcodec = QTableWidgetItem(str(i["vcodec"]))
                filesize = QTableWidgetItem(str(i["filesize"]))
                download_url = QTableWidgetItem(str(i["download_url"]))
                itag.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                resolution.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                fps.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                vcodec.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                filesize.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                download_url.setFlags(
                    Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                self.tableWidget.setItem(sum, 0, itag)
                self.tableWidget.setItem(sum, 1, resolution)
                self.tableWidget.setItem(sum, 2, fps)
                self.tableWidget.setItem(sum, 3, vcodec)
                self.tableWidget.setItem(sum, 4, filesize)
                self.tableWidget.setItem(sum, 5, download_url)
                sum += 1
            self.result.setText("GET STREAMS SUCCESS")


#视频下载
class downloadThread(QThread):
    download_proess_signal = Signal(int)  # 创建信号

    def __init__(self, url, filesize, fileobj, buffer):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer

    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)
            # 流下载模式
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)  # 设置指针位置
                self.fileobj.write(chunk)  # 写入文件
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))  # 发送信号
            #######################################################################
            self.fileobj.close()  # 关闭文件
            self.exit(0)  # 关闭线程


        except Exception as e:
            print(e)


#解析url
class AnalysisThread(QThread):
    analysis_proess_signal = Signal(int)  # 创建信号

    def __init__(self, url):
        super(AnalysisThread, self).__init__()
        self.url = url

    def run(self):
        try:
            global yt
            global result
            url = self.url
            response = request.urlopen(request.Request(url, headers={}))
            data = response.read()
            content_encoding = response.getheader('Content-Encoding')
            if content_encoding == 'gzip':
                data = ungzip(data)
            elif content_encoding == 'deflate':
                data = undeflate(data)
            if True:
                charset = match1(
                    response.getheader('Content-Type', ''), r'charset=([\w-]+)'
                )
                if charset is not None:
                    data = data.decode(charset, 'ignore')
                else:
                    data = data.decode('utf-8', 'ignore')

            video_page = data

            try:  #
                ytInitialPlayerResponse = json.loads(
                    re.search('ytInitialPlayerResponse\s*=\s*([^\n]+?});</script>', video_page).group(1))
            except:
                ytInitialPlayerResponse = json.loads(
                    re.search('ytInitialPlayerResponse\s*=\s*([^\n]+?});', video_page).group(1))
            result = {}
            result['streams'] = []
            result['url'] = url
            result['title'] = ytInitialPlayerResponse["videoDetails"]["title"]
            self.analysis_proess_signal.emit(10)
            result['views'] = ytInitialPlayerResponse["videoDetails"]["viewCount"]
            self.analysis_proess_signal.emit(20)
            result['keyword'] = ytInitialPlayerResponse["videoDetails"]["keywords"]
            self.analysis_proess_signal.emit(30)
            result['pic'] = ytInitialPlayerResponse["videoDetails"]["thumbnail"]["thumbnails"][-1]["url"]
            self.analysis_proess_signal.emit(40)
            temp = ytInitialPlayerResponse['streamingData']['adaptiveFormats']
            newvideo = {}
            for i in temp:
                if i['mimeType'].find('video/mp4') != -1:
                    newvideo['itag'] = i['itag']
                    newvideo['resolution'] = i['qualityLabel']
                    newvideo['fps'] = i['fps']
                    newvideo['vcodec'] = i['mimeType'].split("\"")[1].split("\"")[0]
                    newvideo['download_url'] = i['url']
                    newvideo['filesize'] = round(int(i['contentLength']) / 1024 / 1024, 2)
                    result['streams'].append(newvideo.copy())
                if i['mimeType'].find('audio/mp4') != -1:
                    result['audiourl'] = i['url']
            self.analysis_proess_signal.emit(100)  # 发送信号
            # self.analysis_proess_signal2.emit(result)
            self.exit(0)  # 关闭线程


        except Exception as e:
            self.analysis_proess_signal.emit(402)
            print(e)

def ungzip(data):
    """为内容编码解压缩数据：gzip。
    """
    from io import BytesIO
    import gzip
    buffer = BytesIO(data)
    f = gzip.GzipFile(fileobj=buffer)
    return f.read()
def undeflate(data):
    """为内容编码解压缩数据：deflate。
    """
    import zlib
    decompressobj = zlib.decompressobj(-zlib.MAX_WBITS)
    return decompressobj.decompress(data)+decompressobj.flush()
def match1(text, *patterns):
    """
    在字符串中扫描匹配某些模式的子字符串（仅限第一个子组）
    """

    if len(patterns) == 1:
        pattern = patterns[0]
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
    else:
        ret = []
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                ret.append(match.group(1))
        return ret

if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    MainWindow = QMainWindow()
    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)
    apply_stylesheet(app, theme='light_blue.xml')
    MainWindow.show()

    # 结束QApplication
    sys.exit(app.exec_())
    # 注意，在PySide6中，需要使用app.exec()
    # sys.exit(app.exec())


