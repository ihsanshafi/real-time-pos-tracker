#modules
import cv2 as cv
import mediapipe as mp
import time

#variables
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
path = "C:\\Users\\ihsan\Pictures\Camera Roll\WIN_20221125_21_17_38_Pro.mp4"
url = 'https://192.168.1.5:8080/video'
cams = [0,1,2,url,path]
cap =  cv.VideoCapture(cams[0])
pTime = 0

while True:
    success,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS) #to draw the lines
    
    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img,str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN, 2,(0,255,0),3) #for writing the number of frames per second

    cv.imshow("image",img)
    key = cv.waitKey(1)
    
    #exit command
    if key == ord('q') :
        cap.release()
        cv.destroyAllWindows()
        exit(1)