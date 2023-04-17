import logging
import os
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import requests


# var = datetime.now()
# var1 = var.date()
# s = var1.strftime("%d-%m-%Y")
#
# log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
# logFile = 'LOG/ELOG/elog' + str(s)
# my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=100 * 1024 * 1024, backupCount=10, encoding=None, delay=0)
# my_handler.setFormatter(log_formatter)
# my_handler.setLevel(logging.INFO)
# err_log = logging.getLogger('root')
# err_log.setLevel(logging.INFO)
# err_log.addHandler(my_handler)
#
# ############################IO LOG###################################################
#
# IOlog_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
# IOlogFile = 'LOG/AppLOG/applog' + str(s)
# IOmy_handler = RotatingFileHandler(IOlogFile, mode='a', maxBytes=100 * 1024 * 1024, backupCount=10, encoding=None,delay=0)
# IOmy_handler.setFormatter(IOlog_formatter)
# IOmy_handler.setLevel(logging.INFO)
# app_log = logging.getLogger('root')
# app_log.setLevel(logging.INFO)
# app_log.addHandler(IOmy_handler)


##################################LOG Exterminator######################################
# ls = []
# path = r"Logger###path####"
# now = time.time()
#
#
# for filename in os.listdir(path):
#     if os.path.getmtime(os.path.join(path, filename)) < now - 60:
#         if os.path.isfile(os.path.join(path, filename)):
#             print(filename)
#             print(type(filename))
#             os.remove(os.path.join(path, filename))

# "facility": "0"=> 0-APPLOG,1-ErrorLog,2-Debug
# 	"_level":0        => 0 i/p 2=>o/p,3=err
# 	"_ip" :""
# 	"short_message": "methodName4",
# 	"_logroot":""
#     "_message":"logTxt",
# 	"host": "inzozilotto",
#     "_trace":"",
#     "_data":""

import logging
import graypy
app_log = logging.getLogger('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
app_log.setLevel(logging.DEBUG)
handler = graypy.GELFHTTPHandler('192.168.10.155', 12201)
app_log.addHandler(handler)

class graylog_io:
    def info(logroot,data,method,client_ip):
        json_body={
         "short_message": method,
         "host": "Wesco_mylottohub_api",
         "_ip":client_ip,
         "facility": "0",           #0 - app  1 - error
         "_logroot":logroot,   # DB-in DB-out REQ RES
         "_message":"logTxt",
         "_data":data
       }
        requests.post("http://192.168.10.155:12209/gelf",json=json_body)

class graylog_error():
    def exception(trace_back, error, method,data,client_ip):
        json_body = {
            "short_message": method,
            "host": "Wesco_mylottohub_api",
            "facility": "1",
            "_ip": client_ip,
            "_message": error,
            "_trace": trace_back,
            "_data": data
        }
        requests.post("http://192.168.10.155:12209/gelf", json=json_body)

# err_log = graylog_error
# app_log = graylog_io