import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel, QMainWindow, QApplication


class WaterMark(QMainWindow):
    def __init__(self, application):
        QMainWindow.__init__(self)
        self._app = application
        self.icon_w = 40
        self.icon_h = 40
        self.x_marge = _centi_to_pixel(1, self._screen()["dpi_x"])
        self.y_marge = _centi_to_pixel(1, self._screen()["dpi_y"])
        self._label = QLabel(self)
        self._init()

    def _init(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(self._screen()["width"] - self.icon_w - self.x_marge, self.y_marge,
                         self.icon_w + 2, self.icon_h + 2)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.SplashScreen)

        self._label.setStyleSheet("background: rgba(0, 120, 185, 0.01)")
        self._label.setPixmap(QPixmap("icons/circle.png").scaled(self.icon_w, self.icon_h))

    def mousePressEvent(self, event):
        print("press")

    def mouseDoubleClickEvent(self, event):
        pass

    def enterEvent(self, event):
        self._label.setStyleSheet("background: rgba(0, 120, 185, 0.1)")

    def leaveEvent(self, event):
        self._label.setStyleSheet("background: rgba(0, 120, 185, 0.01)")

    def _screen(self):
        screen = {"width": self._app.primaryScreen().size().width(),
                  "dpi_x": self._app.primaryScreen().physicalDotsPerInchX(),
                  "dpi_y": self._app.primaryScreen().physicalDotsPerInchY()}
        return screen


def _centi_to_pixel(centi, dpi):
    pixels = (dpi * centi) / 2.54
    return round(pixels)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    water_mark = WaterMark(app)
    water_mark.show()
    sys.exit(app.exec_())
