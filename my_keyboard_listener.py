import os

from pynput.keyboard import Listener, Key, Controller
from win10toast import ToastNotifier


class MyKeyboardListener:

    def __init__(self, on_activation=None, on_deactivation=None, on_shutdown=None):
        """
        :type on_shutdown: callable object
        :type on_deactivation: callable object
        :type on_activation: callable object
        """
        self._is_activated = True
        self.on_activation = on_activation
        self.on_deactivation = on_deactivation
        self.on_shutdown = on_shutdown
        self._toaster = ToastNotifier()

    def start(self):
        self._toaster.show_toast("Notification", "Programme is started", duration=2)
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _on_press(self, key):
        if key == Key.pause:
            self._is_activated = not self._is_activated
            if self._is_activated and self.on_activation is not None:
                self.on_activation()
            elif not self._is_activated and self.on_deactivation is not None:
                self.on_deactivation()

        elif key == Key.scroll_lock:  # this call will terminate the callback function and close the script
            self._toaster.show_toast("Notification", "Programme is closed", duration=2)
            if self.on_shutdown is not None:
                self.on_shutdown()

        elif str(key) == "<96>" and self._is_activated:
            self._exit_procedure()

    def switch_state(self):
        self._on_press(Key.pause)

    @staticmethod
    def _exit_procedure():
        """
        perform Alt + F4 keystrokes
        And
        disconnect the current wifi (windows only)
        """
        keyboard_controller = Controller()
        keyboard_controller.press(Key.alt_l)
        keyboard_controller.press(Key.f4)
        keyboard_controller.release(Key.f4)
        keyboard_controller.release(Key.alt_l)

        os.system("netsh wlan disconnect")


if __name__ == '__main__':
    MyKeyboardListener().start()
