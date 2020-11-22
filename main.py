import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # title bar edits
        self.setWindowTitle("Testerdz")
        label = QLabel("Jankyd")
        self.setWindowIcon(QIcon("./icons/icon.png"))

        # mainwindow edits
        self.setStyleSheet("background-color: #303030;")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        backButton = QAction(QIcon("icons/back.png"), "Back button", self)
        backButton.triggered.connect(self.onBackButtonClick)
        toolbar.addAction(backButton)

        homeButton = QAction(QIcon("icons/home.png"), "Home button", self)
        homeButton.triggered.connect(self.onHomeButtonClick)
        toolbar.addAction(homeButton)

        nextButton = QAction(QIcon("icons/next.png"), "Next button", self)
        nextButton.triggered.connect(self.onBackButtonClick)
        toolbar.addAction(nextButton)

        self.setStatusBar(QStatusBar(self))

    def onBackButtonClick(self, s):
        print("Back", s)
    
    def onHomeButtonClick(self, s):
        print("Home", s)

    def onNextButtonClick(self, s):
        print("Next", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()