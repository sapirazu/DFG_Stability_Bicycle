# import csv
# import cv2
# import sys
# import pyzed.sl as sl
# import cv_viewer.tracking_viewer as cv_viewer
# import numpy as np
# import math as m
import time
# import socket
# from ctypes import *
# import random
# import mysql.connector
# from mysql.connector import RefreshOption
# import ogl_viewer.viewer as gl

from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging

# Enable loglevel info
Logging()
# Create a list of all Modbus targets
coms = [ComModbus(ip_address='192.168.0.11'),
        ComModbus(ip_address='192.168.0.3')]
mots = [MotionHandler(com) for com in coms]

for mot in mots:
    mot.acknowledge_faults()
    mot.enable_powerstage()
    if not mot.referenced():
        mot.referencing_task()

for mot in mots:
    mot.position_task(150000, 30,absolute=True, nonblocking=True) # 1cm=1000
time.sleep(0.1)

while True:
    target_positions_reached = [mot.target_position_reached() for mot in mots]
    Logging.logger.info(f"Target positions reached: {target_positions_reached}")
    if all(target_positions_reached):
        break
    time.sleep(0.1)

for mot in mots:
    mot.shutdown()        