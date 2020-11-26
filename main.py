import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from table_coffee_ui import Ui_MainWindow
import sqlite3

cur = sqlite3.connect("coffee.db")
con = cur.cursor()


class Paint_El(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table()

    def table(self):
        data = con.execute("SELECT * FROM coffee")
        for i, row in enumerate(data):
            self.table_coffee.setRowCount(
                self.table_coffee.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table_coffee.setItem(
                    i, j, QTableWidgetItem(str(elem))
                )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Paint_El()
    ex.show()
    sys.exit(app.exec())