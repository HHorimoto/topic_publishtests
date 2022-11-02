cmake_minimum_required(VERSION 3.0.2)
project(topic_publishtests)

find_package(catkin REQUIRED COMPONENTS
  rostest
  rospy
)

catkin_package()

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  add_rostest(test/topic_publishtests.test)
endif()
