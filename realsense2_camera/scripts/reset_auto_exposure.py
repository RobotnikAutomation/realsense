#!/bin/bash
rosrun dynamic_reconfigure dynparam set /camera1/realsense2_camera_manager rs435_depth_enable_auto_exposure 0
rosrun dynamic_reconfigure dynparam set /camera1/realsense2_camera_manager rs435_depth_enable_auto_exposure 1

rosrun dynamic_reconfigure dynparam set /camera2/realsense2_camera_manager rs435_depth_enable_auto_exposure 0
rosrun dynamic_reconfigure dynparam set /camera2/realsense2_camera_manager rs435_depth_enable_auto_exposure 1
