import sys
from PyQt5.QtWidgets import QApplication
from first_page import FirstPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_page = FirstPage()
    first_page.show()
    sys.exit(app.exec_())