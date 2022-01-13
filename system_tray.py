import os
import sys
from PySide2 import QtWidgets, QtGui


def open_calc():
    os.system('calc')


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, parent, on_single_click=None):
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon("icons/icon_act.jpg"), parent)
        if on_single_click is not None:
            self.on_single_click = on_single_click
        self.setToolTip(f'VFX Pipeline Application Build - 3.2.56')
        menu = QtWidgets.QMenu(parent)

        open_cal = menu.addAction("Open Calculator")
        open_cal.triggered.connect(open_calc)
        open_cal.setIcon(QtGui.QIcon("icons/icon1.png"))

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icons/icon1.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.on_tray_icon_activated)

    def on_tray_icon_activated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            pass
        if reason == self.Trigger and hasattr(self, "on_single_click"):
            self.on_single_click()

    def set_on_single_click(self, on_single_click):
        self.on_single_click = on_single_click

    def set_activation_icon(self):
        self.setIcon(QtGui.QIcon("icons/icon_act.jpg"))

    def set_deactivation_icon(self):
        self.setIcon(QtGui.QIcon("icons/icon2_d.jpg"))
