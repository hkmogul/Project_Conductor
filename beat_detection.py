# lib for detecting beats/estimating tempo and amplitude based on x-y location of an object
# generalized for use with OpenCV and other object tracking means
# Hilary Mogul - hmogul@ur.rochester.edu
import numpy as np
from collections import deque
from scipy import stats 

def detect_beat(data, step = 5):
    ''' Detects if a beat/change in inflection was done on a point. Should work with 
        Returns 
        @param Step: Number of last points to consider as 
    '''
    init_data = data[0:len(data)-step]
    final_data = data[-step:]
    init_data_x = []
    init_data_y = []
    final_data_x = []
    final_data_y = []
    # separate the x and y for each one
    for i in range(0,len(data)-step):
        init_data_x.append(data[i][0])
        init_data_y.append(data[i][1])

    for j in range(len(data)-step, len(data)):
        final_data_x.append(data[j][0])
        final_data_y.append(data[j][1])

    # perform a linear regression on the initial and final data
    init_slope, _, _, _, _ = stats.linregress(init_data_x, init_data_y)
    final_slope, _, _, _, _ = stats.linregress(final_data_x, final_data_y)
    # check if the signs are different
    if init_slope * final_slope < 0:
        return True
    else:
        return False

def estimate_tempo(data):
    ''' generate a linearly weighted average of data '''
    # generate the weights based on the length of the data
    weights = len(data)*[1]
    for i in range(0,len(weights)):
        weights[i] = 1./(len(weights)-i)

    return np.average(data,weights)