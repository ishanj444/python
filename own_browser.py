
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://gogoanime.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        back=QAction('back',self)
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)

        forward=QAction('forward',self)
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)
        
        refresh=QAction('refresh',self)
        refresh.triggered.connect(self.browser.reload)
        navbar.addAction(refresh)

        home=QAction('Home',self)
        home.triggered.connect(self.navihome)
        navbar.addAction(home)

        youtube=QAction('youtube',self)
        youtube.triggered.connect(self.naviyt)
        navbar.addAction(youtube)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navitourl)
        navbar.addWidget(self.urlbar)
        self.browser.urlChanged.connect(self.updateurl)

    def navihome(self):
    	self.browser.setUrl(QUrl('https://google.com'))

    def naviyt(self):
    	self.browser.setUrl(QUrl('https://www.youtube.com/'))

    def navitourl(self):
    	urltext = self.urlbar.text()	
    	self.browser.setUrl(QUrl('https://www.' + urltext + '.com'))

    def updateurl(self, x):
    	self.urlbar.setText(x.toString())



app=QApplication(sys.argv) 
QApplication.setApplicationName("Uchiha_Zoro")
window=MainWindow()
app.exec()       

