from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Moodipy.UserSummary import Person
from screeninfo import get_monitors
import time

class LoadPredictPg(QMainWindow):
    def __init__(self):
        max_screen_width = 1536
        min_screen_width = 1000

        max_screen_height = 864
        min_screen_height = 610
        super().__init__()
        self.title = "Load Page"
        self.desktop = QApplication.desktop()
        self.left = 0
        self.top = 0
        temp_width = get_monitors()[0].width * .5
        self.width = max(min(temp_width, max_screen_width), min_screen_width)
        temp_height = get_monitors()[0].height * .5
        self.height = max(min(temp_height, max_screen_height), min_screen_height)
        self.initUI()

    def initUI(self):
        self.sw = (self.width / 1000)
        self.sh = (self.height / 610)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #bffed3")
        self.loadingBar = QProgressBar(self)
        self.loadingBar.setStyleSheet("background-color: #bffed3")
        self.loadingBar.setGeometry(self.sw*400, self.sh*420, self.sw*200, self.sh*25)
        self.startBtn = QPushButton("Start", self)
        self.startBtn.move(self.sw*450, self.sh*460)
        self.startBtn.clicked.connect(self.startProgressBar)

        self.newbtn = QPushButton("Go Back", self)
        self.newbtn.setStyleSheet("background-color: #91edb9; font-weight: bold; border: 5px solid; border-color: white")
        self.newbtn.setGeometry(self.sw * 413, self.sh * 565, self.sw * 180, self.sh * 40)
        self.newbtn.clicked.connect(self.on_back)

        self.mood_window()
        self.show()

    def mood_window(self):
        # Labels
        Person.setLabel(self, "Analyzing", True, self.sw*390, self.sh*200, self.sw*220, self.sh*35, self.sw*19, "white", False, 'Segoe UI')
        Person.setLabel(self, "New", True, self.sw*270, self.sh*260, self.sw*450, self.sh*58, self.sw*25, "white", True, 'Segoe UI')
        Person.setLabel(self, "Songs", True, self.sw*385, self.sh*330, self.sw*220, self.sh*35, self.sw*19, "white", False, 'Segoe UI')

    def startProgressBar(self):
        from Moodipy.songsPrediction import songPredictions
        from Moodipy.PredictionGUI import PredictPG
        from Moodipy.ErrorPagePredict import ErrorPredictPG
        from Moodipy.ErrorNoPop import ErrorNoPopSongs
        self.startBtn.setEnabled(False)
        self.newbtn.setEnabled(False)

        Person.tracks = songPredictions(self.loadingBar)

        if Person.tracks == None:
            self.nextPg = ErrorPredictPG()
            self.nextPg.show()
            self.hide()
        elif Person.tracks == "NO SONGS":
            self.nextPg = ErrorNoPopSongs()
            self.nextPg.show()
            self.hide()
        else:
            self.nextPg = PredictPG()
            self.nextPg.show()
            self.hide()

    def on_back(self):
        from Moodipy.DiscoverPgGUI import DiscoverPG
        self.startBtn.setEnabled(False)
        self.newbtn.setEnabled(False)
        self.nextPg = DiscoverPG()
        self.nextPg.show()
        self.hide()

    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(self.sw*270, self.sh*70, self.sw*450, self.sh*450)

