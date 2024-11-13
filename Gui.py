# -- coding: utf-8 --

################################################################################
## Form generated from reading UI file 'untitledaqBoGg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(817, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Start_training = QWidget()
        self.Start_training.setObjectName(u"Start_training")

        self.pushButton_2 = QPushButton(self.Start_training)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 50, 109, 28))
        self.label = QLabel(self.Start_training)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 251, 61))
        self.label_2 = QLabel(self.Start_training)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 90, 151, 71))
        self.checkBox = QCheckBox(self.Start_training)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(0, 320, 311, 61))
        self.pushButton = QPushButton(self.Start_training)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 510, 121, 41))
        self.tableWidget = QTableWidget(self.Start_training)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 140, 401, 171))
        self.tableWidget.setMinimumSize(QSize(0, 171))
        self.tableWidget.setMaximumSize(QSize(601, 16777215))
        self.lineEdit = QLineEdit(self.Start_training)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 241, 31))
        self.lineEdit_2 = QLineEdit(self.Start_training)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 400, 231, 31))
        self.label_3 = QLabel(self.Start_training)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 380, 251, 16))
        self.label_total_duration = QLabel(self.Start_training)
        self.label_total_duration.setObjectName(u"label_4")
        self.label_total_duration.setGeometry(QRect(280, 460, 121, 31))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_duration.setFont(font)
        self.label_5 = QLabel(self.Start_training)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 460, 181, 31))
        self.label_5.setFont(font)
        self.tabWidget.addTab(self.Start_training, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 20, 161, 41))
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 50, 261, 31))
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 90, 161, 41))
        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 120, 261, 31))
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 160, 161, 41))
        self.lineEdit_5 = QLineEdit(self.tab)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 200, 261, 31))
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete Participant", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Participant ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Training History:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Show all training history\n"
"", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Training Number \n"
"", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date \n"
"", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Training type\n"
"", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Score\n"
"", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Training type:", None))
        self.label_total_duration.setText(QCoreApplication.translate("MainWindow", u"Total duration:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Start_training), QCoreApplication.translate("MainWindow", u"Start training ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Create training ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Participant full name: \n"
"", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Participant ID: \n"
"", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Add new participant ", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
