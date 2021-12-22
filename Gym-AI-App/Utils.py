import numpy as np
import numpy.linalg as LA


def points2vec(point1,point2,point3,shape): # This function converts the three points to two vectors base on the image size
    
    # Vector_i = EndPoint_i - StartPoint_i (When i = x,y,z)
    
    vec1 = np.array([ 
        int(shape[1] - shape[1]*point2.x) - int(shape[1]-shape[1]*point1.x),
        int(shape[0] - shape[0]*point2.y) - int(shape[0] -shape[0]*point1.y),
        -1*(point2.z - point1.z)
    ])

    vec2 = np.array([ 
        int(shape[1] - shape[1]*point3.x) - int(shape[1]-shape[1]*point2.x),
        int(shape[0] - shape[0]*point3.y) - int(shape[0] -shape[0]*point2.y),
        -1*(point3.z - point2.z)
    ])

    return vec1, vec2

def CalculateAngle(point1,point2,point3,shape): # This function calculates the angle between two vectors

        # First, convert the 3 points to 2 vectors
        vector_1, vector_2 = points2vec(point1,point2,point3,shape)
        
        # Make unit vectors
        unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
        unit_vector_2 = vector_2 / np.linalg.norm(vector_2)

        # Calculation of the angle according arcos of the internal product of the unit vectors
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        angle = np.arccos(dot_product)

        # Convert from radians to degrees and return
        return 180 - np.degrees(angle)

def getPoseNumber(excel_string):#function that was made to get the pose number from the string from the excel file
    return int(excel_string[1])

def getFirstPoint(excel_string):#function that gets the first point from the string from the excel file
    return int(excel_string[3:5])

def getSecondPoint(excel_string):#function that gets the second point from the string from the excel file
    return int(excel_string[6:8])

def getThirdPoint(excel_string):#function that gets the third point from the string from the excel file
    return int(excel_string[9:11])

def getFirstAngle(excel_string):#function that gets the first angle from the string from the excel file
    toReturn = ""
    #add all chars till we hit the '<'
    for char in excel_string:
        if char != '<':
            toReturn = toReturn + char
        if char == '<':
            break
    
    return int(toReturn)

def getSecondAngle(excel_string):#function that gets the second angle from the string from the excel file
    toReturn = ""
    #run till we get the first second <, then save the number
    signCounter = 0
    for char in excel_string:
        
        if signCounter == 2:
            toReturn = toReturn + char
        
        if char == '<':
            signCounter +=1

    return int(toReturn)






