import os
from PyQt5 import uic
from PyQt5.QtWidgets import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Get the address of the ui file
        # Assuming that the ui file is in the same folder as this python file
        ui_file_address = os.path.dirname(__file__) + '\\my_simple_ui.ui'

        # Load the main widget and its children from the ui file
        myWidget = uic.loadUi(ui_file_address,self)

        # Connect the click event of the submit button with the method action_submit
        self.pushButton_submit.clicked.connect(self.action_submit)

    def action_submit(self):
        # Copy the text from lineEdit to label_output
        self.label_output.setText(self.lineEdit.text())

# Create an application object
app = QApplication([])

# Create the main widget
mainWidget = MainWidget()

# Show the main widget
mainWidget.show()

# Run the app
app.exec()
