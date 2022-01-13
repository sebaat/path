import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication(sys.argv)
main = QtWidgets.QLabel()
main.setGeometry(100, 100, 300, 300)
main.setPixmap(QtGui.QPixmap("icons/icon1.png"))
main.setWindowFlag(Qt.SplashScreen)

main.show()

sys.exit(app.exec_())
