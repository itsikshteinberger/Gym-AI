import cv2
from matplotlib.pyplot import get
from numpy.lib.function_base import angle
from DetectorModel import Detector
from config import PoseNames
from Utils import *
import numpy as np

def LandMarks(results): #This function returns a dictonary with all poses info (x,y,z,visibility)

    landmarks = results.pose_landmarks.landmark
    landmarksDict = {}
    
    for i in range(0,33):
        landmarksDict[PoseNames[i]] = landmarks[i]

    return landmarksDict


cap = cv2.VideoCapture(0) #Connect to webCam
model = Detector()

#Video feed
while cap.isOpened():

    ret, frame = cap.read() #Get current feed from my webCam

    #Detect stuff and render
    image = frame

    results, image = model.Detection(image)

    
    try:

        #Just checking..    
        image[0:30,0:30,:] = CalculateAngle(LandMarks(results)['LEFT_SHOULDER'],LandMarks(results)['LEFT_ELBOW'],LandMarks(results)['LEFT_WRIST'],image.shape)
        print(CalculateAngle(LandMarks(results)['LEFT_SHOULDER'],LandMarks(results)['LEFT_ELBOW'],LandMarks(results)['LEFT_WRIST'],image.shape))
    
    except:
        pass

    cv2.imshow("Mediapipe Feed", image) #Visualize actual frame

    if cv2.waitKey(10) & 0xFF == ord('q'): #If click q -> exit
            break

#Close all
cap.release()
cv2.destroyAllWindows()
