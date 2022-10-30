# dtm_final
## darknet_ros
    roslaunch darknet_ros darknet_ros.launch
    
* using different camera topic
    *  in darknet_ros/darknet_ros/launch/darknet_ros.launch line 6
      
      <arg name="image" default=" [camera_topic_name] " />
* using different cfg,weight file
    *  in darknet_ros/darknet_ros/launch/darknet_ros.launch line 14

      <arg name="network_param_fiel"   default="$(find darknet_ros)/config/ [yaml_file_name]" />
       
    *  in darknet_ros/darknet_ros/config/yaml_file_name.yaml
        
        yolo_model:
        
            config_file:
                name: config_file_name.cfg
            weight_file:
                name: weight_file_name.weights
            threshold:
                value: 0.3
            detection_classes:
                names:
                    -1
                    -2
                    -3
                    
    *  Download weight file at darknet_ros/darknet_ros/yolo_network_config/weight 
    *  Download cfg file at darknet_ros/darknet_ros/yolo_network_config/cfg
## ublox_f9p
    sudo chmod 777 /dev/ttyACM0
    roslaunch ublox_gps ublox_device.launch
* change launch file
    * in ublox_f9p/ublox_gps/launch/ublox_device.launch
  
      <arg_name="node_name" value="ublox_gps"/>
      
      <arg_name="param_file_name" value="zed-f9p"/>
      
* change device
    * in ublox_f9p/ublox_gps/config/zed-f9p.yaml line 5
      
      device: /dev/port_name (default /dev/ttyACM0)
      
## usb_cam
    roslaunch usb_cam usb_cam-test.launch
    
* change launch file
    * in usb_cam/launch/usb_cam-test.launch line 3
    
      <param name="video_device" value="/dev/port_name (defaule /dev/video0) />
    * in usb_cam/nodes/usb_cam_node.cpp line 92
    
## sub
    rosrun sub lis.py
    
