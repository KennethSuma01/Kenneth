import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class JumbleWordGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.word_label = QLabel("Guess the jumbled country:")
        self.word_label.setStyleSheet("font-size: 18px;")

        self.word_display = QLabel()
        self.word_display.setStyleSheet("font-size: 24px;")

        self.input_box = QLineEdit()

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.checkWord)

        layout = QVBoxLayout()
        layout.addWidget(self.word_label)
        layout.addWidget(self.word_display)
        layout.addWidget(self.input_box)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

        self.generateWord()

        self.setWindowTitle("Jumble Country Game")
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def generateWord(self):
        countries = ['UNITED STATES', 'CANADA', 'AUSTRALIA', 'JAPAN', 'BRAZIL', 'GERMANY']
        self.country = random.choice(countries)
        self.jumbled_country = ''.join(random.sample(self.country, len(self.country)))
        self.word_display.setText(self.jumbled_country)

    def checkWord(self):
        guessed_country = self.input_box.text().strip().upper()
        if guessed_country == self.country:
            self.word_display.setText("Correct!")
            self.generateWord()
        else:
            self.word_display.setText("Try again!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JumbleWordGame()
    sys.exit(app.exec_())
