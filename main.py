import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        self.ui = Ui_Dialog()
        super().__init__()
        self.ui.setupUi(self)
        # self.ui.students.itemSelectionChanged.connect(self.students_fail)
        self.ui.augustButton.clicked.connect(self.august)
        self.show()


    def august(self):
        items = self.ui.students.selectedItems()
        for item in items:
            self.ui.failedStudents.addItem(item.text())
            self.ui.students.takeItem(self.ui.students.row(item))
"""
    def students_fail(self):
        items = self.ui.students.selectedItems()
        self.ui.students.removeItemWidget(items[0])
        for item in items:
            self.ui.failedStudents.addItem(item.text())
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())