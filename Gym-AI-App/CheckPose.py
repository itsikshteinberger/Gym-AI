import pandas as pd
import cv2
from matplotlib.pyplot import get
from numpy.lib.function_base import angle
from DetectorModel import Detector
from config import PoseNames
from Utils import *
import numpy as np
import config

#importing the csv file
df = pd.read_csv('Gym-AI/Gym-AI-App/pose_degrees.csv', index_col=0)

#Angles Array
AnglesArray = ['13_11_23',
            '14_12_24',
            '12_24_26',
            '11_23_25',
            '23_25_27',
            '24_26_28',
            '26_28_30',
            '25_27_29',
            '11_13_15',
            '12_14_16']


#CheckPose is a function, that recieves an exercise name, an array of current degrees that the person is at, and a
# pose position(1 or 2) and checks pose_degrees.csv if that exercise exists.
# If the name exists, it will return an array, where each cell represents a degree between points, and 
# will contain a boolean value on whether the degree is in the correct range.
# Check Config.py for the names of the points that are in the array (AnglesArray)
# The Array is also here

def CheckPose(exercise_name, current_angles_array, position):

    #first we check if the exercise exists
    #PLEASE DO THIS I DONT KNOW HOW

    correct_angles = [] #array of boolean values for correct angles

    #here we basically check if the angle we recieved is between the correct values in the csv, and if it is we assign it true correct_angles, otherwise false
    for iteration, angle_to_check in enumerate(AnglesArray):
        correct_angles.append(current_angles_array[iteration] > getFirstAngle(df['P'+position+'_'+angle_to_check][exercise_name]) and current_angles_array[iteration] <getSecondAngle(df['P'+position+'_'+angle_to_check][exercise_name]))

    return correct_angles






    
