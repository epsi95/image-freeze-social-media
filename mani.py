import numpy as np
import cv2 as cv

cap = cv.VideoCapture(2)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
output = None
isinitialized = False
height = None
height_to_capture = 4 # 10 pixels
till_captured = 0 # 10 pixels

while True:
    ret, frame = cap.read()
    
    if (not ret) and (frame == None):
        break
    
    if(not isinitialized):
        output = np.zeros(frame.shape, dtype = frame.dtype)
        height = frame.shape[1]
        isinitialized = True

    
    if(not height_to_capture > height):
        output[till_captured : till_captured + height_to_capture] = frame[till_captured : till_captured + height_to_capture]
        till_captured += height_to_capture
    else:
        till_captured = height
        
    output_to_show = np.vstack((output[:till_captured], frame[till_captured:]))
    cv.imshow('frame', output_to_show)
    
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
