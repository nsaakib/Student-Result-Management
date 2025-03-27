from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#f5f5f5")
        self.root.focus_force()

        # TITLE
        title = Label(self.root, text="Manage Studnet Details", 
                      font=("Goudy Old Style", 20, "bold"), 
                      bg="#004080", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        #VARIABLES
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()
        self.var_pin=StringVar()


        #WIDGETS
        #COLUMN1
        lbl_roll = Label(self.root, text="Roll No.", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_roll.place(x=10, y=60)

        lbl_name = Label(self.root, text="Name", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_name.place(x=10, y=100)

        lbl_email = Label(self.root, text="E-mail", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_email.place(x=10, y=140)

        lbl_gender = Label(self.root, text="Gender", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_gender.place(x=10, y=180)

        lbl_state = Label(self.root, text="State", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_state.place(x=10, y=220)

        lbl_city = Label(self.root, text="City", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_city.place(x=310, y=220)

        lbl_pin = Label(self.root, text="Pin", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_pin.place(x=500, y=220)

        lbl_address= Label(self.root, text="Address", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_address.place(x=10, y=260)

        #COLUMN2
        lbl_dob = Label(self.root, text="D.O.B", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_dob.place(x=360, y=60)

        lbl_contact = Label(self.root, text="Contact", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_contact.place(x=360, y=100)

        lbl_admission = Label(self.root, text="Admission", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_admission.place(x=360, y=140)

        lbl_course = Label(self.root, text="Course", font=("Goudy Old Style", 15, "bold"), bg="#f5f5f5")
        lbl_course.place(x=360, y=180)

        #ENTRY FIELDS
        #COLUMN1
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_name.place(x=150, y=100, width=200)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_email.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Others"), font=("Goudy Old Style", 15, "bold"), state='readonly',justify= CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        self.txt_address = Text(self.root, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=500, height=100)

        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_state.place(x=150, y=220, width=150)

        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_city.place(x=380, y=220, width=100)
        
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_pin.place(x=560, y=220, width=120)

        #COLUMN2
        self.course_list = []
        #function call
        self.fetch_course()

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_contact.place(x=480, y=100, width=200)

        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        txt_admission.place(x=480, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=(self.course_list), font=("Goudy Old Style", 15, "bold"), state='readonly',justify= CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")

        #BUTTONS
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2", command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2", command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2", command= self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command= self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #SEARCH PANEL
        self.var_search = StringVar()

        lbl_search_roll= Label(self.root, text="Search by | Roll No.", font=("Goudy Old Style", 10, "bold"), bg="#f5f5f5")
        lbl_search_roll.place(x=720, y=60)

        self.search_CourseName= Entry(self.root, textvariable=self.var_search, font=("Goudy Old Style", 15, "bold"), bg="lightyellow")
        self.search_CourseName.place(x=870, y=60, width=180)

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2", command= self.search)
        btn_search.place(x=1070,y=60,width=120,height=28)

        #CONTENT
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        self.CourseTable=ttk.Treeview(self.c_frame,columns=("Roll","Name","Email","Gender","DOB","Contact","Admission","Course","State","City","Pin","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("Roll",text="Roll No.")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Email",text="E-mail")
        self.CourseTable.heading("Gender",text="Gender")
        self.CourseTable.heading("DOB",text="D.O.B")
        self.CourseTable.heading("Contact",text="Contact")
        self.CourseTable.heading("Admission",text="Admission")
        self.CourseTable.heading("Course",text="Course")
        self.CourseTable.heading("State",text="State")
        self.CourseTable.heading("City",text="City")
        self.CourseTable.heading("Pin",text="Pin")
        self.CourseTable.heading("Address",text="Address")

        self.CourseTable["show"]='headings'

        self.CourseTable.column("Roll",width=100)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("Email",width=100)
        self.CourseTable.column("Gender",width=100)
        self.CourseTable.column("DOB",width=100)
        self.CourseTable.column("Contact",width=100)
        self.CourseTable.column("Admission",width=100)
        self.CourseTable.column("Course",width=100)
        self.CourseTable.column("State",width=100)
        self.CourseTable.column("City",width=100)
        self.CourseTable.column("Pin",width=100)
        self.CourseTable.column("Address",width=200)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        

#sub function for db connection

#clear 

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),  
        self.var_email.set(""), 
        self.var_gender.set(""),  
        self.var_dob.set(""),  
        self.var_contact.set(""),  
        self.var_a_date.set(""),  
        self.var_course.set(""), 
        self.var_state.set(""), 
        self.var_city.set(""),  
        self.var_pin.set(""),  
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

# delete

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required", parent = self.root)
            else:
                cur.execute("select * from student where Roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please select Student from the list first", parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from student where Roll =?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student info deleted successfully", parent = self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    def get_data(self, ev):
        self.txt_roll.config(state='readonly')

        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),  
        self.var_email.set(row[2]), 
        self.var_gender.set(row[3]),  
        self.var_dob.set(row[4]),  
        self.var_contact.set(row[5]),  
        self.var_a_date.set(row[6]),  
        self.var_course.set(row[7]), 
        self.var_state.set(row[8]), 
        self.var_city.set(row[9]),  
        self.var_pin.set(row[10]),  
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[11])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required", parent = self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Course Name available", parent = self.root)
                else:
                  cur.execute("""
                        INSERT INTO student (Roll, Name, Email, Gender, DOB, Contact, Admission, Course, State, City, Pin, Address) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        self.var_roll.get(),
                        self.var_name.get(),  
                        self.var_email.get(),  
                        self.var_gender.get(),  
                        self.var_dob.get(),  
                        self.var_contact.get(),  
                        self.var_a_date.get(),  
                        self.var_course.get(), 
                        self.var_state.get(), 
                        self.var_city.get(),  
                        self.var_pin.get(),  
                        self.txt_address.get("1.0", END)  
                    ))

                con.commit()
                messagebox.showinfo("Success", "Course Added Successfully", parent= self.root)
#calling show function
                self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#update

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required", parent = self.root)
            else:
                cur.execute("select * from student where Roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select Student from list", parent = self.root)
                else:
                  cur.execute("update student set Name = ?, Email = ?, Gender = ?, DOB = ?, Contact = ?, Admission = ?, Course = ?, State = ?, City = ?, Pin = ?, Address = ? WHERE Roll = ?", 
                            (
                                self.var_name.get(),  
                                self.var_email.get(),  
                                self.var_gender.get(),  
                                self.var_dob.get(),  
                                self.var_contact.get(),  
                                self.var_a_date.get(),  
                                self.var_course.get(),  
                                self.var_state.get(),  
                                self.var_city.get(),  
                                self.var_pin.get(),  
                                self.txt_address.get("1.0", END),  
                                self.var_roll.get()
                            )
                        )

                con.commit()
                messagebox.showinfo("Success", "Student Details Updated Successfully", parent= self.root)
#calling show function
                self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


# show function
  
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#FETCH COURSE

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select Name from course")
            rows = cur.fetchall()
            
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#search
   
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student where Roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
