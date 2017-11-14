import win32api
from collections import deque
import numpy as np
dLen = 100
minLen = 5
loc_x = deque(maxlen = dLen)
loc_y = deque(maxlen=dLen)
prevX, prevY = win32api.GetCursorPos()
while True:
    x,y = win32api.GetCursorPos()
    if (x == prevX and y==prevY):
        continue
    loc_x.append(x)
    loc_y.append(y)
    if len(loc_x) < minLen:
        continue
    prevX = x
    prevY = y
    dx = np.diff(loc_x)
    dy = np.diff(loc_y)
    avgDiffX = np.average(dx)
    avgDiffY = np.average(dy)
    lastDiffX = dx[-1]
    lastDiffY = dy[-1]
    if (avgDiffX*lastDiffX < 0) or (avgDiffY*lastDiffY < 0):
        print("Beat!")
        loc_x.clear()
        loc_y.clear()
        print("Location is {},{}. Average diff in x is {}, average diff in y is {}".format(x,y,avgDiffX, avgDiffY))
        print("Last diff in x is {}, in y is {}".format(dx[-1], dy[-1]))
        print("---")