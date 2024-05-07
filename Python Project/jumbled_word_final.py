import sys
# defines a series of functions for generating or manipulating random integers
import random 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Jumbled(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jumbled Word")
 
        # setting geometry
        self.setGeometry(100, 100, 320, 350)
 
        # calling method
        self.UiComponents()
 
        # to show all the widgets
        self.show()
 
        # keywords
        self.words = ['PYTHON', 'PROGRAM', 'DEVELOPER', 'PROGRAMMER', 
                      'DEVICE', 'DEVELOP', 'VARIABLES', 'COMMAND', 
                      'KEYBOARD', 'MOUSE', 'MONITOR', 'DESKTOP']


        self.current_text = ""
 
    # method for components
    def UiComponents(self):
 
        # creating head label
        head = QLabel("Jumbled Word Game", self)
 
        # setting position to the header
        head.setGeometry(20, 10, 280, 60)
 
        # font styles
        font = QFont('Times', 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
 
        # setting font to the head
        head.setFont(font)
 
        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
 
        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.blue)
        head.setGraphicsEffect(color)
 
        # creating label to show the jumbled word
        self.j_word = QLabel(self)
        self.j_word.setGeometry(30, 80, 260, 50)
 
        # setting style sheet
        self.j_word.setStyleSheet("border : 5px solid black; background : darkcyan;")
 
        # setting font
        self.j_word.setFont(QFont('Times', 12))
 
        # setting alignment
        self.j_word.setAlignment(Qt.AlignCenter)
 
 
        # creating a line edit widget to get the text
        self.input = QLineEdit(self)
        self.input.setGeometry(20, 150, 200, 40)
 
        # setting alignment
        self.input.setAlignment(Qt.AlignCenter)
 
        # creating push button to check the input
        self.check = QPushButton("Check", self)
        self.check.setGeometry(230, 155, 80, 30)
 
        # adding action to the check button
        self.check.clicked.connect(self.check_action)
 
        # result label
        self.result = QLabel(self)
        self.result.setGeometry(40, 210, 240, 50)
 
        # setting font
        self.result.setFont(QFont('Times', 13))
 
        # setting alignment
        self.result.setAlignment(Qt.AlignCenter)
 
        # setting style sheet
        self.result.setStyleSheet("border : 5px solid black; background : yellow;")
 
        # creating push buttons to start and reset the game
        start = QPushButton("Start", self)
        reset = QPushButton("Reset", self)
        start.setGeometry(15, 290, 140, 40)
        reset.setGeometry(165, 290, 140, 40)
 
        # adding action to the buttons
        start.clicked.connect(self.start_action)
        reset.clicked.connect(self.reset_action)
 
    def check_action(self):
 
        # getting text from the line edit
        text = self.input.text()
 
        # checking answers
        if text == self.current_text:
            self.result.setText("Correct Answer")
            self.result.setStyleSheet("background : lightgreen;")
 
        else:
            self.result.setText("Wrong Answer")
            self.result.setStyleSheet("background : red;")
 
 
    # play function 
    def start_action(self):
 
        # selecting a word on words pool
        self.current_text = random.choice(self.words)
 
        # sample() method for shuffling the characters of the word
        random_word = random.sample(self.current_text, len(self.current_text))
 
        # join() method join the elements of the iterator(e.g. list) with particular character .
        jumbled = ''.join(random_word)
 
        # setting text to the jumbled word
        self.j_word.setText(jumbled)
 
        # setting result text to blank
        self.result.setText("")
        self.result.setStyleSheet("border : 5px solid black; background : yellow;")
 
        # setting text of input to blank
        self.input.setText("")
        
    # restart function
    def reset_action(self):
 
        # setting current text to blank
        self.current_text = ""
 
        # setting text of input to blank
        self.input.setText("")
 
        # clearing the text of all the labels
        self.j_word.setText("")
        self.result.setText("")
        self.result.setStyleSheet("border : 5px solid black; background : yellow;")
 
 
App = QApplication(sys.argv)
jumbled = Jumbled()
sys.exit(App.exec())
