#!/usr/bin/env python3  
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

xRoom1 = 5
yRoom1 = 1
xRoom2 = -6.3
yRoom2 = -0.98
xbath = 1.01
ybath = 3.02
xOutside = 1.11
yOutside = -.98


#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal):

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("You have reached the destination")
           return True

   else:
           rospy.loginfo("The robot failed to reach the destination")
           return False

if __name__ == '__main__':

    rospy.init_node('map_navigation', anonymous=False)

    
    while True:

        rospy.loginfo("\n|---------------------------|\nPRESS A KEY:\n0 : Room 1\n1 : Room 2\n2 : Bath\n3 : Outside\nq : Quite\n|---------------------------|\n")
        choice = input() 
        if choice == "0":
            x_goal = xRoom1
            y_goal = yRoom1
            move_to_goal(x_goal, y_goal)

        elif choice == "1":
            x_goal = xRoom2
            y_goal = yRoom2
            move_to_goal(x_goal, y_goal)

        elif choice == "2":
            x_goal = xbath
            y_goal = ybath
            move_to_goal(x_goal, y_goal)
        
        elif choice == "3":
            x_goal = xOutside
            y_goal = yOutside
            move_to_goal(x_goal, y_goal)
        elif choice =="q":
            exit()
        else:
            print("")
            print("AM I JOKING?")
            pass
    rospy.spin()
