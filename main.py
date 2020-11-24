from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 800, 592)
        self.setFixedSize(800, 592)
        self.canvas = QPixmap(800, 592)
        self.label = QLabel(self)
        self.label.resize(800, 552)
        self.label.move(0, 40)
        self.pushButton = QPushButton('создать круг', self)
        self.pushButton.move(363, 10)
        self.pushButton.resize(73, 21)
        self.canvas.colorCount()
        self.label.setPixmap(self.canvas)
        layout = QGridLayout(self.centralWidget())
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)
        self.initUI()


class Draw(MainWindow):
    def initUI(self):
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        self.label.setPixmap(self.canvas)
        for _ in range(randint(1, 15)):
            x, y = randint(50, 750), randint(50, 542)
            w, h = [randint(10, 50) for i in range(2)]
            painter = QPainter(self.label.pixmap())
            pen = QPen()
            pen.setWidth(5)
            pen.setColor(QColor(*[randint(0, 250), randint(0, 250), randint(0, 250)]))
            painter.setPen(pen)
            painter.drawEllipse(x, y, w, h)
            painter.end()
            self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Draw()
    w.show()
    sys.exit(app.exec_())
