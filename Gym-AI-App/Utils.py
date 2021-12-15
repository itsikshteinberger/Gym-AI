import numpy as np
import numpy.linalg as LA

def points2vec(point1,point2,point3,shape): # This function convert the three points to two vectors base on the image size
    
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

def CalculateAngle(point1,point2,point3,shape): # This function calculate the angle between two vectors

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