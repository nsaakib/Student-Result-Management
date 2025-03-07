from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#f5f5f5")
        self.root.focus_force()

        # TITLE
        title = Label(self.root, text="Manage Course Details", 
                      font=("Goudy Old Style", 20, "bold"), 
                      bg="#004080", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        #VARIABLES
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #WIDGETS
        lbl_course_name = Label(self.root, text="Course Name", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_course_name.place(x=10, y=60)

        lbl_duration = Label(self.root, text="Duration", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_duration.place(x=10, y=100)

        lbl_charges = Label(self.root, text="Charges", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_charges.place(x=10, y=140)

        lbl_description = Label(self.root, text="Description", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_description.place(x=10, y=180)

        #ENTRY FIELDS
        self.txt_course_name = Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_course_name.place(x=150, y=60, width=200)

        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_duration.place(x=150, y=100, width=200)

        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_charges.place(x=150, y=140, width=200)

        self.txt_description = Text(self.root, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=150, y=180, width=500, height=130)

        #BUTTONS
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2", command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2")
        self.btn_update.place(x=270,y=400,width=110,height=40)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2")
        self.btn_delete.place(x=390,y=400,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2")
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #SEARCH PANEL
        self.var_search = StringVar()
        lbl_search_CourseName = Label(self.root, text="Search by | Course Name", font=("Goudy Old Style", 10, "bold"), bg="#f5f5f5")
        lbl_search_CourseName.place(x=720, y=60)

        self.search_CourseName= Entry(self.root, textvariable=self.var_search, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.search_CourseName.place(x=870, y=60, width=180)

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2")
        btn_search.place(x=1070,y=60,width=120,height=28)

        #CONTENT
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        self.CourseTable=ttk.Treeview(self.c_frame,columns=("C_id","Name","Duration","Charges","Description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("C_id",text="Course ID")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Duration",text="Duration")
        self.CourseTable.heading("Charges",text="Charges")
        self.CourseTable.heading("Description",text="Description")

        self.CourseTable["show"]='headings'

        self.CourseTable.column("C_id",width=100)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("Duration",width=100)
        self.CourseTable.column("Charges",width=100)
        self.CourseTable.column("Description",width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)

#sub function

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required", parent = self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Course Name available", parent = self.root)
                else:
                    cur.execute("insert into course (name, duration, charges, description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent= self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()