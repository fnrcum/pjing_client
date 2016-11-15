from PIL import Image, ImageTk
import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class OptionsGUI(QWidget):
    def __init__(self, im, parent=None):
        super(OptionsGUI, self).__init__(parent)

        self.im = im
        layout = QVBoxLayout()

        self.l1 = QLabel()
        self.l1.setPixmap(QPixmap("out.png"))
        layout.addWidget(self.l1)
        self.setLayout(layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)

        self.b2 = QPushButton("&Upload")
        self.b2.setDefault(True)
        self.b2.clicked.connect(self.upload)
        hbox.addWidget(self.b2)

        self.b4 = QPushButton("&Save")
        self.b4.setDefault(True)
        self.b4.clicked.connect(self.save)
        hbox.addWidget(self.b4)

        self.b1 = QPushButton("&Quit")
        self.b1.setDefault(True)
        self.b1.clicked.connect(self.quit)
        hbox.addWidget(self.b1)

        self.setLayout(hbox)

        self.setWindowTitle("pJing")
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def upload(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Unsupported Action")
        msg.setInformativeText("File uploads are not supported yet!")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()
        print "value of pressed message box button:", retval

    def save(self):
        path = QFileDialog.getSaveFileName(self, 'Dialog Title', selectedFilter='*.png')
        if path:
            self.im.save(str(path))
        if os.path.isfile('out.png'):
            os.remove('out.png')

    def quit(self):
        if os.path.isfile('out.png'):
            os.remove('out.png')
        quit()



