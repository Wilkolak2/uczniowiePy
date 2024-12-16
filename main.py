import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        self.ui = Ui_Dialog()
        super().__init__()
        self.ui.setupUi(self)
        self.ui.students.itemClicked.connect(self.students_fail)
        self.ui.failedStudents.itemClicked.connect(self.good_students)
        self.ui.wyrokButton.clicked.connect(self.student_save)
        self.ui.wyrokButton.clicked.connect(self.student_save2)
        self.show()

    def students_fail(self):
        items = self.ui.students.selectedItems()
        self.ui.students.takeItem(self.ui.students.currentRow())
        for item in items:
            self.ui.failedStudents.addItem(item.text())


    def good_students(self):
        items = self.ui.failedStudents.selectedItems()
        self.ui.failedStudents.takeItem(self.ui.failedStudents.currentRow())
        for item in items:
            self.ui.students.addItem(item.text())


    def student_save(self):
        with open('sierpien.txt','w') as file:
            for i in range(self.ui.failedStudents.count()):
                file.write(self.ui.failedStudents.item(i).text())
                file.write('\n')

    def student_save2(self):
        with open('zdajacy.txt','w') as file:
            for i in range(self.ui.students.count()):
                file.write(self.ui.students.item(i).text())
                file.write('\n')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())