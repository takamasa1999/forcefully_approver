from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from settings import main_settings
from tools import MyCounter
import random
import sys

global rejected_amount_list
rejected_amount_list = []

class SecondPage(QWidget):

    def __init__(self, pos_x=main_settings["center_pos_for_sub_window_x"], pos_y=main_settings["center_pos_for_sub_window_y"], display_comment=""):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.display_comment = display_comment
        super().__init__()
        self.initUI()
    
    def button_yes_click(self):
        sys.exit()

    def button_no_click(self):
        rejected_amount_list.append("rejected")
        rejected_amount_int = len(rejected_amount_list)
        display_generate_amounts = rejected_amount_int**2

        for i in range(display_generate_amounts):
            window_half_width = main_settings["sub_window_width"]//2
            window_half_height = main_settings["sub_window_height"]//2
            random_step = 1
            pos_x = main_settings["center_pos_for_sub_window_x"] + random.randrange(-window_half_width, window_half_width, random_step)
            pos_y = main_settings["center_pos_for_sub_window_y"] + random.randrange(-window_half_height, window_half_height, random_step)
            exec(f"self.new_ex_{i} = SecondPage(pos_x=pos_x, pos_y=pos_y, display_comment=self.display_comment)")
            exec(f"self.new_ex_{i}.show()")

    def initUI(self):

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.setWindowIcon(QIcon(main_settings["window_icon_dir"]))
        self.setWindowTitle("You can't say \"No\" technically...")
        self.resize(main_settings["sub_window_width"], main_settings["sub_window_height"])
        self.move(self.pos_x, self.pos_y)

        counter = MyCounter()

        label = QLabel(self.display_comment)
        label.setWordWrap(True)
        grid_layout.addWidget(label, counter.get_count_and_add_one(), 0, 1, 1)

        button_yes = QPushButton('Yes')
        button_yes.clicked.connect(self.button_yes_click)
        grid_layout.addWidget(button_yes, counter.get_count_and_add_one(), 0, 1, 1)

        button_no = QPushButton('No')
        button_no.clicked.connect(self.button_no_click)
        grid_layout.addWidget(button_no, counter.get_count(), 1, 1, 1)