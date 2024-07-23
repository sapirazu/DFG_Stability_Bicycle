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
def main():
    zed = sl.Camera()

    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720  # Use HD720 video mode
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
    init_params.coordinate_units = sl.UNIT.METER
    init_params.sdk_verbose = 1

    status = zed.open(init_params)
    if status != sl.ERROR_CODE.SUCCESS:
        print("Camera Open : " + repr(status) + ". Exit program.")
        exit()

    # Enable Positional tracking (mandatory for object detection)
    positional_tracking_parameters = sl.PositionalTrackingParameters()
    # If the camera is static, uncomment the following line to have better performances and boxes sticked to the ground.
    positional_tracking_parameters.set_as_static = True
    zed.enable_positional_tracking(positional_tracking_parameters)

    # Define the Objects detection module parameters
    body_params = sl.BodyTrackingParameters()
    # Different model can be chosen, optimizing the runtime or the accuracy
    body_params.detection_model = sl.BODY_TRACKING_MODEL.HUMAN_BODY_FAST
    body_params.enable_tracking = True
    body_params.enable_segmentation = False
    # Optimize the person joints position, requires more computations
    body_params.enable_body_fitting = True
    # Object tracking requires the positional tracking module

    body_params.body_format = sl.BODY_FORMAT.BODY_34  # Choose the BODY_FORMAT you wish to use
    # Enable Object Detection module
    zed.enable_body_tracking(body_params)
    body_runtime_param = sl.BodyTrackingRuntimeParameters()
    body_runtime_param.detection_confidence_threshold = 40
    # Get ZED camera information
    camera_info = zed.get_camera_information()
    # 2D viewer utilities
    display_resolution = sl.Resolution
    image_scale = [1000,500]
    # Create ZED objects filled in the main loop
    bodies = sl.Bodies()
    image = sl.Mat()
    keypoint = []



    while np.any(keypoint) != True:
            # Grab an image
            if zed.grab() == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                zed.retrieve_image(image, sl.VIEW.LEFT, sl.MEM.CPU, display_resolution)
                # Retrieve objects
                err = zed.retrieve_bodies(bodies, body_runtime_param)
                obj_array = bodies.body_list  # from hi
                image_data = image.get_data()  # from hi
                # Update OCV view
                image_left_ocv = image.get_data()
                cv_viewer.render_2D(image_left_ocv, image_scale, bodies.body_list, body_params.enable_tracking,
                                    body_params.body_format)
                cv2.imshow("ZED | 2D View", image_left_ocv)
                cv2.waitKey(1)

                for i in range(len(obj_array)):
                    obj_data = obj_array[i]
                    position = obj_data.head_position
                    bounding_box = obj_data.bounding_box




if __name__ == "__main__":
   while 1 == True:
    main()