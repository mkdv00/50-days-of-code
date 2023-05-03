from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, \
    QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QLabel, QGridLayout, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(800, 600)

        # Add Menu Bar with two items
        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')

        # Create Add student Action
        add_student_action = QAction(QIcon('icons/add.png'), 'Add student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        # Create About Action
        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        # Create Search Action
        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        search_action.triggered.connect(self.search)

        # Create table with student data
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar and add status bar elements
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton('Delete Record')
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.status_bar.removeWidget(child)

        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)

    def load_data(self):
        with sqlite3.connect('database.db') as connection:
            result = connection.execute('SELECT * FROM students;')

            self.table.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()
    
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()


class EditDialog(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Get student name from selected row
        index = main_window.table.currentRow()
        student_name = main_window.table.item(index, 1).text()

        # Get id from selected row
        self.student_id = main_window.table.item(index, 0).text()

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        course_name = main_window.table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # Add mobile widget
        mobile_name = main_window.table.item(index, 3).text()
        self.mobile_name = QLineEdit(mobile_name)
        self.mobile_name.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile_name)

        # Add a submit button
        button = QPushButton('Update')
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?;',
                           (self.student_name.text(),
                            self.course_name.itemText(self.course_name.currentIndex()),
                            self.mobile_name.text(),
                            self.student_id))
            connection.commit()
        # Refresh the table
        main_window.load_data()
        self.close()


class DeleteDialog(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Delete student')

        layout = QGridLayout()
        confirmation = QLabel('Are you sure you want to delete?')
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        # Get selected row index and student id
        index = main_window.table.currentRow()
        student_id = main_window.table.item(index, 0).text()

        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE from students WHERE id = ?;', (student_id, ))
            connection.commit()

        main_window.load_data()
        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle('Success')
        confirmation_widget.setText('The record was deleted successfully!')
        confirmation_widget.exec()


class InsertDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile widget
        self.mobile_name = QLineEdit()
        self.mobile_name.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile_name)

        # Add a submit button
        button = QPushButton('Register')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_name.text()

        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO students (name, course, mobile) VALUES (?, ?, ?);',
                           (name, course, mobile))
            connection.commit()

        main_window.load_data()
        self.close()


class SearchDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Search Student')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add Search button
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)

        for item in items:
            main_window.table.item(item.row(), 1).setSelected(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
