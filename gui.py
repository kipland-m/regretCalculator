# Inside this file will live the GUI for RegretCalculator,
# Being built in PyQt5
# 04/13/2021
# Kipland Melton

import sys
import PyQt5.QtWidgets as qtw

# Widgets go here
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("regretCalculator")
        self.setLayout(qtw.QVBoxLayout())
        
    def calc(self):

        value_entry1 = qtw.QLineEdit()
        value_entry2 = qtw.QLineEdit()
        stock_amount = qtw.QLineEdit()

        btn_calculate = QPushButton('Calculate')

        self.layout().addWidget(btn1)

        self.show()

if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()


