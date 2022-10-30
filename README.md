# dtm_final
## darknet_ros
    roslaunch darknet_ros darknet_ros.launch
    
* using different camera topic
*  in darknet_ros/darknet_ros/launch/darknet_ros.launch line6
      
      <arg name="image" default=" [camera topic name] " />
* using different cfg,weight file
*   in darknet_ros/darknet_ros/launch/darknet_ros.launch line14
       
       <arg name="network_param_fiel"   default="$(find darknet_ros)/config/ [yaml file name]" />
    *in darknet_ros/darknet_ros/config/yaml file name.yaml
            
            
