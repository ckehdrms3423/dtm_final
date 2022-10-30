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
            
            
