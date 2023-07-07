import yaml
from epics import PV
import time
import globals

class PV_epics:

       def __init__(self, gui):
              self.epics_variables = dict()
              self.gui = gui

       def Write_PV(self, name,data):
              self.epics_variables[name].value = data
              time.sleep(0.1)
              return self.epics_variables[name].value

       def Read_PV(self, name):
              #print(epics_variables)
              return (str(self.epics_variables[str(name)].value))

       def load_conf(self):
              globals.init()
              with open('config.yml') as cfg:
                     main_config = yaml.load(cfg);
                     keys = list(main_config['EPICS_PV'].keys())
                     values = main_config['EPICS_PV'].values()
                     pv_list = list()
                     for n in values:
                            pv_list.append(PV(str(n)))
                     self.epics_variables.update(dict(zip(keys,pv_list)))

              self.epics_variables['STATUS_X'].add_callback(self.status_x_callback)
              self.epics_variables['STATUS_Y'].add_callback(self.status_y_callback)
              self.epics_variables['GET_BEAM_X'].add_callback(self.get_pos_x_callback)
              self.epics_variables['GET_BEAM_Y'].add_callback(self.get_pos_y_callback)

              globals.VERT_INBEAM_DEFOULT_VALUE = main_config['VERT_INBEAM_DEFOULT_VALUE']
              globals.HOR_INBEAM_DEFOULT_VALUE = main_config['HOR_INBEAM_DEFOULT_VALUE']
              globals.VERT_DELTA_DEFOULT_VALUE = main_config['VERT_DELTA_DEFOULT_VALUE']
              globals.HOR_DELTA_DEFOULT_VALUE = main_config['HOR_DELTA_DEFOULT_VALUE']
              globals.VERT_HOME_DEFOULT_VALUE = main_config['VERT_HOME_DEFOULT_VALUE']
              globals.HOR_HOME_DEFOULT_VALUE = main_config['HOR_HOME_DEFOULT_VALUE']
              return main_config

       def status_x_callback(self, pvname, value, timestamp, cb_info, **kwargs):
              self.gui.status_text_update("state change: timestamp -> {0},  name -> {1},  value -> {2}".format(timestamp,pvname,value))
       def status_y_callback(self, pvname, value, timestamp, cb_info, **kwargs):
              self.gui.status_text_update("state change: timestamp -> {0},  name -> {1},  value -> {2}".format(timestamp,pvname,value))
       def get_pos_x_callback(self, pvname, value, timestamp, cb_info, **kwargs):
              self.gui.status_text_update("state change: timestamp -> {0},  name -> {1},  value -> {2}".format(timestamp,pvname,value))
       def get_pos_y_callback(self, pvname, value, timestamp, cb_info, **kwargs):
              self.gui.status_text_update("state change: timestamp -> {0},  name -> {1},  value -> {2}".format(timestamp,pvname,value))


       