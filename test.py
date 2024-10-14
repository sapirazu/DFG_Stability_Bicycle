import csv
import cv2
import sys
import pyzed.sl as sl
import cv_viewer.tracking_viewer as cv_viewer
import numpy as np
import math as m
import time
import socket
from ctypes import *
import random
import mysql.connector
from mysql.connector import RefreshOption
import ogl_viewer.viewer as gl

from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging

# Enable loglevel info
Logging()

com = ComModbus('192.168.0.13')
with MotionHandler(com) as mot:
    mot.acknowledge_faults()
    mot.enable_powerstage()
    mot.referencing_task()

    mot.position_task(1, 1000)
    mot.position_task(-5, 2000)
    mot.position_task(10, 1500, absolute=True)