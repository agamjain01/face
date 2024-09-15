from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import Student_Detail
from  Train import Train
from Face_recognition import Face_Recognition
from Developer import Developer
from  Attendance import Attendance_st
from Help import help
from tkinter import messagebox

import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # First Image
        img = Image.open(r"College Image\\images.jpeg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        F_lbl = Label(self.root, image=self.photoimg)
        F_lbl.place(x=0, y=0, width=500, height=130)  
        
        # Second  Image
        img1 = Image.open(r"College Image\download.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        F_lbl = Label(self.root, image=self.photoimg1)
        F_lbl.place(x=1000, y=0, width=550, height=130) 
        
        
        #  Thrid Image
        img3 = Image.open(r"College Image\\image2.jpeg")
        img3 = img3.resize((550, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        F_lbl = Label(self.root, image=self.photoimg3)
        F_lbl.place(x=500, y=0, width=550, height=130)  
        
        # BG_Images
        img4 = Image.open(r"College Image\\or.jpeg")
        img4 = img4.resize((1530, 720), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_image = Label(self.root, image=self.photoimg4)
        bg_image.place(x=0, y=130, width=1530, height=720)
        
        # title 
        
        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE ",font=("times new romen",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Studant b
        img5 = Image.open(r"College Image\\Student.jpeg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
         
        b1=Button(bg_image,image=self.photoimg5,command=self.student_Button_work,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Student Details",command=self.student_Button_work,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        # Face detector
        img6 = Image.open(r"College Image\\Face Detector.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
         
        b1=Button(bg_image,image=self.photoimg6,command=self.face_recognizer,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_recognizer,font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
         #  Attendance
        img7 = Image.open(r"College Image\\CollegeA.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
         
        b1=Button(bg_image,image=self.photoimg7,command=self.Attendance_detail,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Attendance",command=self.Attendance_detail,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        #  Help 
        img8 = Image.open(r"College Image\\Help.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
         
        b1=Button(bg_image,image=self.photoimg8,command=self.help_detail,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Help",cursor="hand2",command=self.help_detail,font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        # Train Data b
        img9 = Image.open(r"College Image\\Train.jpeg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
         
        b1=Button(bg_image,image=self.photoimg9,command=self.Train_Data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Train Data ",command=self.Train_Data,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        # Photos 
        img10 = Image.open(r"College Image\\Photo.jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
         
        b1=Button(bg_image,image=self.photoimg10,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Photos ",cursor="hand2",command=self.open_img,font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        #  Developer
        img11 = Image.open(r"College Image\\Developer.jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
         
        b1=Button(bg_image,image=self.photoimg11,command=self.Developer_detail,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Developer",command=self.Developer_detail,cursor="hand2",font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        #  Exit 
        img12 = Image.open(r"College Image\\Exit.png")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
         
        b1=Button(bg_image,image=self.photoimg12,command=self.iEXIT,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Exit",cursor="hand2",command=self.iEXIT,font=("times new romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
        
        
        
    def open_img(self):
        os.startfile("data")  
        
    def iEXIT(self):
        self.iEXIT=messagebox.askyesno("Face Recognition","Are you sure you want to EXIT? ",parent=self.root)
        if self.iEXIT >0:
            self.root.destroy()
        else:
            return
        
        
        
        
        
        # =============== function System==================
        
    def student_Button_work(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Detail(self.new_window)
        
        
    def Train_Data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def Developer_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
    def Attendance_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_st(self.new_window)
        
    def help_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)
            



 




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
