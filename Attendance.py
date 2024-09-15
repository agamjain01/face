from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[] 

class Attendance_st:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        # ===========================Variable=================
        self.var_att_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_att=StringVar()
       
        
        
        # First Image
        img = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\images.jpeg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        F_lbl = Label(self.root, image=self.photoimg)
        F_lbl.place(x=0, y=0, width=800, height=200)  
        
        # Second  Image
        img1 = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\download.jpeg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        F_lbl = Label(self.root, image=self.photoimg1)
        F_lbl.place(x=800, y=0, width=800, height=200)
        
        
        # BG_Images
        img4 = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\or.jpeg")
        img4 = img4.resize((1530, 720), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_image = Label(self.root, image=self.photoimg4)
        bg_image.place(x=0, y=200, width=1530, height=720)
        
        # title 
        
        title_lbl=Label(bg_image,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new romen",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_Frame=Frame(bg_image,bd=2)
        main_Frame.place(x=20,y=50,width=1480,height=600)
        
        # Left label Frame
        
        left_Frame=LabelFrame(main_Frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new romen",12,"bold"))
        left_Frame.place(x=10,y=10,width=740,height=580)
        
        # Left_label  Image
        img_left = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\Left_Label_image.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        F_lbl = Label(left_Frame, image=self.photoimg_left)
        F_lbl.place(x=5, y=0, width=720, height=130)
        
        left_insert_Frame=Frame(left_Frame,bd=2,relief=RIDGE,bg='white')
        left_insert_Frame.place(x=5,y=135,width=720,height=350) 
        
        # lable And entry
        
        # Attendance  Id
        
        AttendanceId_label=Label(left_insert_Frame,text="AttendanceId: ",font=("times new romen",10,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        AttendanceId_Entry=ttk.Entry(left_insert_Frame,width=20,textvariable=self.var_att_id,font=("times new romen",10,"bold"))
        AttendanceId_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        # RollNo
        
        RollNo_label=Label(left_insert_Frame,text="RollNo: ",font=("times new romen",10,"bold"),bg="white")
        RollNo_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)
        
        RollNo_Entry=ttk.Entry(left_insert_Frame,width=20,textvariable=self.var_roll,font=("times new romen",10,"bold"))
        RollNo_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        
        # Name
        
        Name_label=Label(left_insert_Frame,text="Name: ",font=("times new romen",10,"bold"),bg="white")
        Name_label.grid(row=1,column=0)
        
        Name_Entry=ttk.Entry(left_insert_Frame,width=20,textvariable=self.var_name,font=("times new romen",10,"bold"))
        Name_Entry.grid(row=1,column=1,pady=5)
        
        
        # dep
        
        dep_label=Label(left_insert_Frame,text="department: ",font=("times new romen",10,"bold"),bg="white")
        dep_label.grid(row=1,column=2)
        
        dep_Entry=ttk.Entry(left_insert_Frame,width=20,textvariable=self.var_dep,font=("times new romen",10,"bold"))
        dep_Entry.grid(row=1,column=3,pady=5)
        
        
        # Time
        
        Time_label=Label(left_insert_Frame,text="Time: ",font=("times new romen",10,"bold"),bg="white")
        Time_label.grid(row=2,column=0)
        
        Time_Entry=ttk.Entry(left_insert_Frame,width=20,textvariable=self.var_time,font=("times new romen",10,"bold"))
        Time_Entry.grid(row=2,column=1,pady=5)
        
        # date
        
        date_label=Label(left_insert_Frame,text="date: ",font=("times new romen",10,"bold"),bg="white")
        date_label.grid(row=2,column=2)
        
        date_Entry=ttk.Entry(left_insert_Frame,textvariable=self.var_date,width=20,font=("times new romen",10,"bold"))
        date_Entry.grid(row=2,column=3,pady=5)
        
        
        # Attendance
        
        status_label=Label(left_insert_Frame,text="Attendance status: ",font=("times new romen",10,"bold"),bg="white")
        status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Attendance_status_combo=ttk.Combobox(left_insert_Frame,font=("times new romen",10,"bold"),textvariable=self.var_att,state="readonly",width=18)
        Attendance_status_combo["values"]=("Status","Present","adsent")
        Attendance_status_combo.current(0) 
        Attendance_status_combo.grid(row=3,column=1,padx=3,pady=5,sticky=W)
        
        
        # Button frame 
        
        
        Button_frame=Label(left_insert_Frame,bg="white",bd=2,relief=RIDGE)
        Button_frame.place(x=0,y=300,width=715,height=32)
        
        # import_csv 
        
        import_csv_Butt=Button(Button_frame,text="import csv ",command=self.importCSV,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        import_csv_Butt.grid(row=0,column=0)
        # Export
        
             
        Export_Butt=Button(Button_frame,text="Export csv ",command=self.ExportCsv,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Export_Butt.grid(row=0,column=1)
        # Update
        
        
        Update_Butt=Button(Button_frame,text="Update ",width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Update_Butt.grid(row=0,column=2)
        
        # Reset
        Reset_Butt=Button(Button_frame,text= "Reset",command=self.re_button,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Reset_Butt.grid(row=0,column=3)
        
        
        
        
        
        # RSH LABLE
        Right_Frame=LabelFrame(main_Frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new romen",12,"bold"))
        Right_Frame.place(x=760,y=10,width=710,height=580)
        
        
        table_frame=Label(Right_Frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=695,height=490)
        
        
        
        # ======================= scroll bar table =====================
        
        Scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","Attendance"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        
        
        Scrollbar_x.config(command=self.AttendanceReportTable.xview)
        Scrollbar_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance Id ")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
        
    

        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        
        self.AttendanceReportTable.bind("ButtonRelease",self.get_cursor)
        
        
    # =======================fectch_data==============================
        
    def fectch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
     
     # import Csv       
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSv file","*.csv"),("All file","*.*")),parent=self.root)
        
        with open(fln)  as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fectch_data(mydata)
    
    
    # import Csv 
    
    def ExportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSv file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","You data is Exported to  "+os.path.basename(fln)+"  successfully")       
        
        
        except Exception as e:
                messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root)    
        
        
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"] 
        self.var_att_id.set(rows[0]) 
        self.var_roll.set(rows[1])  
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_att.set(rows[6])



    def re_button(self):
        self.var_att_id.set("") 
        self.var_roll.set("")  
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_att.set("")
            
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance_st(root)
    root.mainloop()