import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QComboBox, QPushButton, QHBoxLayout

def window():
    app = QApplication(sys.argv)
    win = QMainWindow() # Create a window in application
    win.setGeometry(300, 300, 800, 600) # setting size of window and position on the screen - (x, y, width, height)
    win.setWindowTitle("DFG - BGU")

# Create a tab widget
    tab_widget = QTabWidget()
    win.setCentralWidget(tab_widget)

    # Create tabs
    tab1 = QWidget()
    tab2 = QWidget()
    tab3 = QWidget()

    # Add tabs to the tab widget
    tab_widget.addTab(tab1, "Start Exercise")
    tab_widget.addTab(tab2, "Create Exercise")
    tab_widget.addTab(tab3, "Add User")

   # Add content to tab1
    tab1_layout = QVBoxLayout()
    tab1_label = QLabel("User ID")
    tab1_label.setGeometry(100, 100, 200, 50)
    
    tab1_layout.addWidget(tab1_label)

    # Create a horizontal layout for the combo box and delete button
    combo_layout = QHBoxLayout()
    combo_label = QLabel("Select Exercise:")
    combo_box = QComboBox()
    combo_box.addItems(["Exercise 1", "Exercise 2", "Exercise 3"])
    delete_button = QPushButton("Delete")

    # Add widgets to the horizontal layout
    combo_layout.addWidget(combo_label)
    combo_layout.addWidget(combo_box)
    combo_layout.addWidget(delete_button)

    # Add the horizontal layout to the main layout of tab1
    tab1_layout.addLayout(combo_layout)
    tab1.setLayout(tab1_layout)

    # Add content to tab2
    tab2_layout = QVBoxLayout()
    tab2_label = QLabel("Content for Create Exercise")
    tab2_layout.addWidget(tab2_label)
    tab2.setLayout(tab2_layout)

    # Add content to tab3
    tab3_layout = QVBoxLayout()
    tab3_label = QLabel("Content for Add A New User")
    tab3_layout.addWidget(tab3_label)
    tab3.setLayout(tab3_layout)
  
    win.show()
    sys.exit(app.exec_())  # for clean exit

window()  # call the function to run the window