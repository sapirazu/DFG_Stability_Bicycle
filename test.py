# import csv
# import cv2
# import sys
# import pyzed.sl as sl
# import cv_viewer.tracking_viewer as cv_viewer
import numpy as np
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

def move_platform(mots, dirction, angel,speed):
    step=angel*14000
    match dirction:
        case 'f':
            # move forward
            position_0=150000+step
            position_1=150000+step
            pass
        case 'b':
            # move backward
            position_0=150000-step
            position_1=150000-step
            pass
        case 'l':
            # move left
            position_0=150000-step
            position_1=150000+step
            pass
        case 'r':
            # move right
            position_0=150000+step
            position_1=150000-step
            pass
        case 'h':
            # move home
            position_0=150000
            position_1=150000
            pass

    mots[0].position_task(position_0, speed, absolute=True, nonblocking=True)
    mots[1].position_task(position_1, speed, absolute=True, nonblocking=True)
    while True:
        target_positions_reached = [mot.target_position_reached() for mot in mots]
        Logging.logger.info(f"Target positions reached: {target_positions_reached}")
        if all(target_positions_reached):
            break


if __name__ == "__main__":

    # Enable loglevel info
    #Logging()
    # Create a list of all Modbus targets
    coms = [ComModbus(ip_address='192.168.0.1'),   # Right motor
            ComModbus(ip_address='192.168.0.3')]    # Left motor
    
    for com in coms:
       if not com.connected():
        exit()

    mots = [MotionHandler(com) for com in coms]

    for mot in mots:
        mot.acknowledge_faults()
        mot.enable_powerstage()
        if not mot.referenced():
            mot.referencing_task()

    move_platform(mots, 'h', 0, 60)
    move_platform(mots, 'f', 3, 60)
    move_platform(mots, 'b', 5, 60)
    move_platform(mots, 'l', 3, 60)
    move_platform(mots, 'r', 5, 60)
    move_platform(mots, 'h', 0, 60)

    for mot in mots:
        mot.shutdown()