from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout, QTabWidget
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import QTimer
import sys

# GUI class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._main_window = MainWindow
        if self._main_window.objectName():
            self._main_window.setObjectName(u"MainWindow")
        self._main_window.resize(830, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(755, 578))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)



#Tab 1: START EXERCISE 
        self.Start_exercise = QWidget()
        self.Start_exercise.setObjectName(u"Start_exercise")
        self.tabWidget.addTab(self.Start_exercise, "")

        # Add Delete Participant button
        self.Delete_participant = QPushButton(self.Start_exercise)
        self.Delete_participant.setObjectName(u"Delete_participant")
        self.Delete_participant.setGeometry(QRect(250, 50, 141, 31))
        self.Delete_participant.setFont(font)

        
        #action to delete participant
        self.Delete_participant.clicked.connect(self._main_window.delete_participant)
        
        self.Participant_ID = QLabel(self.Start_exercise)
        self.Participant_ID.setObjectName(u"Participant_ID")
        self.Participant_ID.setGeometry(QRect(0, 0, 251, 61))
        self.Participant_ID.setFont(font)

        self.Participant_ID_label = QComboBox(self.Start_exercise)
        self.Participant_ID_label.setObjectName(u"Participant_ID_label")
        self.Participant_ID_label.setGeometry(QRect(10, 50, 231, 31))
        self.Participant_ID_label.setFont(font)
        
        #define the table title
        self.exercise_history = QLabel(self.Start_exercise)
        self.exercise_history.setObjectName(u"exercise_history")
        self.exercise_history.setGeometry(QRect(0, 80, 151, 71))
        self.exercise_history.setFont(font)
        
        self.table_exercise_history_Widget = QTableWidget(self.Start_exercise)
        if (self.table_exercise_history_Widget.columnCount() < 4):
            self.table_exercise_history_Widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_exercise_history_Widget.setObjectName(u"table_exercise_history_Widget")
        self.table_exercise_history_Widget.setGeometry(QRect(10, 140, 600, 250))
        self.table_exercise_history_Widget.setMinimumSize(QSize(500, 200))
        self.table_exercise_history_Widget.setMaximumSize(QSize(550, 150))
        self.table_exercise_history_Widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        #checkBox to show the exercise history
        self.show_exercise_history = QCheckBox(self.Start_exercise)
        self.show_exercise_history.setObjectName(u"show_exercise_history")
        self.show_exercise_history.setGeometry(QRect(0, 330, 311, 61))
        self.show_exercise_history.setFont(font)
        
        #choose the exercise type from the comboBox
        self.exercise_type = QLabel(self.Start_exercise)
        self.exercise_type.setObjectName(u"exercise_type")
        self.exercise_type.setGeometry(QRect(0, 390, 251, 16))
        self.exercise_type.setFont(font)
        self.Exercise_type_label = QComboBox(self.Start_exercise)
        self.Exercise_type_label.setObjectName(u"Exercise_type_label")
        self.Exercise_type_label.setGeometry(QRect(10, 420, 231, 31))
        self.Exercise_type_label.setFont(font)
        
        #button to start the exercise (and the timer to show the running time)
        self.Start_button_tab1 = QPushButton(self.Start_exercise)
        self.Start_button_tab1.setObjectName(u"Start_button_tab1")
        self.Start_button_tab1.setGeometry(QRect(320, 510, 121, 41))
        self.Start_button_tab1.setFont(font)

        # #connect the button click to the start_timer function
        # self.Start_button_tab1.clicked.connect(self.start_timer)
        # def start_timer(self):
        #     self.timer = QTimer()
        #     self.timer.timeout.connect(self.update_time)
        #     self.timer.start(1000)                      # Update every 1000 milliseconds (1 second)
        #     self.start_button.setEnabled(False)         # Disable the button to prevent multiple starts
        #     self.running_time.setText("00:00:00")
        #     self.timer.start()
        # def update_time(self):                          #Update the time label with the elapsed time.
        #     self.elapsed_seconds += 1
        # # Calculate hours, minutes, and seconds
        #     hours = self.elapsed_seconds // 3600
        #     minutes = (self.elapsed_seconds % 3600) // 60
        #     seconds = self.elapsed_seconds % 60

        # # Update the label
        # self.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        


        self.Total_duration = QLabel(self.Start_exercise)
        self.Total_duration.setObjectName(u"Total_duration")
        self.Total_duration.setGeometry(QRect(270, 460, 121, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.Total_duration.setFont(font1)
        
        self.running_time = QLabel(self.Start_exercise)
        self.running_time.setObjectName(u"running_time")
        self.running_time.setGeometry(QRect(410, 460, 181, 31))
        self.running_time.setFont(font1)

        

      

#Tab 2: CREATE EXERCISE 
        self.Creat_exercise = QWidget()
        self.Creat_exercise.setObjectName(u"Creat_exercise")
        self.tabWidget.addTab(self.Creat_exercise, "")
        

        self.Exercise_name = QLabel(self.Creat_exercise)
        self.Exercise_name.setObjectName(u"Exercise_name")
        self.Exercise_name.setGeometry(QRect(0, 0, 251, 61))
        self.Exercise_name.setFont(font)
        
        self.ExerciseName_label_tab2 = QLineEdit(self.Creat_exercise)
        self.ExerciseName_label_tab2.setObjectName(u"ExerciseName_label_tab2")
        self.ExerciseName_label_tab2.setGeometry(QRect(10, 50, 231, 31))
        self.ExerciseName_label_tab2.setFont(font)
        
        self.TotalExerciseDuration_label_tab2 = QLabel(self.Creat_exercise)
        self.TotalExerciseDuration_label_tab2.setObjectName(u"TotalExerciseDuration_label_tab2")
        self.TotalExerciseDuration_label_tab2.setGeometry(QRect(0, 90, 161, 41))
        self.TotalExerciseDuration_label_tab2.setFont(font)
        
        self.SetTotalExeDuration = QSpinBox(self.Creat_exercise)
        self.SetTotalExeDuration.setObjectName(u"SetTotalExeDuration")
        self.SetTotalExeDuration.setGeometry(QRect(10, 130, 231, 31))
        self.SetTotalExeDuration.setFont(font)

        #checkBox to calculate the total duration of the exercise in order to set the amount of perturbation
        self.SaveExercise_checkBox = QCheckBox(self.Creat_exercise)
        self.SaveExercise_checkBox.setObjectName(u"SaveExercise_checkBox")
        self.SaveExercise_checkBox.setGeometry(QRect(270, 140, 81, 20))
        self.SaveExercise_checkBox.setFont(font)

        #create perturbation table
        self.SetDesiredPertub_label_tab2 = QLabel(self.Creat_exercise)
        self.SetDesiredPertub_label_tab2.setObjectName(u"SetDesiredPertub_label_tab2")
        self.SetDesiredPertub_label_tab2.setGeometry(QRect(0, 200, 211, 31))
        self.SetDesiredPertub_label_tab2.setFont(font)
        
        self.Perturbation_time = QLabel(self.Creat_exercise)
        self.Perturbation_time.setObjectName(u"Perturbation_time")
        self.Perturbation_time.setGeometry(QRect(0, 250, 131, 24))
        self.Perturbation_time.setFont(font)
        
        self.PertubationType_label_tab2 = QLabel(self.Creat_exercise)
        self.PertubationType_label_tab2.setObjectName(u"PertubationType_label_tab2")
        self.PertubationType_label_tab2.setGeometry(QRect(0, 290, 141, 24))
        self.PertubationType_label_tab2.setFont(font)
        
        self.PertubationDegrees_label_tab2 = QLabel(self.Creat_exercise)
        self.PertubationDegrees_label_tab2.setObjectName(u"PertubationDegrees_label_tab2")
        self.PertubationDegrees_label_tab2.setGeometry(QRect(0, 330, 151, 24))
        self.PertubationDegrees_label_tab2.setFont(font)
        
        self.Speed_label_tab2 = QLabel(self.Creat_exercise)
        
        self.Speed_label_tab2.setObjectName(u"Speed_label_tab2")
        self.Speed_label_tab2.setGeometry(QRect(0, 370, 81, 24))
        self.Speed_label_tab2.setFont(font)
        
        self.Perturbation_type = QComboBox(self.Creat_exercise)
        Perturbation_list = ['-','Left', 'Right', 'Forward','Backward','No perturbations']
        self.Perturbation_type.addItems(Perturbation_list)
        self.Perturbation_type.setObjectName(u"Perturbation_type")
        self.Perturbation_type.setGeometry(QRect(180, 290, 141, 31))
        self.Perturbation_type.setFont(font)
        
        self.Speed = QComboBox(self.Creat_exercise)
        Speed_list = ['-','1','2','3','4','5','6','7','8','9','10']
        self.Speed.addItems(Speed_list)
        self.Speed.setObjectName(u"Speed")
        self.Speed.setGeometry(QRect(180, 370, 141, 31))
        self.Speed.setFont(font)
        
        self.SetPertubTime = QSpinBox(self.Creat_exercise)
        self.SetPertubTime.setObjectName(u"SetPertubTime")
        self.SetPertubTime.setGeometry(QRect(180, 250, 141, 31))
        self.SetPertubTime.setFont(font)
        
        self.Addpertub_button_tab2 = QPushButton(self.Creat_exercise)
        self.Addpertub_button_tab2.setObjectName(u"Addpertub_button_tab2")
        self.Addpertub_button_tab2.setGeometry(QRect(20, 420, 121, 41))
        self.Addpertub_button_tab2.setFont(font)
        
        self.AddExercise_button_tab2 = QPushButton(self.Creat_exercise)
        self.AddExercise_button_tab2.setObjectName(u"AddExercise_button_tab2")
        self.AddExercise_button_tab2.setGeometry(QRect(310, 510, 131, 41))
        self.AddExercise_button_tab2.setFont(font)
        
        self.DeleteExercise_button_tab2 = QPushButton(self.Creat_exercise)
        self.DeleteExercise_button_tab2.setObjectName(u"DeleteExercise_button_tab2")
        self.DeleteExercise_button_tab2.setGeometry(QRect(270, 50, 121, 31))
        self.DeleteExercise_button_tab2.setFont(font)
        
        self.PertubationtableWidget = QTableWidget(self.Creat_exercise)
        self.PertubationtableWidget.setObjectName(u"PertubationtableWidget")
        self.PertubationtableWidget.setGeometry(QRect(490, 200, 256, 192))
        
        self.ClearTable_button_tab2 = QPushButton(self.Creat_exercise)
        self.ClearTable_button_tab2.setObjectName(u"ClearTable_button_tab2")
        self.ClearTable_button_tab2.setGeometry(QRect(530, 410, 171, 41))
        self.ClearTable_button_tab2.setFont(font)
        
        self.SaveEditTable_checkBox = QCheckBox(self.Creat_exercise)
        self.SaveEditTable_checkBox.setObjectName(u"SaveEditTable_checkBox")
        self.SaveEditTable_checkBox.setGeometry(QRect(170, 430, 211, 21))
        self.SaveEditTable_checkBox.setFont(font)
        
        self.Perturbation_degrees = QDoubleSpinBox(self.Creat_exercise)
        self.Perturbation_degrees.setObjectName(u"Perturbation_degrees")
        self.Perturbation_degrees.setGeometry(QRect(180, 330, 141, 31))
        
        

#Tab 3: Add new participant
        self.Add_new_participant = QWidget()
        self.Add_new_participant.setObjectName(u"Add_new_participant")
        self.tabWidget.addTab(self.Add_new_participant, "")

        
        self.FullName_label_tab3 = QLabel(self.Add_new_participant)
        self.FullName_label_tab3.setObjectName(u"FullName_label_tab3")
        self.FullName_label_tab3.setGeometry(QRect(0, 10, 161, 41))
        self.FullName_line_tab3 = QLineEdit(self.Add_new_participant)
        self.FullName_line_tab3.setObjectName(u"FullName_line_tab3")
        self.FullName_line_tab3.setGeometry(QRect(10, 50, 261, 31))
        
        self.ParticipantID_label_tab3 = QLabel(self.Add_new_participant)
        self.ParticipantID_label_tab3.setObjectName(u"ParticipantID_label_tab3")
        self.ParticipantID_label_tab3.setGeometry(QRect(0, 90, 161, 41))
        self.ParticipantID_line_tab3 = QLineEdit(self.Add_new_participant)
        self.ParticipantID_line_tab3.setObjectName(u"ParticipantID_line_tab3")
        self.ParticipantID_line_tab3.setGeometry(QRect(10, 130, 261, 31))

        self.Gender_label_tab3 = QLabel(self.Add_new_participant)
        self.Gender_label_tab3.setObjectName(u"Gender_label_tab3")
        self.Gender_label_tab3.setGeometry(QRect(0, 170, 161, 41))
        self.Gender = QComboBox(self.Add_new_participant)
        Gender_list = ['-','male','female']
        self.Gender.addItems(Gender_list)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setGeometry(QRect(10, 210, 131, 31))
        
        self.Age_label_tab3 = QLabel(self.Add_new_participant)
        self.Age_label_tab3.setObjectName(u"Age_label_tab3")
        self.Age_label_tab3.setGeometry(QRect(0, 250, 161, 41))
        self.Age_label_tab3.setFont(font)
        self.lineEdit_age = QLineEdit(self.Add_new_participant)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setGeometry(QRect(10, 290, 131, 31))
        self.lineEdit_age.setFont(font)
        
        self.Height_label_tab3 = QLabel(self.Add_new_participant)
        self.Height_label_tab3.setObjectName(u"Height_label_tab3")
        self.Height_label_tab3.setGeometry(QRect(0, 330, 161, 41))
        self.SetHeight = QDoubleSpinBox(self.Add_new_participant)
        self.SetHeight.setObjectName(u"SetHeight")
        self.SetHeight.setGeometry(QRect(10, 370, 131, 31))
        
        self.Weight_label_tab3 = QLabel(self.Add_new_participant)
        self.Weight_label_tab3.setObjectName(u"Weight_label_tab3")
        self.Weight_label_tab3.setGeometry(QRect(0, 410, 161, 41))
        self.SetWeight = QDoubleSpinBox(self.Add_new_participant)
        self.SetWeight.setObjectName(u"SetWeight")
        self.SetWeight.setGeometry(QRect(10, 450, 131, 31))

        self.AddParticipant_button_tab3 = QPushButton(self.Add_new_participant)
        self.AddParticipant_button_tab3.setObjectName(u"AddParticipant_button_tab3")
        self.AddParticipant_button_tab3.setGeometry(QRect(320, 490, 151, 41))

        ######### DONE WITH THE TABS #########


        #set the current tab to the first tab
        self.tabWidget.setCurrentIndex(0)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    
   
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", u"MainWindow", None))
        self.Delete_participant.setText(_translate("MainWindow", u"Delete Participant", None))
        self.Participant_ID.setText(_translate("MainWindow", u"Participant ID:", None))
        self.exercise_history.setText(_translate("MainWindow", u"Exercise History:", None))
        self.show_exercise_history.setText(_translate("MainWindow", u"Show exercise history", None))
        self.Start_button_tab1.setText(_translate("MainWindow", u"START", None))
        ___qtablewidgetitem = self.table_exercise_history_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(_translate("MainWindow", u"Exercise Number \n"
"", None));
        ___qtablewidgetitem1 = self.table_exercise_history_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(_translate("MainWindow", u"Date \n"
"", None));
        ___qtablewidgetitem2 = self.table_exercise_history_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(_translate("MainWindow", u"Exercise type\n"
"", None));
        ___qtablewidgetitem3 = self.table_exercise_history_Widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(_translate("MainWindow", u"Score\n"
"", None));
        self.exercise_type.setText(_translate("MainWindow", u"Exercise name:", None))
        self.Total_duration.setText(_translate("MainWindow", u"Total duration:", None))
        self.running_time.setText(_translate("MainWindow", u"00:00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Start_exercise), _translate("MainWindow", u"Start training ", None))
        self.Exercise_name.setText(_translate("MainWindow", u"Exercise name:", None))
        self.TotalExerciseDuration_label_tab2.setText(_translate("MainWindow", u"Total exercise duration: ", None))
        self.SaveExercise_checkBox.setText(_translate("MainWindow", u"Save", None))
        self.SetDesiredPertub_label_tab2.setText(_translate("MainWindow", u"Set the desired perturbation:", None))
        self.Perturbation_time.setText(_translate("MainWindow", u"Perturbation time: ", None))
        self.PertubationType_label_tab2.setText(_translate("MainWindow", u"Perturbation type:", None))
        self.PertubationDegrees_label_tab2.setText(_translate("MainWindow", u"Perturbation degrees:", None))
        self.Speed_label_tab2.setText(_translate("MainWindow", u"Speed: ", None))
        self.Addpertub_button_tab2.setText(_translate("MainWindow", u"Add perturbation", None))
        self.AddExercise_button_tab2.setText(_translate("MainWindow", u"Add exercise", None))
        self.DeleteExercise_button_tab2.setText(_translate("MainWindow", u"Delete exercise", None))
        self.ClearTable_button_tab2.setText(_translate("MainWindow", u"Clear perturbation table", None))
        self.SaveEditTable_checkBox.setText(_translate("MainWindow", u"Save and edit table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Creat_exercise), _translate("MainWindow", u"Create training ", None))
        self.FullName_label_tab3.setText(_translate("MainWindow", u"Participant full name: ", None))
        self.ParticipantID_label_tab3.setText(_translate("MainWindow", u"Participant ID: ", None))
        self.Gender_label_tab3.setText(_translate("MainWindow", u"Gender:", None))
        self.Height_label_tab3.setText(_translate("MainWindow", u"Height [cm]: ", None))
        self.Weight_label_tab3.setText(_translate("MainWindow", u"Weight [Kg]: ", None))
        self.Age_label_tab3.setText(_translate("MainWindow", u"Age: ", None))
        self.AddParticipant_button_tab3.setText(_translate("MainWindow", u"Add participant", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add_new_participant), _translate("MainWindow", u"Add new participant ", None))
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Logic for tab 1:
        # Connect the Delete_participant button to the delete_participant method
        #self.ui.Delete_participant.clicked.connect(self.delete_participant)
    
    def delete_participant(self):
        print("Delete Participant button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())