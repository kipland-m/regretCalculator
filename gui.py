# Inside this file will live the GUI for RegretCalculator,
# Being built in PyQt5
# 04/13/2021
# Kipland Melton

import sys
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):

	# The init method will declare all window logic (title, cont)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RegretCalculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()


        self.show()

    # This is going to holds all other elements
    def keypad(self):
    	container = qtw.QWidget()
    	container.setLayout(qtw.QGridLayout())

    	# Button Text labels
    	first_val_label = qtw.QLabel("First Value")
    	second_val_label = qtw.QLabel("Second Value")
    	shares_val_label = qtw.QLabel("# of Shares")

    	# Buttons
    	first_val = qtw.QLineEdit()
    	second_val = qtw.QLineEdit()
    	shares_val = qtw.QLineEdit()
    	btn_result = qtw.QPushButton("Calculate")

    	# Now you must add the buttons to the layout
    	# With each addWidget 

    	container.layout().addWidget(first_val_label,0,0,1,1)
    	container.layout().addWidget(second_val_label,0,1,1,1)
    	container.layout().addWidget(shares_val_label,0,2,1,1)

    	container.layout().addWidget(first_val,1,0,1,1)
    	container.layout().addWidget(second_val,1,1,1,1)
    	container.layout().addWidget(shares_val,1,2,1,1)

    	container.layout().addWidget(btn_result,2,1,1,1)

    	self.layout().addWidget(container)



if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
