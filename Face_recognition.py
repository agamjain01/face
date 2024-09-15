from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # Label
        
        title_lbl=Label(self.root,text="Face Recognition",font=("times new romen",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
          # image
        
        img_Top = Image.open(r"College Image\\Face_detector.jpeg")
        img_Top = img_Top.resize((650, 700), Image.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)
        
        F_lbl = Label(self.root, image=self.photoimg_Top)
        F_lbl.place(x=0, y=50, width=650, height=700) 
        
        
        img_Second = Image.open(r"College Image\\Fcae_sec.jpeg")
        img_Second = img_Second.resize((950, 700), Image.LANCZOS)
        self.photoimg_Second = ImageTk.PhotoImage(img_Second)
        
        F_lbl = Label(self.root, image=self.photoimg_Second)
        F_lbl.place(x=655, y=50, width=950, height=700) 
        
        
        #button 
        
        b1_1=Button(self.root, text=" FACE RECOGNITION ",command=self.face_recgo,cursor="hand2",font=("times new romen",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=700,width=200,height=40)
        
        # ============================ attendance ========================
        
    def mark_attendance(self,i,r,n,d):
      with open("Attendance.csv","r+",newline="\n") as f:
        mydataList=f.readlines()
        name_list=[]
        for line in mydataList:
          entry=line.split((","))
          name_list.append(entry[0])
        if ((i not in name_list)  and (r not in name_list) and (n not in name_list) and (d not in name_list)):
          now=datetime.now()
          d1=now.strftime("%d/%m/%Y")
          dtstring=now.strftime("%H:%M:%S")
          f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},preset")
          
            
    
    
    # =========================================== Face Recgonition========================
    
    def face_recgo(self):
      def drew_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
        
        coord=[]
        
        for (x,y,w,h) in features:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
          id,predict=clf.predict(gray_image[y:y+h,x:x+w])
          confidence=int((100*(1-predict/300)))
          
          # print(f"id : {id}")
          
          
          conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recogintion")
          my_cursor = conn.cursor()
          
          my_cursor.execute("select Name  from student_data where Student_id = %s",(id,))
          n=my_cursor.fetchone()
          n="+".join(n)  if n else "unknown"
          
          my_cursor.execute("select Roll  from student_data where Student_id = %s",(id,))
          r=my_cursor.fetchone()
          r="+".join(r) if r else "unknown"
          
          my_cursor.execute("select Dep  from student_data where Student_id = %s",(id,))
          d=my_cursor.fetchone()
          d="+".join(d) if d else "unknown"
          
          my_cursor.execute("select Student_id  from student_data where Student_id = %s",(id,))
          i=my_cursor.fetchone()
          i="+".join(i) if i else "unknown"
          
          if confidence>80:
            cv2.putText(img,f"Student_id.{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.putText(img,f"Roll.{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.putText(img,f"Name.{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.putText(img,f"Department.{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            self.mark_attendance(i,r,n,d)
          else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            
          coord=[x,y,w,h]
        
        return coord
      
      
      def recognize(img,clf,faceCascade):
        coord=drew_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        return img
      faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      clf=cv2.face.LBPHFaceRecognizer_create()
      clf.read("classifier.xml")
      
      video_cap=cv2.VideoCapture(0)
      
      while True:
        ret,img=video_cap.read()
        img = cv2.flip(img, 1)
        img = recognize(img,clf,faceCascade)
        cv2.imshow("Welcome to face Recognition",img)
        
        if cv2.waitKey(1)==13:
          break
      video_cap.release()
      cv2.destroyAllWindows()
         
        
        
    
            
            
          
        
        
        
  
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
