from PyQt5 import QtWidgets
from JEPO_TARGET_CONTROL import Ui_MainWindow
from PyQt5 import QtGui
import sys
import time
import epics_processing
import globals

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.on_off_BTN.setCheckable(True)
        self.ui.GROUP_HORISONTAL.setEnabled(False)
        self.ui.GROUP_VERTICAL.setEnabled(False)
        self.ui.on_off_BTN.clicked.connect(self.on_off_button_clicked)
        self.ui.auto_manual_checkbox.stateChanged.connect(self.mode_select_check_changed)

        self.ui.VERTICAL_IN_BEAM_BUTTON.clicked.connect(self.VERTICAL_IN_BEAM_BUTTON_clicked)
        self.ui.VERTICAL_DELTA_BUTTON.clicked.connect(self.VERTICAL_DELTA_BUTTON_clicked)
        self.ui.VERTICAL_HOME_BUTTON.clicked.connect(self.VERTICAL_HOME_BUTTON_clicked)
        self.ui.HORISONTAL_IN_BEAM_BUTTON.clicked.connect(self.HORISONTAL_IN_BEAM__BUTTON_clicked)
        self.ui.HORISONTAL_DELTA_BUTTON.clicked.connect(self.HORISONTAL_DELTA_BUTTON_clicked)
        self.ui.HORISONTAL_HOME_BUTTON.clicked.connect(self.HORISONTAL_HOME_BUTTON_clicked)

        self.epics = epics_processing.PV_epics(gui = self);
        self.on_load()
    
    def VERTICAL_IN_BEAM_BUTTON_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.VERTICAL_IN_BEAM_TEXT_IN.text()
            #self.status_text_update("setting IN_BEAM_Y value to -> " + str(
            self.epics.Write_PV('IN_BEAM_Y',value)#))

    def VERTICAL_DELTA_BUTTON_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.VERTICAL_DELTA_TEXT_IN.text()
            #self.status_text_update("setting DELTA_Y value to -> " + str(
            self.epics.Write_PV('DELTA_Y',value)#))

    def VERTICAL_HOME_BUTTON_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.VERTICAL_HOME_TEXT_IN.text()
            #self.status_text_update("setting HOME_Y value to -> " + str(
            self.epics.Write_PV('HOME_Y',value)#))

    def HORISONTAL_IN_BEAM_BUTTON_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.HORISONTAL_IN_BEAM_TEXT_IN.text()
            #self.status_text_update("setting IN_BEAM_X value to -> " + str(
            self.epics.Write_PV('IN_BEAM_X',value)#))

    def HORISONTAL_DELTA_BUTTON_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.HORISONTAL_DELTA_TEXT_IN.text()
            #self.status_text_update("setting DELTA_X value to -> " + str(
            self.epics.Write_PV('DELTA_X',value)#))

    def HORISONTAL_HOME_clicked(self):
        if globals.on_state == "ON":
            value = self.ui.HORISONTAL_HOME_TEXT_IN.text()
            #self.status_text_update('setting HOME_X value to -> ' + str(
            self.epics.Write_PV('HOME_X',value)#))

    def mode_select_check_changed(self):
        if self.ui.auto_manual_checkbox.isChecked():
            globals.mode = "MANUAL"
            self.ui.GROUP_HORISONTAL.setEnabled(True)
            self.ui.GROUP_VERTICAL.setEnabled(True)
            self.status_text_update("monde change: mode set to -> " + globals.mode)
            self.epics.Write_PV('MODE', "MANUAL")
        else:
            globals.mode = "AUTO"
            self.epics.Write_PV('MODE', "AUTO")
            self.ui.GROUP_HORISONTAL.setEnabled(False)
            self.ui.GROUP_VERTICAL.setEnabled(False)
            self.status_text_update("monde change: mode set to -> " + globals.mode)
            
    def on_off_button_clicked(self):
        if self.ui.on_off_BTN.isChecked():
            globals.on_state = "ON"
            if self.ui.comboBox.currentText() == "File":
                self.load_from_file()
            else:
                self.load_from_epics()
            self.status_text_update("state change: program state set to -> " + str(globals.on_state))
            self.epics.Write_PV('GUI', globals.on_state)
            self.ui.on_off_BTN.setText("ON")
            self.ui.on_off_BTN.setStyleSheet("background-color: green")
        else:
            globals.on_state = "OFF"
            self.status_text_update("state change: program state set to -> " + str(globals.on_state))
            self.epics.Write_PV('GUI', globals.on_state)
            self.ui.on_off_BTN.setText("OFF")
            self.ui.on_off_BTN.setStyleSheet("background-color: None")
    
    def on_load(self):
        self.status_text_update("software loaded successfully")
        self.epics.load_conf()
        
    def load_from_file(self):
        self.status_text_update("data loaded from config file")
        self.ui.VERTICAL_IN_BEAM_TEXT_IN.setText(str(globals.VERT_INBEAM_DEFOULT_VALUE))
        self.ui.HORISONTAL_IN_BEAM_TEXT_IN.setText(str(globals.HOR_INBEAM_DEFOULT_VALUE))
        self.ui.HORISONTAL_DELTA_TEXT_IN.setText(str(globals.HOR_DELTA_DEFOULT_VALUE))
        self.ui.HORISONTAL_HOME_TEXT_IN.setText(str(globals.HOR_HOME_DEFOULT_VALUE))
        self.ui.VERTICAL_DELTA_TEXT_IN.setText(str(globals.VERT_DELTA_DEFOULT_VALUE))
        self.ui.VERTICAL_HOME_TEXT_IN.setText(str(globals.VERT_HOME_DEFOULT_VALUE))
        
    def load_from_epics(self):
        self.status_text_update("data loaded from epics values")
        self.ui.VERTICAL_IN_BEAM_TEXT_IN.setText(self.epics.Read_PV('IN_BEAM_Y'))
        self.ui.HORISONTAL_IN_BEAM_TEXT_IN.setText(self.epics.Read_PV('IN_BEAM_X'))
        self.ui.HORISONTAL_DELTA_TEXT_IN.setText(self.epics.Read_PV('DELTA_X'))
        self.ui.HORISONTAL_HOME_TEXT_IN.setText(self.epics.Read_PV('HOME_X'))
        self.ui.VERTICAL_DELTA_TEXT_IN.setText(self.epics.Read_PV('DELTA_Y'))
        self.ui.VERTICAL_HOME_TEXT_IN.setText(self.epics.Read_PV('HOME_Y'))

    def status_text_update(self, text = ""):
        self.ui.textBrowser.append(str(text))
        self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
    
    def closeEvent(self, event):
        globals.on_state = "OFF"
        self.epics.Write_PV('GUI', globals.on_state)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())



