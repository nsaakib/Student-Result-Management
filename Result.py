from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#f5f5f5")
        self.root.focus_force()

        # TITLE
        title = Label(self.root, text="Add Student Result", 
                      font=("Goudy Old Style", 20, "bold"), 
                      bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)

        #VARIABLES
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #WIDGETS
        lbl_select= Label(self.root, text="Select Student", font=("Goudy Old Style", 20, "bold"), bg="white")
        lbl_select.place(x=50, y=100)

        lbl_name = Label(self.root, text="Name", font=("Goudy Old Style", 20 , "bold"), bg="white")
        lbl_name.place(x=50, y=160)

        lbl_course = Label(self.root, text="Course", font=("Goudy Old Style", 20, "bold"), bg="white")
        lbl_course.place(x=50, y=220)

        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("Goudy Old Style", 20, "bold"), bg="white")
        lbl_marks_ob.place(x=50, y=280)

        lbl_full_marks = Label(self.root, text="Full Marks", font=("Goudy Old Style", 20, "bold"), bg="white")
        lbl_full_marks.place(x=50, y=340)

        #ENTRY FIELDS
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll,values=(self.roll_list), font=("Goudy Old Style", 15, "bold"), state='readonly',justify= CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=500,y=100,width=100,height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Goudy Old Style", 20, "bold"), bg="lightyellow",state="readonly")
        txt_name.place(x=280, y=160, width=320)

        txt_course = Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 20, "bold"), bg="lightyellow",state="readonly")
        txt_course.place(x=280, y=220, width=320)

        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("Goudy Old Style", 20, "bold"), bg="lightyellow")
        txt_marks.place(x=280, y=280, width=320)

        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("Goudy Old Style", 20, "bold"), bg="lightyellow")
        txt_full_marks.place(x=280, y=340, width=320)

        #BUTTON
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add)
        btn_add.place(x=300,y=420,width=120,height=35)

        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear)
        btn_clear.place(x=430,y=420,width=120,height=35)

        #IMAGE
        img = Image.open("picture.jpg")  # Load the image
        img = img.resize((50, 50), Image.Resampling.LANCZOS)

        self.bg_img=Image.open("picture.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img)
        self.lbl_bg.place(x=650,y=100)


 #FETCH ROLL

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select Roll from student")
            rows = cur.fetchall()
            
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    #SEARCH BY ROLL
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row = cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #ADD
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record", parent = self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Result already present", parent = self.root)
                else:
                    cur.execute("""insert into result (roll, name, course, marks_ob, full_marks) values(?,?,?,?,?)""",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent= self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set("")
    



if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()