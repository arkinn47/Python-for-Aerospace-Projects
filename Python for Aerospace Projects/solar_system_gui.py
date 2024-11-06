from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox, QApplication, QMainWindow, QButtonGroup, QRadioButton
import solar_system_visualization as ssv
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()  # Parent constructor
        self.setGeometry(200, 200, 500, 500)
        self.cb2 = QCheckBox("2D Visualization", self)
        self.cb1 = QCheckBox("3D Visualization", self)
        self.setWindowTitle("Solar System Visualization")
        self.initUI()

    def initUI(self):
        '''Function produces everything that goes into the GUI.'''
        #Create label.
        self.label = QtWidgets.QLabel(self)
        self.label.setText(
            "Select a checkbox to create either a 2d or 3d visualization of the solar system.")
        self.label.resize(500, 30)
        self.label.move(25, 250)

        #Create checkboxes.
        self.cb1.setGeometry(270, 150, 300, 50)
        self.cb2.setGeometry(130, 150, 300, 50)
        self.setStyleSheet("QCheckBox")

        #Create button to visualize.
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Visualize")
        self.b1.move(200, 200)
        self.b1.clicked.connect(self.clicked)

        self.setStyleSheet("QCheckBox{"
                           "font-size: 15px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}"
                           )

    def clicked(self):
        '''Creat visualizations when clicked.'''
        dimension = None
        if self.cb1.isChecked() and self.cb2.isChecked() == False:
            dimension = '3d'
        elif self.cb2.isChecked() and self.cb1.isChecked() == False:
            dimension = '2d'
        elif self.cb2.isChecked() and self.cb1.isChecked() == True:
            dimension = 'both'
        ssv.create_visualization(dimension)


def window():
    # Config setup for application
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
