# Form implementation generated from reading ui file 'projectui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 776)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.95)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(250, 255, 250)")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DataFileButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.DataFileButton_1.setGeometry(QtCore.QRect(40, 440, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DataFileButton_1.setFont(font)
        self.DataFileButton_1.setStatusTip("")
        self.DataFileButton_1.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.DataFileButton_1.setAutoDefault(False)
        self.DataFileButton_1.setDefault(False)
        self.DataFileButton_1.setFlat(False)
        self.DataFileButton_1.setObjectName("DataFileButton_1")
        self.DataFileButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.DataFileButton_2.setGeometry(QtCore.QRect(260, 440, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DataFileButton_2.setFont(font)
        self.DataFileButton_2.setStatusTip("")
        self.DataFileButton_2.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.DataFileButton_2.setAutoDefault(False)
        self.DataFileButton_2.setDefault(False)
        self.DataFileButton_2.setFlat(False)
        self.DataFileButton_2.setObjectName("DataFileButton_2")
        self.objNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.objNameEdit.setEnabled(True)
        self.objNameEdit.setGeometry(QtCore.QRect(40, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.objNameEdit.setFont(font)
        self.objNameEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.objNameEdit.setText("")
        self.objNameEdit.setObjectName("objNameEdit")
        self.objNamelabel = QtWidgets.QLabel(self.centralwidget)
        self.objNamelabel.setGeometry(QtCore.QRect(40, 200, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.objNamelabel.setFont(font)
        self.objNamelabel.setObjectName("objNamelabel")
        self.signalPathlabel = QtWidgets.QLabel(self.centralwidget)
        self.signalPathlabel.setGeometry(QtCore.QRect(40, 500, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.signalPathlabel.setFont(font)
        self.signalPathlabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.signalPathlabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.signalPathlabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.signalPathlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signalPathlabel.setObjectName("signalPathlabel")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(530, 30, 781, 201))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 660, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.pushButton.setObjectName("pushButton")
        self.ClearPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearPushButton.setGeometry(QtCore.QRect(270, 660, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.ClearPushButton.setFont(font)
        self.ClearPushButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.ClearPushButton.setObjectName("ClearPushButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 30, 391, 151))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("CMHT-Logo.webp"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setEnabled(True)
        self.IDEdit.setGeometry(QtCore.QRect(170, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.IDEdit.setFont(font)
        self.IDEdit.setAutoFillBackground(False)
        self.IDEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.IDEdit.setText("")
        self.IDEdit.setObjectName("IDEdit")
        self.IDlabel = QtWidgets.QLabel(self.centralwidget)
        self.IDlabel.setGeometry(QtCore.QRect(170, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.IDlabel.setFont(font)
        self.IDlabel.setObjectName("IDlabel")
        self.TestButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestButton.setGeometry(QtCore.QRect(40, 550, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.TestButton.setObjectName("TestButton")
        self.IndicatorLabel = QtWidgets.QLabel(self.centralwidget)
        self.IndicatorLabel.setGeometry(QtCore.QRect(40, 620, 431, 21))
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(50, 200, 50);border: 1.5px solid gray;border-radius: 10px;}")
        self.IndicatorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.IndicatorLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.IndicatorLabel.setText("")
        self.IndicatorLabel.setObjectName("IndicatorLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(339, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit.setFont(font)
        self.dateEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.dateEdit.setStyleSheet("QDateEdit {border: 1px solid gray;border-radius: 8px;}")
        self.dateEdit.setFrame(True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(5, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.TimeSpec.OffsetFromUTC)
        self.dateEdit.setObjectName("dateEdit")
        self.FrequencyInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FrequencyInput.setGeometry(QtCore.QRect(40, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FrequencyInput.setFont(font)
        self.FrequencyInput.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.FrequencyInput.setObjectName("FrequencyInput")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(170, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinBox.setFont(font)
        self.spinBox.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.spinBox.setStyleSheet("QSpinBox {border: 1px solid gray;border-radius: 8px;}")
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox.setAccelerated(False)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.Fqlabel = QtWidgets.QLabel(self.centralwidget)
        self.Fqlabel.setGeometry(QtCore.QRect(40, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Fqlabel.setFont(font)
        self.Fqlabel.setObjectName("Fqlabel")
        self.RpeatsLabel = QtWidgets.QLabel(self.centralwidget)
        self.RpeatsLabel.setGeometry(QtCore.QRect(170, 290, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.RpeatsLabel.setFont(font)
        self.RpeatsLabel.setObjectName("RpeatsLabel")
        self.TempEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TempEdit.setEnabled(True)
        self.TempEdit.setGeometry(QtCore.QRect(340, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.TempEdit.setFont(font)
        self.TempEdit.setAutoFillBackground(False)
        self.TempEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.TempEdit.setObjectName("TempEdit")
        self.TestNumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TestNumEdit.setEnabled(True)
        self.TestNumEdit.setGeometry(QtCore.QRect(260, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.TestNumEdit.setFont(font)
        self.TestNumEdit.setAutoFillBackground(False)
        self.TestNumEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.TestNumEdit.setObjectName("TestNumEdit")
        self.TestNumlabel = QtWidgets.QLabel(self.centralwidget)
        self.TestNumlabel.setGeometry(QtCore.QRect(260, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.TestNumlabel.setFont(font)
        self.TestNumlabel.setObjectName("TestNumlabel")
        self.Temperature = QtWidgets.QLabel(self.centralwidget)
        self.Temperature.setGeometry(QtCore.QRect(340, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Temperature.setFont(font)
        self.Temperature.setObjectName("Temperature")
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(340, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(530, 260, 781, 211))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(530, 500, 781, 221))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.MeasuredVLabel = QtWidgets.QLabel(self.centralwidget)
        self.MeasuredVLabel.setGeometry(QtCore.QRect(830, 480, 241, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MeasuredVLabel.setFont(font)
        self.MeasuredVLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.MeasuredVLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MeasuredVLabel.setObjectName("MeasuredVLabel")
        self.MeasuredcurLabel = QtWidgets.QLabel(self.centralwidget)
        self.MeasuredcurLabel.setGeometry(QtCore.QRect(810, 240, 251, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MeasuredcurLabel.setFont(font)
        self.MeasuredcurLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.MeasuredcurLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MeasuredcurLabel.setObjectName("MeasuredcurLabel")
        self.OutSigLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutSigLabel.setGeometry(QtCore.QRect(840, 10, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OutSigLabel.setFont(font)
        self.OutSigLabel.setAutoFillBackground(False)
        self.OutSigLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.OutSigLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.OutSigLabel.setObjectName("OutSigLabel")
        self.ampInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ampInput.setGeometry(QtCore.QRect(260, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ampInput.setFont(font)
        self.ampInput.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.ampInput.setObjectName("ampInput")
        self.ampLabel = QtWidgets.QLabel(self.centralwidget)
        self.ampLabel.setGeometry(QtCore.QRect(260, 290, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ampLabel.setFont(font)
        self.ampLabel.setObjectName("ampLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1356, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gamry Signal"))
        self.DataFileButton_1.setText(_translate("MainWindow", "Select Signal Profile"))
        self.DataFileButton_2.setText(_translate("MainWindow", "Load Default Profile"))
        self.objNamelabel.setText(_translate("MainWindow", "Model:"))
        self.signalPathlabel.setText(_translate("MainWindow", "Signal Profile"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.ClearPushButton.setText(_translate("MainWindow", "Clear"))
        self.IDlabel.setText(_translate("MainWindow", "Cell ID:"))
        self.TestButton.setText(_translate("MainWindow", "Test"))
        self.FrequencyInput.setText(_translate("MainWindow", "80"))
        self.Fqlabel.setText(_translate("MainWindow", "Freq. [KHz]:"))
        self.RpeatsLabel.setText(_translate("MainWindow", "Cycles:"))
        self.TempEdit.setText(_translate("MainWindow", "23"))
        self.TestNumEdit.setText(_translate("MainWindow", "1"))
        self.TestNumlabel.setText(_translate("MainWindow", "Test #:"))
        self.Temperature.setText(_translate("MainWindow", "Temperature:"))
        self.DateLabel.setText(_translate("MainWindow", "M/d/yyyy:"))
        self.MeasuredVLabel.setText(_translate("MainWindow", "Measured Voltage [V] vs Time [s]"))
        self.MeasuredcurLabel.setText(_translate("MainWindow", "Measured Current [A] vs Time [s]"))
        self.OutSigLabel.setText(_translate("MainWindow", "Output Signal vs Time [s]"))
        self.ampInput.setText(_translate("MainWindow", "1"))
        self.ampLabel.setText(_translate("MainWindow", "Amp. :"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
