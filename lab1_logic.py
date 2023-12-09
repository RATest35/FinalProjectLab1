from PyQt6.QtWidgets import *
from lab1_gui import *


class Logic(QMainWindow, Ui_MainWindow):
    __zoey_votes: int
    __jane_votes: int
    __stph_votes: int
    __bob_votes: int
    __george_votes: int
    __jill_votes: int
    __PASSWORD = 'America Freedom'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__zoey_votes = 0
        self.__jane_votes = 0
        self.__stph_votes = 0
        self.__bob_votes = 0
        self.__george_votes = 0
        self.__jill_votes = 0

        self.home_btn.clicked.connect(lambda: self.go_home())
        self.vote_btn.clicked.connect(lambda: self.go_vote())
        self.confirm_btn.clicked.connect(lambda: self.cast_vote())
        self.exit_btn.clicked.connect(lambda: self.exit())
        self.pass_confirm_btn.clicked.connect(lambda: self.check_password())
        self.pass_home_btn.clicked.connect(lambda: self.go_home())
        self.close_btn.clicked.connect(lambda: quit())

    def go_home(self) -> None:
        """
        sets the page to the home page and sets the placeholder text for password input to ''
        :return:
        """
        self.stackedWidget.setCurrentIndex(0)
        self.pass_input.setPlaceholderText('')

    def go_vote(self) -> None:
        """
        sets page to the candidates menu
        :return:
        """
        self.stackedWidget.setCurrentIndex(1)

    def cast_vote(self) -> None:
        """
        adds one to the total votes of the candidate selected then sends the user to the home page
        :return:
        """
        if self.zoey_radio.isChecked():
            self.__zoey_votes += 1
        elif self.jane_radio.isChecked():
            self.__jane_votes += 1
        elif self.stephan_radio.isChecked():
            self.__stph_votes += 1
        elif self.bob_radio.isChecked():
            self.__bob_votes += 1
        elif self.george_radio.isChecked():
            self.__george_votes += 1
        elif self.jill_radio.isChecked():
            self.__jill_votes += 1
        self.go_home()

    def exit(self) -> None:
        """
        sets the page to the password page
        :return:
        """
        self.stackedWidget.setCurrentIndex(3)

    def vote_counter(self) -> None:
        self.zoey_total.setText(f'Zoey: {self.__zoey_votes}')
        self.jane_total.setText(f'Jane: {self.__jane_votes}')
        self.stephan_total.setText(f'Stephan: {self.__stph_votes}')
        self.bob_total.setText(f'Bob: {self.__bob_votes}')
        self.george_total.setText(f'George: {self.__george_votes}')
        self.jill_total.setText(f'Jill: {self.__jill_votes}')
        total = self.__zoey_votes + self.__jane_votes + self.__stph_votes + self.__bob_votes + self.__george_votes + self.__jill_votes
        self.all_votes.setText(f'Total Votes: {total}')

    def check_password(self) -> None:
        inputted_pass = self.pass_input.text().strip()
        if inputted_pass == Logic.__PASSWORD:
            self.vote_counter()
            self.stackedWidget.setCurrentIndex(2)
            self.pass_input.setPlaceholderText('')
        else:
            self.pass_input.setPlaceholderText('Incorrect Password')
            self.pass_input.setText('')
