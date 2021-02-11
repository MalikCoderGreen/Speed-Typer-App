import random
import difflib
from sentDict import sentences
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSlot, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QPalette

"""

*** PyQt5 speed typing application ***

Author: 
Maliak Green 

Date created: 
02/09/2021

Description:
This app chooses a random sentence from a dictionary of sentences and times the user's-
attempt at typing the exact sentence shown on the GUI. After the user submits their sentence, 
the program will get their time it took to type and the accuracy compared to the random sentence.

Conditions: 
- Must type all the same letters shown in sentence. 
- Must type all the same grammar symbols used in the sentence i.e. "' , - ; :". 

"""

# Main GUI window class.
class MainWindow(QMainWindow): 
    
    def __init__(self):
        super().__init__()
        # Set window properties. 
        self.setWindowTitle("Speed Typer")
        self.my_font = QFont("Helvetica [Cronyx]", 20, QFont.Bold)

        self.my_style = "color: rgb(255, 215, 0)"
        
        self.create_widgets()
        self.setGeometry(200, 200, 1000, 500)

        # Window color. 
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(self.p)



        # Random sentence from dictionary. 
        self.sentence = ""
    


    def create_widgets(self):
        """ 
        Method: Intialize all UI widgets.  
        """

        # Button to generate sentence from dictionary. 
        self.getSent = QPushButton("Start", self)
        self.getSent.setGeometry(440, 20, 100, 45)
        self.getSent.clicked.connect(self.generate_S)
        self.getSent.setFont(self.my_font)

        # Button to close application. 
        self.closeBtn = QPushButton("Quit", self)
        self.closeBtn.setGeometry(440, 300, 100, 45)
        self.closeBtn.clicked.connect(self.close)
        self.closeBtn.setFont(self.my_font)


        # User attempt to type sentence. 
        self.usrAttempt = QLineEdit(self)
        self.usrAttempt.setGeometry(180, 175, 600, 30)
        self.usrAttempt.returnPressed.connect(self.fireTimer)

        # Submit user attempt.
        self.subBtn = QPushButton("submit", self)
        self.subBtn.setGeometry(780, 170, 100, 45)
        self.subBtn.clicked.connect(self.getAccuracy)
        self.subBtn.setFont(self.my_font)
    

        # Label to show random sentence. 
        self.sentLabel = QLabel("", self)
        self.sentLabel.setGeometry(140, 120, 800, 50)
        self.sentLabel.setFont(self.my_font)
        self.sentLabel.setStyleSheet(self.my_style)

        self.disclaimer = QLabel("Once you press start, you will display a sentence and be timed. Be ready!", self)
        self.disclaimer.setGeometry(140, 60, 700, 50)
        self.disclaimer.setFont(self.my_font)
        self.disclaimer.setStyleSheet(self.my_style)

        # Labels to show accuracy and time results. 
        self.accLabel = QLabel("", self)
        self.accLabel.setGeometry(250, 200, 200, 50)
        self.accLabel.setFont(self.my_font)
        self.accLabel.setStyleSheet(self.my_style)

        self.timerLabel = QLabel("", self)
        self.timerLabel.setGeometry(500, 200, 200, 50)
        self.timerLabel.setFont(self.my_font)
        self.timerLabel.setStyleSheet(self.my_style)


        # Timer object to record time it took for user to type. 
        self.curr_time = QTime(00, 00, 00)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.fireTimer)

    

    
    def generate_S(self):
        """  
        Method: Get random sentence from dictionary. 
        """
        
        self.disclaimer.hide()
        self.accLabel.hide()
        self.timerLabel.hide()

        self.timer.start()

        self.sentence = sentences[ random.randrange(0, len(sentences) - 1) ]
        self.sentence = self.sentence.rstrip()

        self.sentLabel.setText(self.sentence)

        self.usrAttempt.setText("")
        
    
    def getAccuracy(self):
        """
        Method: Get user's attempt from UI and compute accuracy. 
        """

        self.timer.stop()
        attempt = self.usrAttempt.text()
        
        # Compute string comparison accuracy with SequenceMatcher func from difflib library.
        acc = difflib.SequenceMatcher(None, attempt, self.sentence)
        result = acc.ratio() * 100
        result = str(round(result, 2))
        
        # Update result labels. 
        self.accLabel.setText(f'Accuracy: {result}%')
        self.timerLabel.setText(f'Time: {self.curr_time.toString("hh:mm:ss")}')
        self.accLabel.show()
        self.timerLabel.show()
        
        # Reset time for label and reset value for user-attempt line edit.
        self.curr_time.setHMS(00, 00, 00)
      

    def fireTimer(self):
        """  
        Method: Fire timer when user starts typing. 
        """

        self.curr_time = self.curr_time.addSecs(1)





# Create instance and start app loop. 
app = QApplication([])
window = MainWindow()

window.show()
app.exec_()




