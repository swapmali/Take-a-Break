from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import time
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(286, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.start_button.setObjectName("start_button")
        self.input_break_time = QtWidgets.QLineEdit(self.centralwidget)
        self.input_break_time.setGeometry(QtCore.QRect(180, 10, 71, 31))
        self.input_break_time.setObjectName("input_break_time")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(180, 120, 75, 23))
        self.stop_button.setObjectName("stop_button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 271, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 50, 261, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 286, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionMade_with_love_India = QtWidgets.QAction(MainWindow)
        self.actionMade_with_love_India.setObjectName("actionMade_with_love_India")
        self.action_author_Swapnil_Mali = QtWidgets.QAction(MainWindow)
        self.action_author_Swapnil_Mali.setObjectName("action_author_Swapnil_Mali")
        self.actionLicence = QtWidgets.QAction(MainWindow)
        self.actionLicence.setObjectName("actionLicence")
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionMade_with_love_India)
        self.menuAbout.addAction(self.action_author_Swapnil_Mali)
        self.menuAbout.addAction(self.actionLicence)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.flg = 1
        self.start_button.clicked.connect(self.start_take_a_break)
        self.stop_button.clicked.connect(self.stop_take_a_break)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Enter Break time :</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">After Every Break Time your Favourite Video will Play on Youtube!!</span></p></body></html>"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionMade_with_love_India.setText(_translate("MainWindow", "Made with love India"))
        self.action_author_Swapnil_Mali.setText(_translate("MainWindow", "@author: Swapnil Mali"))
        self.actionLicence.setText(_translate("MainWindow", "Licence"))

    def start_take_a_break(self):
        try:
            my_break_time = int(self.input_break_time.text())
            if my_break_time < 1:
                print("This can't be a optimal break time, It might disturb you!!" )
                self.input_break_time.setText("")
            else:
                # QtWidgets.QMessageBox.about(self, "Title", "Message")
                self.input_break_time.setText("")
                while self.flg:
                    self.stop_button.clicked.connect(self.stop_take_a_break)
                    time.sleep(my_break_time)
                    print("Break Time son")

        except ValueError:
            print('Please try again..')

    def stop_take_a_break(self):
        self.flg = 0
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    label = QtWidgets.QLabel('Hello World!!')
    label.show()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

