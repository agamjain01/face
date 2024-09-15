from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student_Detail:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # ====================== Variable==============
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_st_id=StringVar()
        self.var_st_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
      
      
      
    # First Image
        img = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\images.jpeg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        F_lbl = Label(self.root, image=self.photoimg)
        F_lbl.place(x=0, y=0, width=500, height=130)  
        
        # Second  Image
        img1 = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\download.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        F_lbl = Label(self.root, image=self.photoimg1)
        F_lbl.place(x=1000, y=0, width=550, height=130) 
        
        
        #  Thrid Image
        img3 = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\IMG_20221229_122349.jpg")
        img3 = img3.resize((550, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        F_lbl = Label(self.root, image=self.photoimg3)
        F_lbl.place(x=500, y=0, width=550, height=130)    
        
        
        # BG_Images
        img4 = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\or.jpeg")
        img4 = img4.resize((1530, 720), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_image = Label(self.root, image=self.photoimg4)
        bg_image.place(x=0, y=130, width=1530, height=720)
        
        # title 
        
        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM ",font=("times new romen",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_Frame=Frame(bg_image,bd=2)
        main_Frame.place(x=20,y=50,width=1480,height=600)
        
        
        # Left label Frame
        
        left_Frame=LabelFrame(main_Frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold"))
        left_Frame.place(x=10,y=10,width=740,height=580)
        
        # Left_label  Image
        img_left = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\Left_Label_image.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        F_lbl = Label(left_Frame, image=self.photoimg_left)
        F_lbl.place(x=5, y=0, width=720, height=130) 
        
        # Current Course Infromention
        
        Current_Label_Frame=LabelFrame(left_Frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infromention",font=("times new romen",12,"bold"))
        Current_Label_Frame.place(x=5,y=135,width=720,height=110)
        
        # Department 
        dp_label=Label(Current_Label_Frame,text="Department ",font=("times new romen",10,"bold"),bg="white")
        dp_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dp_combo=ttk.Combobox(Current_Label_Frame,textvariable=self.var_dep,font=("times new romen",10,"bold"),state="readonly")
        dp_combo["values"]=("Select Department","Computer Sicence ","Civil ","Mechnical")
        dp_combo.current(0)
        dp_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        
        # course 
        
        Cou_label=Label(Current_Label_Frame,text="Course ",font=("times new romen",10,"bold"),bg="white")
        Cou_label.grid(row=0,column=2,padx=10,sticky=W)
        
        Course_combo=ttk.Combobox(Current_Label_Frame,textvariable=self.var_course,font=("times new romen",10,"bold"),state="readonly")
        Course_combo["values"]=("Select Course","CSE ","IBM","AI & ML ","TCS")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)
        
        
        # Year
        
        year_label=Label(Current_Label_Frame,text="Year ",font=("times new romen",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_Label_Frame,textvariable=self.var_year,font=("times new romen",10,"bold"),state="readonly")
        year_combo["values"]=("Select Course","2020-2021 ","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0) 
        year_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)
        # Semester
        
        Semester_label=Label(Current_Label_Frame,text="Semester ",font=("times new romen",10,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(Current_Label_Frame,textvariable=self.var_semester,font=("times new romen",10,"bold"),state="readonly")
        Semester_combo["values"]=("Select Semester","Semester 1","Semester 2","Semester 3","Semester 4")
        Semester_combo.current(0) 
        Semester_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)
        
        
        # Class Student Infromention
        
        class_Student_Frame=LabelFrame(left_Frame,bd=2,bg="white",relief=RIDGE,text="Class Student Infromention",font=("times new romen",12,"bold"))
        class_Student_Frame.place(x=5,y=250,width=720,height=300)
        
        # Student ID 
        
        Student_ID_label=Label(class_Student_Frame,text="Student ID: ",font=("times new romen",10,"bold"),bg="white")
        Student_ID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Student_ID_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_st_id,width=20,font=("times new romen",10,"bold"))
        Student_ID_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Student Name
        
        Student_Name_label=Label(class_Student_Frame,text="Student Name: ",font=("times new romen",10,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Student_Name_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_st_name,width=20,font=("times new romen",10,"bold"))
        Student_Name_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Student division
        
        Student_Div_label=Label(class_Student_Frame,text="Division: ",font=("times new romen",10,"bold"),bg="white")
        Student_Div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # Student_Div_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_div,width=20,font=("times new romen",10,"bold"))
        # Student_Div_Entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_Student_Frame,textvariable=self.var_div,font=("times new romen",10,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0) 
        div_combo.grid(row=1,column=1,padx=3,pady=5,sticky=W)
        
        
        
        # Roll Number
        
        Roll_number_label=Label(class_Student_Frame,text="Roll Number: ",font=("times new romen",10,"bold"),bg="white")
        Roll_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Roll_number_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_roll,width=20,font=("times new romen",10,"bold"))
        Roll_number_Entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        # Gander 
        
        Student_Gender_label=Label(class_Student_Frame,text="Gender: ",font=("times new romen",10,"bold"),bg="white")
        Student_Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        Gender_combo=ttk.Combobox(class_Student_Frame,textvariable=self.var_gender,font=("times new romen",10,"bold"),state="readonly",width=18)
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0) 
        Gender_combo.grid(row=2,column=1,padx=3,pady=5,sticky=W)
        
        
        
        # DOB
        
        Student_DOB_label=Label(class_Student_Frame,text="DOB: ",font=("times new romen",10,"bold"),bg="white")
        Student_DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Student_DOB_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_dob,width=20,font=("times new romen",10,"bold"))
        Student_DOB_Entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        # Email
        
        Student_Email_label=Label(class_Student_Frame,text="Email: ",font=("times new romen",10,"bold"),bg="white")
        Student_Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Student_Email_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_email,width=20,font=("times new romen",10,"bold"))
        Student_Email_Entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        # Phone Number 
        
        Student_Phone_label=Label(class_Student_Frame,text="Phone no.: ",font=("times new romen",10,"bold"),bg="white")
        Student_Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Student_Phone_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_phone,width=20,font=("times new romen",10,"bold"))
        Student_Phone_Entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        
        Student_Address_label=Label(class_Student_Frame,text="Address: ",font=("times new romen",10,"bold"),bg="white")
        Student_Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        Student_Address_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_address,width=20,font=("times new romen",10,"bold"))
        Student_Address_Entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher Name
        
        Student_Teacher_label=Label(class_Student_Frame,text="Teacher Name: ",font=("times new romen",10,"bold"),bg="white")
        Student_Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        Student_Teacher_Entry=ttk.Entry(class_Student_Frame,textvariable=self.var_teacher,width=20,font=("times new romen",10,"bold"))
        Student_Teacher_Entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        # RADIOBUTTON
        self.var_radioBu1=StringVar()
        RadioBu1=ttk.Radiobutton(class_Student_Frame,variable=self.var_radioBu1,text="Take a Photo",value="Yes")
        RadioBu1.grid(row=5,column=0)
         
        
        RadioBu2=ttk.Radiobutton(class_Student_Frame,variable=self.var_radioBu1,text="No a Photo",value="No")
        RadioBu2.grid(row=5,column=1)
        
        
        
        # Button frame 
        
        
        Button_frame=Label(class_Student_Frame,bg="white",bd=2,relief=RIDGE)
        Button_frame.place(x=0,y=190,width=715,height=32)
        
        # Save 
        
        Save_Butt=Button(Button_frame,text="Save ",command=self.Add_data,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Save_Butt.grid(row=0,column=0)
        # UPDATE
        
             
        UPDATE_Butt=Button(Button_frame,text="UPDATE ",command=self.update_data,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        UPDATE_Butt.grid(row=0,column=1)
        # Delete
        
        
        Delete_Butt=Button(Button_frame,text="Delete ",command=self.Delect_data,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Delete_Butt.grid(row=0,column=2)
        
        # Reset
        Reset_Butt=Button(Button_frame,text= "Reset",command=self.reset_data,width=21,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Reset_Butt.grid(row=0,column=3)
        
        
        # Button frame1 
        
        
        Button_frame1=Label(class_Student_Frame,bg="white",bd=2,relief=RIDGE)
        Button_frame1.place(x=0,y=225,width=715,height=32)
        
        Take_photo_Butt=Button(Button_frame1,text="Take photo Sample ",command=self.generate_data,width=45,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Take_photo_Butt.grid(row=1,column=0)   
        
        Take_photo_Butt=Button(Button_frame1,text="Take photo ",width=45,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Take_photo_Butt.grid(row=1,column=1)
        
        # Right label Frame
        
        Right_Frame=LabelFrame(main_Frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold"))
        Right_Frame.place(x=760,y=10,width=710,height=580)
        
        
        # Right_label  Image
        img_Right = Image.open(r"C:\\Users\\hp\\OneDrive\Desktop\\Project\\College Image\\Left_Label_image.jpeg")
        img_Right = img_left.resize((690, 130), Image.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)
        
        # RSH Image
        
        F_lbl = Label(Right_Frame, image=self.photoimg_Right)
        F_lbl.place(x=5, y=0, width=690, height=130) 
        
        
        # ================ Search System ======================
        
        Search_Frame=LabelFrame(Right_Frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new romen",12,"bold"))
        Search_Frame.place(x=5,y=135,width=690,height=70)
        
        Search_label=Label(Search_Frame,text="Search By : ",font=("times new romen",15,"bold"),bg="skyblue",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        # search_combo
        
        
        search_combo=ttk.Combobox(Search_Frame,font=("times new romen",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll No.","Phone No. ")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        
        # search  Entry
        
        search_Entry=ttk.Entry(Search_Frame,width=15,font=("times new romen",10,"bold"))
        search_Entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        # search 
        Search_Butt=Button(Search_Frame,text="Search ",width=10,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        Search_Butt.grid(row=0,column=3)
        
        # ShowAll
        ShowAll_Butt=Button(Search_Frame,text= "Show All",width=10,font=("times new romen",10,"bold"),bg="Blue",fg="White")
        ShowAll_Butt.grid(row=0,column=4,padx=3)
        
        
        # ================= Table Frame=======================
        
        Table_Frame=Frame(Right_Frame,bd=2,bg="white",relief=RIDGE,)
        Table_Frame.place(x=5,y=210,width=690,height=340)
        
        
        # Scrollbar
        
        Scrollbar_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        
        Scrollbar_x.config(command=self.Student_table.xview)
        Scrollbar_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("Dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Yaer")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("id",text="ID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("div",text="division")
        self.Student_table.heading("roll",text="Roll")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("phone",text="Phone")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("teacher",text="TeacherName")
        self.Student_table.heading("photo",text="Photo")
        self.Student_table["show"]="headings"
        
        
        
        self.Student_table.column("Dep",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("roll",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("phone",width=100)
        self.Student_table.column("address",width=100)
        self.Student_table.column("teacher",width=100)
        self.Student_table.column("photo",width=100)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        # ====================== Decration =================
        
        
    def Add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_st_name.get()=="" or self.var_st_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
            
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogintion")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_st_id.get(),
                                                                                                        self.var_st_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radioBu1.get()
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student information is add ",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root)   
    
    
    # ============================= fetch data======================
    
    def fetch_data(self):
    
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogintion")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_data")
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,value=i)
                conn.commit()
            conn.close()
                   
    
    # ============================= get cursor======================
    
    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),        
        self.var_semester.set(data[3]),
        self.var_st_id.set(data[4]),
        self.var_st_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radioBu1.set(data[14])
    
    
    
    # =====================Update function=============   
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_st_name.get()=="" or self.var_st_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogintion")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_data set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,division=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_st_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radioBu1.get(),
                                                                                                                                                                                                                self.var_st_id.get()
                                                                                                                                                                                                                ))
                
                    conn.commit()
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details Successfully Update",parent=self.root)
                self.fetch_data()
                conn.close()
            except Exception as e: 
                messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root) 
    
    
    # ===========================Delete Function====================
    
    def Delect_data(self):
        if self.var_st_id.get()=="":
            messagebox.showerror("Error","Student id must be requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Update","do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogintion")
                    my_cursor=conn.cursor()
                    sql="delete from student_data where Student_id=%s"
                    val=(self.var_st_id.get(),)
                    my_cursor.execute(sql,val)
                
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details Successfully delete",parent=self.root)
            except Exception as e: 
                messagebox.showerror("Error",f"Due to{str(e)}",parent=self.root) 
    # ============= Reset Data===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Setect Year")
        self.var_semester.set("Select Semester")
        self.var_st_id.set("")
        self.var_st_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radioBu1.set("")
        
        
        
        
    # =============================== generate data set or Photo Sample===============================
    
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_st_name.get() == "" or self.var_st_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recogintion")
                my_cursor = conn.cursor()
                
                # Get the highest ID in the table
                                
                student_id = self.var_st_id.get()
                
                # print("id : ", student_id)
                
                # Update the student's data
                my_cursor.execute("""
                    UPDATE student_data SET 
                        Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, 
                        division=%s, Roll=%s, Gender=%s, DOB=%s, 
                        Phone=%s, Email=%s, Address=%s, Teacher=%s, 
                        Photo_Sample=%s 
                    WHERE Student_id=%s
                """, (
                                                                            self.var_dep.get(),
                                                                            self.var_course.get(),
                                                                            self.var_year.get(),
                                                                            self.var_semester.get(),
                                                                            self.var_st_name.get(),
                                                                            self.var_div.get(),
                                                                            self.var_roll.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_email.get(),
                                                                            self.var_address.get(),
                                                                            self.var_teacher.get(),
                                                                            self.var_radioBu1.get(),
                                                                            self.var_st_id.get()
                                                                        ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # =========================== Load face with OpenCV ===========================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None  # Make sure to return None if no face is detected

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break
                    face = face_cropped(my_frame)
                    if face is not None:
                        img_id += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                        
                    if cv2.waitKey(1) == 13 or img_id == 100:  # WaitKey should be 1, not key
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed")
            
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)

             
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student_Detail(root)
    root.mainloop()
