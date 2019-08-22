import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, qApp
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class MyApp(QMainWindow):
            
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        webcamAction = QAction(QIcon('webcam.png'), 'Webcam', self)
        webcamAction.triggered.connect(self.
        
        videoAction = QAction(QIcon('video.png'), 'Video', self)
        videoAction.triggered.connect(self.showDialog)
        
        graphAction = QAction(QIcon('graph.png'), 'Graph', self)
        videoAction.triggered.connect(self.showDialog)
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        
        self.statusBar()
        self.toolbar = self.addToolBar('mytool')
        
        self.toolbar.addAction(webcamAction)
        self.toolbar.addAction(videoAction)
        self.toolbar.addAction(graphAction)
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('으아니')
        self.setGeometry(300, 300, 300, 200)#(창 시작지점 X, Y / 창 크기 W, H)
        self.show()
        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
            #end with
        #end if
    #end def

                                    
                
#end def
def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
