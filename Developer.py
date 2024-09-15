from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new romen",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # Full
        img_Full = Image.open(r"College Image\\Developer_Image.jpeg")
        img_Full = img_Full.resize((1530, 950), Image.LANCZOS)
        self.photoimg_Full = ImageTk.PhotoImage(img_Full)
        
        bg_image = Label(self.root, image=self.photoimg_Full)
        bg_image.place(x=0, y=46, width=1530, height=950)
        
        
        # =================================frame==========================
        
        main_Frame=Frame(bg_image,bd=2,bg="white")
        main_Frame.place(x=1000,y=0,width=500,height=600)
        
        
        img_ = Image.open(r"College Image\\Agam.jpg")
        img_ = img_.resize((195,200), Image.LANCZOS)
        self.photoimg_ = ImageTk.PhotoImage(img_)
        
        bg_ = Label(main_Frame, image=self.photoimg_)
        bg_.place(x=300, y=0, width=195, height=200)
        
        
        dep_label=Label(main_Frame,text=" Hello , my name is Agam ",font=("times new romen",15,"bold"),bg="white")
        dep_label.place(x=0,y=5)
        
        course_label=Label(main_Frame,text="I am Student of B.tech(CSE) ",font=("times new romen",15,"bold"),bg="white")
        course_label.place(x=0,y=40)
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
