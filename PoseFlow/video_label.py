import glob
import cv2


input_label = ''
vid_array = glob.glob("./*.avi")

for index, vid in enumerate(vid_array): 
    cap = cv2.VideoCapture(vid)
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)  