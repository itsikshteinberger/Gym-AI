import cv2
from DetectorModel import Detector

cap = cv2.VideoCapture(0) #Connect to webCam
model = Detector()

#Video feed
while cap.isOpened():

    ret, frame = cap.read() #Get current feed from my webCam

    #Detect stuff and render
    image = frame

    results, image = model.Detection(image)

    cv2.imshow("Mediapipe Feed", image) #Visualize actual frame

    if cv2.waitKey(10) & 0xFF == ord('q'): #If click q -> exit
            break

#Close all
cap.release()
cv2.destroyAllWindows()