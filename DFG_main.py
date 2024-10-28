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
from mysql.connector.constants import RefreshOption
import ogl_viewer.viewer as gl
from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging
import motor
import z_camera


def connect_myc():
    db = mysql.connector.connect(
     host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
    )
    refresh = RefreshOption.LOG
    db.cmd_refresh(refresh)
    myc = db.cursor()
    return db, myc

if __name__ == '__main__':
    motors = motor.connect()
    
    zed, camera_data=z_camera.stert_camera_recorded()
    
    key_wait = 10
    start_time = time.time()
    timer = round((time.time() - start_time),6)
    db=connect_myc()


    ##################################### the mian loop  ###################################
    while timer<120 and key_wait==10 :
        timer = round((time.time() - start_time),6)
        key_wait = z_camera.camera_work(zed, camera_data)
        keypoint = z_camera.take_co(camera_data.bodies)
        if len(keypoint)!=0:
         angel = z_camera.angel_analsis(keypoint)
        


