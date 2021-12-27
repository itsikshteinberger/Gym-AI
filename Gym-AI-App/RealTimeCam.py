import cv2
from matplotlib.pyplot import get
from numpy.lib.function_base import angle
from DetectorModel import Detector
from config import PoseNames
from Utils import *
import numpy as np
from CheckPose import *
from AddPose import *

def LandMarks(results): #This function returns a dictonary with all poses info (x,y,z,visibility)

    landmarks = results.pose_landmarks.landmark
    landmarksDict = {}
    
    for i in range(0,33):
        landmarksDict[PoseNames[i]] = landmarks[i]

    return landmarksDict


cap = cv2.VideoCapture(0) #Connect to webCam
model = Detector()

FirstPositionDegrees = []
SecondPositionDegrees = []
CurrentDegrees = []

#Video feed
while cap.isOpened():

    ret, frame = cap.read() #Get current feed from my webCam

    #Detect stuff and render
    image = frame

    results, image = model.Detection(image)

    
    
    
    
    try:

         
        #save current degrees in this array
        CurrentDegrees = [CalculateAngle(LandMarks(results)['LEFT_ELBOW'],LandMarks(results)['LEFT_SHOULDER'],LandMarks(results)['LEFT_HIP'],image.shape),
                    CalculateAngle(LandMarks(results)['RIGHT_ELBOW'],LandMarks(results)['RIGHT_SHOULDER'],LandMarks(results)['RIGHT_HIP'],image.shape),
                    CalculateAngle(LandMarks(results)['RIGHT_SHOULDER'],LandMarks(results)['RIGHT_HIP'],LandMarks(results)['RIGHT_KNEE'],image.shape),
                    CalculateAngle(LandMarks(results)['LEFT_SHOULDER'],LandMarks(results)['LEFT_HIP'],LandMarks(results)['LEFT_KNEE'],image.shape),
                    CalculateAngle(LandMarks(results)['LEFT_HIP'],LandMarks(results)['LEFT_KNEE'],LandMarks(results)['LEFT_ANKLE'],image.shape),
                    CalculateAngle(LandMarks(results)['RIGHT_HIP'],LandMarks(results)['RIGHT_KNEE'],LandMarks(results)['RIGHT_ANKLE'],image.shape),
                    CalculateAngle(LandMarks(results)['RIGHT_KNEE'],LandMarks(results)['RIGHT_ANKLE'],LandMarks(results)['RIGHT_HEEL'],image.shape),
                    CalculateAngle(LandMarks(results)['LEFT_KNEE'],LandMarks(results)['LEFT_ANKLE'],LandMarks(results)['LEFT_HEEL'],image.shape),
                    CalculateAngle(LandMarks(results)['LEFT_SHOULDER'],LandMarks(results)['LEFT_ELBOW'],LandMarks(results)['LEFT_WRIST'],image.shape),
                    CalculateAngle(LandMarks(results)['RIGHT_SHOULDER'],LandMarks(results)['RIGHT_ELBOW'],LandMarks(results)['RIGHT_WRIST'],image.shape)]
        
        
        
        #here you can put the pose you want to check, and the position of that pose
        truthArrayP1 = CheckPose('Dan', CurrentDegrees, '1')
        truthArrayP2 = CheckPose('Dan', CurrentDegrees, '2')
        image[0:30,0:30,:] = [0,200,0] if truthArrayP1[0] else [0,0,200]
        image[40:70,0:30,:] = [0,200,0] if truthArrayP1[1] else [0,0,200]
        image[80:110,0:30,:] = [0,200,0] if truthArrayP1[2] else [0,0,200]
        image[120:150,0:30,:] = [0,200,0] if truthArrayP1[3] else [0,0,200]
        image[160:190,0:30,:] = [0,200,0] if truthArrayP1[4] else [0,0,200]
        image[200:230,0:30,:] = [0,200,0] if truthArrayP1[5] else [0,0,200]
        image[240:270,0:30,:] = [0,200,0] if truthArrayP1[6] else [0,0,200]
        image[280:310,0:30,:] = [0,200,0] if truthArrayP1[7] else [0,0,200]
        image[320:350,0:30,:] = [0,200,0] if truthArrayP1[8] else [0,0,200]
        image[360:390,0:30,:] = [0,200,0] if truthArrayP1[9] else [0,0,200]
        image[0:30,40:70,:] = [0,200,0] if truthArrayP2[0] else [0,0,200]
        image[40:70,40:70,:] = [0,200,0] if truthArrayP2[1] else [0,0,200]
        image[80:110,40:70,:] = [0,200,0] if truthArrayP2[2] else [0,0,200]
        image[120:150,40:70,:] = [0,200,0] if truthArrayP2[3] else [0,0,200]
        image[160:190,40:70,:] = [0,200,0] if truthArrayP2[4] else [0,0,200]
        image[200:230,40:70,:] = [0,200,0] if truthArrayP2[5] else [0,0,200]
        image[240:270,40:70,:] = [0,200,0] if truthArrayP2[6] else [0,0,200]
        image[280:310,40:70,:] = [0,200,0] if truthArrayP2[7] else [0,0,200]
        image[320:350,40:70,:] = [0,200,0] if truthArrayP2[8] else [0,0,200]
        image[360:390,40:70,:] = [0,200,0] if truthArrayP2[9] else [0,0,200]
        # End of checking
        
    except:
        pass

    cv2.imshow("Mediapipe Feed", image) #Visualize actual frame

    #if 's' is pressed, save the two positions recorded as a new row in the csv, under the name in addPose
    if cv2.waitKey(10) & 0xFF == ord('s'): 
            addPose('Dan', FirstPositionDegrees, SecondPositionDegrees)
            break
    
    #if 'Q' is pressed just exit
    if cv2.waitKey(10) & 0xFF == ord('q'): 
            break
    
    #if '1' is pressed, record the current pose as position 1
    if cv2.waitKey(10) & 0xFF == ord('1'): 
            FirstPositionDegrees = CurrentDegrees
            print("got 1")
            
    #if '' is pressed, record the current pose as position 2
    if cv2.waitKey(10) & 0xFF == ord('2'): 
            SecondPositionDegrees = CurrentDegrees
            print("got 2")
            
    


#Close all
cap.release()
cv2.destroyAllWindows()
