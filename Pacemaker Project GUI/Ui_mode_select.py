# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\New folder\mode_select.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mode(object):
    def setupUi(self, mode):
        mode.setObjectName("mode")
        mode.resize(614, 413)
        mode.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(mode)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(mode)
        self.pushButton.setGeometry(QtCore.QRect(450, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(mode)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 201, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout.addWidget(self.radioButton_12)

        self.retranslateUi(mode)
        QtCore.QMetaObject.connectSlotsByName(mode)

    def retranslateUi(self, mode):
        _translate = QtCore.QCoreApplication.translate
        mode.setWindowTitle(_translate("mode", "Mode Select"))
        self.label.setText(_translate("mode", "Select your mode for your pacemaker"))
        self.pushButton.setText(_translate("mode", "Confirm"))
        self.radioButton.setText(_translate("mode", "AOO"))
        self.radioButton_3.setText(_translate("mode", "VOO"))
        self.radioButton_4.setText(_translate("mode", "AAI"))
        self.radioButton_2.setText(_translate("mode", "VVI"))
        self.radioButton_5.setText(_translate("mode", "DOO"))
        self.radioButton_6.setText(_translate("mode", "DDD"))
        self.radioButton_7.setText(_translate("mode", "AOOR"))
        self.radioButton_8.setText(_translate("mode", "AAIR"))
        self.radioButton_9.setText(_translate("mode", "VOOR"))
        self.radioButton_10.setText(_translate("mode", "VVIR"))
        self.radioButton_11.setText(_translate("mode", "DOOR"))
        self.radioButton_12.setText(_translate("mode", "DDDR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mode = QtWidgets.QDialog()
    ui = Ui_mode()
    ui.setupUi(mode)
    mode.show()
    sys.exit(app.exec_())
