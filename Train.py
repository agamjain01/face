from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # Label
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new romen",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # top image
        
        img_Top = Image.open(r"College Image\\traindata.jpeg")
        img_Top = img_Top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)
        
        F_lbl = Label(self.root, image=self.photoimg_Top)
        F_lbl.place(x=0, y=45, width=1530, height=325) 
        
        
        #button 
        
        b1_1=Button(self.root,text="TRAIN DATA ",cursor="hand2",command=self.Train_classifier,font=("times new romen",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=370,width=1530,height=80)
        
        
        
        # Bottom image
        
        img_bottom = Image.open(r"College Image\\train2.jpeg")
        img_bottom = img_bottom.resize((1530, 350), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        F_lbl = Label(self.root, image=self.photoimg_bottom)
        F_lbl.place(x=0, y=440, width=1530, height=350) 
        
        


    def Train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L')  
            imageNp = np.array(img, 'uint8')  
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13  
        
        ids = np.array(ids)
        
        # Train the classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows() 
        messagebox.showinfo("Result", "Training datasets completed!!!!")

        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
