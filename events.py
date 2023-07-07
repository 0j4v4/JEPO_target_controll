import test
from main_gui import Ui_MainWindow
import main_gui


def status_x_callback(pvname, value, timestamp, cb_info, **kwargs):
       main_gui.status_text_update(self,"status x changed -> {0}".format(value))
def status_y_callback(pvname, value, timestamp, cb_info, **kwargs):
       main_gui.status_text_update(self,"status y changed -> {0}".format(value))
def get_pos_x_callback(pvname, value, timestamp, cb_info, **kwargs):
       main_gui.status_text_update(self,"pos x changed -> {0}".format(value))
def get_pos_y_callback(pvname, value, timestamp, cb_info, **kwargs):
       main_gui.status_text_update(self,"pos y changed -> {0}".format(value))

