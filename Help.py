from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new romen",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # Full
        img_Full = Image.open(r"College Image\\helpb.jpeg")
        img_Full = img_Full.resize((1530, 950), Image.LANCZOS)
        self.photoimg_Full = ImageTk.PhotoImage(img_Full)
        
        bg_image = Label(self.root, image=self.photoimg_Full)
        bg_image.place(x=0, y=46, width=1530, height=950)
        
        
        
        dep_label=Label(bg_image,text=" Email: agam8126@gmail.com",font=("times new romen",20,"bold"),bg="black",fg="yellow")
        dep_label.place(x=560,y=380)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()