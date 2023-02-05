from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon
from settings import main_settings
from tools import MyCounter
from second_page import SecondPage

class FirstPage(QWidget):

    def __init__(self):
        self.pos_x = main_settings["center_pos_for_sub_window_x"]
        self.pos_y = main_settings["center_pos_for_sub_window_y"]
        super().__init__()
        self.initUI()

    def button_click_action(self):
        self.new_ex = SecondPage(display_comment=self.textarea.toPlainText())
        self.close()
        self.new_ex.show()

    def initUI(self):

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        self.setWindowIcon(QIcon(main_settings["window_icon_dir"]))

        self.setWindowTitle('Welcome to forcefully approver!')
        self.resize(main_settings["sub_window_width"], main_settings["sub_window_height"])
        self.move(self.pos_x, self.pos_y)

        counter = MyCounter()

        label = QLabel("Input something that you want to make somebody forcefully approve.")
        label.setWordWrap(True)
        grid_layout.addWidget(label, counter.get_count_and_add_one(), 0, 1, 1)

        self.textarea = QPlainTextEdit()
        grid_layout.addWidget(self.textarea, counter.get_count_and_add_one(), 0, 1, 1)

        button = QPushButton('Go to force it!')
        button.clicked.connect(self.button_click_action)
        grid_layout.addWidget(button, counter.get_count_and_add_one(), 0, 1, 1)