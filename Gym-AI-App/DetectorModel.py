#Import all we need

import PIL
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class Detector:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils #For visualisation
        self.mp_pose = mp.solutions.pose #Pose estimation model

        self.pose = self.mp_pose.Pose( min_detection_confidence = 0.5, min_tracking_confidence = 0.5)

        self.cap = cv2.VideoCapture(0) #Connect to webCam

    def Detection(self, image, visualize =  False):
        
        image.flags.writeable = False
        
        results = self.pose.process(image)
        
        image.flags.writeable = True

        self.mp_drawing.draw_landmarks( 
            image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS, 
            self.mp_drawing.DrawingSpec(color = (254,117,66), thickness=2, circle_radius = 2),
            self.mp_drawing.DrawingSpec(color = (254,66,230), thickness=2, circle_radius = 2)
        )

        if (visualize):
            plt.imshow(image, interpolation='nearest')
            plt.show()

        return results, image
        

