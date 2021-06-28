import numpy as np 
import cv2 
import time 

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0 
for i in range(60):
    ret,background = cap.read()
background = np.flip(background,axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_blue = np.array([94,80,70])
    u_blue = np.array([135,255,255])
    
   
    mask1 = cv2.inRange(hsv,l_blue,u_blue)

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask2  = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img,img,mask=mask2)
    res2 = cv2.bitwise_and(background,background,mask = mask1)

    final = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("Invisible Cloak",final)

    if cv2.waitKey(5) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()