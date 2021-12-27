import pandas as pd
from csv import writer
from Utils import *

#add pose is a function that recieves 2 lists of degrees, for both positions, and an exercise name,and adds it to the .csv
def addPose(exercise, DegreeArray1, DegreeArray2):
    #here we connect the exercise name and degrees into one array so we can add to the row
    fullRow = [exercise] + convertArrayToCsvRow(DegreeArray1) + convertArrayToCsvRow(DegreeArray2)

    f = open('Gym-AI/Gym-AI-App/pose_degrees.csv','a')
    f.write("\n")
    f.close()
    
    with open('Gym-AI/Gym-AI-App/pose_degrees.csv', 'a', newline='') as f_object:

        
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        
        print(fullRow)
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(fullRow)
    
        #Close the file object
        f_object.close()



