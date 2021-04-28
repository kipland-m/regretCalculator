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
    	self.first_val = qtw.QLineEdit(self)
    	self.second_val = qtw.QLineEdit(self)
    	self.shares_val = qtw.QLineEdit(self)
    	self.btn_result = qtw.QPushButton("Calculate",self)
		
    	# Now you must add the buttons to the layout
    	# With each addWidget 

    	container.layout().addWidget(first_val_label,0,0,1,1)
    	container.layout().addWidget(second_val_label,0,1,1,1)
    	container.layout().addWidget(shares_val_label,0,2,1,1)

    	container.layout().addWidget(self.first_val,1,0,1,1)
    	container.layout().addWidget(self.second_val,1,1,1,1)
    	container.layout().addWidget(self.shares_val,1,2,1,1)

    	container.layout().addWidget(self.btn_result,2,1,1,1)

    	self.btn_result.clicked.connect(self.on_click)

    	self.layout().addWidget(container)

    def val_input(self, text):
    	textBoxValue = self.first_val.text()
    	QMessageBox.question(self,'message','you typed'+textBoxValue,QMessageBox.ok,QMessageBox.ok)
    	self.first_val.setText("")



if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
