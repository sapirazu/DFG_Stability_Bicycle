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

def main():
    #fvbsfklvsl
    x=0

def camera_work():
    key_wait = 10

    if zed.grab() == sl.ERROR_CODE.SUCCESS:
          # Retrieve left image
        zed.retrieve_image(image, sl.VIEW.LEFT, sl.MEM.CPU, display_resolution)
        # Retrieve bodies            
        zed.retrieve_bodies(bodies, body_runtime_param)
            # Update GL view
        viewer.update_view(image, bodies)
            # Update OCV view
        image_left_ocv = image.get_data()
        cv_viewer.render_2D(image_left_ocv, image_scale, bodies.body_list, body_param.enable_tracking,body_param.body_format)
                                
        cv2.imshow("ZED | 2D View", image_left_ocv)
        key = cv2.waitKey(key_wait)
        if key == 113:  # for 'q' key
                print("Exiting...")
            
        if key == 109:  # for 'm' key
            if (key_wait > 0):
                    print("Pause")
                    key_wait = 0
            else:
                print("Restart")
                key_wait = 10
 
def take_co():
    keypoint = []
    obj_array=bodies.body_list
    for i in range(len(obj_array)):
        obj_data = obj_array[i]
        position = obj_data.head_position
        bounding_box = obj_data.bounding_box
        keypoint = obj_data.keypoint
    return keypoint

def angel_analsis(keypoint):
     shoulder=0
     torso_RL=0
     torso_BF=0
     neck = keypoint[3]
     pelvis = keypoint[0]
     L_shoulder = keypoint[5]
     R_shoulder = keypoint[12]





if __name__ == '__main__':
    # Create a Camera object
    zed = sl.Camera()
    # Path of .svo2 file captured by ZED for testing
    input_path = "C:/Users/owner/Documents/ZED/HD2K_SN37511070_14-32-49.svo2"
    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.set_from_svo_file(input_path)

    # init_params.camera_resolution = sl.RESOLUTION.HD1080  # Use HD1080 video mode
    # init_params.coordinate_units = sl.UNIT.METER  # Set coordinate units
    # init_params.depth_mode = sl.DEPTH_MODE.ULTRA
    # init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Enable Positional tracking (mandatory for object detection)
    positional_tracking_parameters = sl.PositionalTrackingParameters()
    # If the camera is static, uncomment the following line to have better performances
    # positional_tracking_parameters.set_as_static = True
    zed.enable_positional_tracking(positional_tracking_parameters)

    body_param = sl.BodyTrackingParameters()
    body_param.enable_tracking = True  # Track people across images flow
    body_param.enable_body_fitting = False  # Smooth skeleton move
    body_param.detection_model = sl.BODY_TRACKING_MODEL.HUMAN_BODY_FAST
    body_param.body_format = sl.BODY_FORMAT.BODY_34  # Choose the BODY_FORMAT you wish to use

    # Enable Object Detection module
    zed.enable_body_tracking(body_param)

    body_runtime_param = sl.BodyTrackingRuntimeParameters()
    body_runtime_param.detection_confidence_threshold = 40

    # Get ZED camera information
    camera_info = zed.get_camera_information()
    # 2D viewer utilities
    display_resolution = sl.Resolution(min(camera_info.camera_configuration.resolution.width, 1280),
                                       min(camera_info.camera_configuration.resolution.height, 720))
    image_scale = [display_resolution.width / camera_info.camera_configuration.resolution.width
        , display_resolution.height / camera_info.camera_configuration.resolution.height]

    # Create OpenGL viewer
    viewer = gl.GLViewer()
    viewer.init(camera_info.camera_configuration.calibration_parameters.left_cam, body_param.enable_tracking,
                body_param.body_format)
    # Create ZED objects filled in the main loop
    bodies = sl.Bodies()
    image = sl.Mat()
    bodiedata = sl.BodyData
    key_wait = 10


    ##################################### the mian loop  ###################################
    while viewer.is_available():
        camera_work()
        keypoint = take_co()
        if len(keypoint)!=0:
         angel_analsis(keypoint)

