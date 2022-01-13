import sys
import threading

from PySide2 import QtWidgets, QtGui
from tendo import singleton

from my_keyboard_listener import MyKeyboardListener
from system_tray import SystemTrayIcon

if __name__ == '__main__':

    # Make sure only a single instance of a program is running per machine
    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException as error:
        sys.exit(-1)

    # Launch
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(window)
    tray_icon.set_on_single_click(lambda: keyboard_listener.switch_state())
    tray_icon.show()

    keyboard_listener = MyKeyboardListener(on_activation=lambda: tray_icon.set_activation_icon(),
                                           on_deactivation=lambda: tray_icon.set_deactivation_icon(),
                                           on_shutdown=lambda: app.exit())
    threading.Thread(target=lambda: keyboard_listener.start(), daemon=True).start()
    sys.exit(app.exec_())
