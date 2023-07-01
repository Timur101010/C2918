import sys
from time import strftime, gmtime
import threading
from time import sleep
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSi


def pyqtSignal(str, arguments):
    pass


class Backend(QObject):
    updated = pyqtSignal(str, arguments=['updater'])


def __init__(self):
    QObject.__init__(self)


def bootUp(self):
    t_thread = threading.Thread(target=self._bootUp)
    t_thread.daemon = True
    t_thread.start()


def _bootUp(self):
    while True:
        curr_time = strftime("%H:%M:%S", gmtime())
        print(curr_time)
        self.updater(curr_time)
        sleep(1)


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

backend = Backend()
engine.rootContext().setContextProperty("backend", backend)

engine.load('./UI/main.qml')

backend.bootUp()

sys.exit(app.exec())
