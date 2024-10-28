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

class Segment:
    def __init__(self, segment_ID, time, speed, angle, exercise_ID,direction):
        self.segment_ID = segment_ID
        self.time = time
        self.speed = speed
        self.angle = angle
        self.exercise_ID = exercise_ID
        self.direction = direction

class exercise:
    def __init__(self, exercise_ID, exercise_name, description, time):
        self.exercise_ID = exercise_ID
        self.exercise_name = exercise_name
        self.description = description
        self.time = time




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

def get_exercise_progrems(myc, exercise_ID):

    myc.execute( f"SELECT * FROM exercise_sement WHERE exercise_ID = {exercise_ID} ORDER BY segment_time")    
    myresult = myc.fetchall()
    Segment_list = []
    for row in myresult:
        s = Segment(row[0], row[1], row[2], row[3], row[4], row[5])
        Segment_list.append(s)
        #print("ID", segment.segment_ID,"time", segment.time,"speed", segment.speed,"angle", segment.angle,"exercise_ID",  segment.exercise_ID,"direction",  segment.direction)
    myc.execute( f"SELECT * FROM exercise_progrems WHERE exercise_ID = {exercise_ID}")
    myresult = myc.fetchall()

    exercise_progrem = exercise(myresult[0][0], myresult[0][1], myresult[0][2], myresult[0][3])
    print("ID", exercise_progrem.exercise_ID,"name", exercise_progrem.exercise_name,"description", exercise_progrem.description,"time",  exercise_progrem.time)

    return Segment_list, exercise_progrem


if __name__ == '__main__':
    
    
    zed, camera_data=z_camera.stert_camera_recorded()
    
    key_wait = 10
    start_time = time.time()
    timer = round((time.time() - start_time),6)
    db, myc=connect_myc()

    Segment_list, exercise_progrem = get_exercise_progrems(myc, 1)
    x=0
    motors = motor.connect()
    motor.move_platform(motors, 'h', 0, 200)

    ##################################### the mian loop  ###################################
    while timer<exercise_progrem.time and key_wait==10 :
        
        if x<len(Segment_list) and timer>Segment_list[x].time:
            motor.move_platform(motors, Segment_list[x].direction, Segment_list[x].angle, Segment_list[x].speed)
            x=x+1
            motor.move_platform(motors, 'h', 0, 200)
        
        timer = round((time.time() - start_time),6)
        print (timer)
        key_wait = z_camera.camera_work(zed, camera_data)
        keypoint = z_camera.take_co(camera_data.bodies)
        if len(keypoint)!=0:
         angel = z_camera.angel_analsis(keypoint)







    # shutdown all
        
    for mot in motors:
        mot.shutdown()
    db.close()
    zed.close()
    cv2.destroyAllWindows()
    print("finish")

