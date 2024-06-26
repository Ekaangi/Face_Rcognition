import cv2
import numpy as np

cap=cv2.VideoCapture(0)

skip=0
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
face_data=[]
file_name=input("Enter the name of the person whose is being taken : ")

while True:
    boolean,frame=cap.read()

    if boolean==False:
        continue
     
    faces=face_cascade.detectMultiScale(frame,1.3,5)
    
    if len(faces)==0:
        continue
    
    faces=sorted(faces,key=lambda f:f[2]*f[3],reverse=True)
      
    for (x,y,w,h) in faces:
    
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        
        offset=10
        face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
        
        face_section=cv2.resize(face_section,(100,100))
        
        skip+=1
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data))

    cv2.imshow("Photo",frame)
    cv2.imshow("Region of Interest",face_section)
    
    #press 'q' , the above process will stop
    
    keypressed=cv2.waitKey(1) & 0xFF
    if keypressed==ord('q'):
        break
   
face_data=np.asarray(face_data) 

face_data=face_data.reshape((face_data.shape[0],-1))

np.save(file_name+'.npy',face_data)
cap.release()
cv2.destroyAllWindows()   
