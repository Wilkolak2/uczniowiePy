# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 406)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 571, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.students = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.students.setObjectName("students")
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        self.gridLayout.addWidget(self.students, 1, 1, 1, 1)
        self.failedStudents = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.failedStudents.setObjectName("failedStudents")
        self.gridLayout.addWidget(self.failedStudents, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.wyrokButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.wyrokButton.setStyleSheet("font-weight:bold;\n"
"color: #FF0000;\n"
"background-color:rgb(0, 0, 255);\n"
"")
        self.wyrokButton.setObjectName("wyrokButton")
        self.gridLayout.addWidget(self.wyrokButton, 3, 0, 1, 2)
        self.uczenValue = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.uczenValue.setObjectName("uczenValue")
        self.gridLayout.addWidget(self.uczenValue, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.students.isSortingEnabled()
        self.students.setSortingEnabled(False)
        item = self.students.item(0)
        item.setText(_translate("Dialog", "Patryk Janusz"))
        item = self.students.item(1)
        item.setText(_translate("Dialog", "Oskar Janusz"))
        item = self.students.item(2)
        item.setText(_translate("Dialog", "Fifi "))
        item = self.students.item(3)
        item.setText(_translate("Dialog", "Na pewno nie ja"))
        self.students.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "Uczniowie"))
        self.label_2.setText(_translate("Dialog", "Uczniowie ktorzy nie zdaja"))
        self.wyrokButton.setText(_translate("Dialog", "Zapisz Wyrok"))
        self.label_3.setText(_translate("Dialog", "Dodaj ucznia"))
        self.pushButton.setText(_translate("Dialog", "Dodaj"))
