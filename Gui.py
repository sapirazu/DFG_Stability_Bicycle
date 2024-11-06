import pyQt5.QtWidgets as qtw
import pyQt5.QtCore as qtc

class MainWindow(qtw.QWidget):
    def main_window(self):
        self.setWindowTitle('DFG Stability Bicycle')
        self.setLayout(qtw.QVBoxLayout())
        self.setGeometry(100,100,800,600)
        self.show()
        
        # create a label
        label = qtw.QLabel('Welcome to DFG Stability Bicycle')
        self.layout().addWidget(label)
        
        # create a button
        button = qtw.QPushButton('Click me', clicked = self.click_button)
        self.layout().addWidget(button)
