from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        self.canvas = QPixmap(800, 592)
        self.canvas.colorCount()
        self.label.setPixmap(self.canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        self.label.setPixmap(self.canvas)
        for _ in range(randint(1, 15)):
            x, y = randint(50, 750), randint(50, 542)
            w, h = [randint(10, 50) for i in range(2)]
            painter = QPainter(self.label.pixmap())
            pen = QPen()
            pen.setWidth(5)
            pen.setColor(QColor(*[255, 255, 0]))
            painter.setPen(pen)
            painter.drawEllipse(x, y, w, h)
            painter.end()
            self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
