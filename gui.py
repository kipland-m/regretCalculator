# Inside this file will live the GUI for RegretCalculator,
# Being built in PyQt5
# 04/13/2021
# Kipland Melton

import sys
from PyQt5.QtWidgets import QApplication, QLabel

class Window():

    def __init__(self):
        super().__init__()
        app = QApplication([])
        label = QLabel("test oop")
        label.show()
        app.exec_()


if __name__ == "__main__":
    Window()


