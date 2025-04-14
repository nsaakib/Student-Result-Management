from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

class ReportClass:
    def __init__(self, root):  # <-- Corrected __init__
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#f5f5f5")
        self.root.focus_force()

        # TITLE
        title = Label(self.root, text="View Student Result",
                      font=("Goudy Old Style", 20, "bold"),
                      bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)

        # Search
        self.var_search = StringVar()
        self.var_id = ""

        lbl_search = Label(self.root, text="Search By Roll No.", font=("Goudy Old Style", 20, "bold"), bg="white")
        lbl_search.place(x=280, y=100)

        txt_search = Entry(self.root, textvariable=self.var_search, font=("Goudy Old Style", 20), bg="lightyellow")
        txt_search.place(x=520, y=100, width=150)

        btn_search = Button(self.root, text="Search", font=("Goudy Old Style", 15, "bold"),
                            bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=680, y=100, width=100, height=28)

        btn_clear = Button(self.root, text="Clear", font=("Goudy Old Style", 15, "bold"),
                           bg="gray", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=800, y=100, width=100, height=28)

        # Result labels (fixed Lable → Label)
        labels = ["Roll No", "Name", "Course", "Marks Obtained", "Total Marks", "Percentage"]
        x_positions = [150, 300, 450, 600, 750, 900]

        for i in range(6):
            Label(self.root, text=labels[i], font=("Goudy Old Style", 15, "bold"),
                  bg="white", bd=2, relief=GROOVE).place(x=x_positions[i], y=230, width=150, height=50)

        # Result fields
        self.roll = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)

        self.full = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=750, y=280, width=150, height=50)

        self.per = Label(self.root, font=("Goudy Old Style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)

        # Delete button
        btn_delete = Button(self.root, text="Delete", font=("Goudy Old Style", 15, "bold"),
                            bg="red", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=500, y=350, width=150, height=35)

    # Search function
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])

                    try:
                        marks_ob = float(row[4])
                        full_marks = float(row[5])
                        percentage = (marks_ob / full_marks) * 100
                        self.per.config(text=f"{percentage:.2f}%")
                    except (ValueError, ZeroDivisionError):
                        self.per.config(text="N/A")
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Clear function
    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    # Delete function
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search student result first", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rid=?", (self.var_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM result WHERE rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__ == "__main__":  # <-- Corrected from _name_
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()
