from tkinter import *
from PIL import Image,ImageTk
from Course import CourseClass
from Student import StudentClass
from Result import ResultClass
from clock import AnalogClock
from Report import ReportClass
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#f5f5f5")

        # ICONS
        img = Image.open("logo_p.png")
        img = img.resize((50, 50), Image.Resampling.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(img)

        # TITLE
        title = Label(self.root, text="Student Result Management System", 
                     font=("Goudy Old Style", 22, "bold"), 
                     bg="#004080", fg="white",
                     image=self.logo_dash, compound=LEFT, padx=10)
        title.place(x=0, y=0, relwidth=1, height=60)

        # MENU
        M_frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_frame.place(x=10, y=70, width=1340, height=80)

        btn_course = Button(M_frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)

        btn_student = Button(M_frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377",
                           fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=270, y=5, width=200, height=40)

        btn_result = Button(M_frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=520, y=5, width=200, height=40)

        btn_view = Button(M_frame, text="View Student Result", font=("goudy old style", 15, "bold"),
                         bg="#0b5377", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=770, y=5, width=200, height=40)

        btn_exit = Button(M_frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377",
                         fg="white", cursor="hand2", command=self.exit_app)
        btn_exit.place(x=1020, y=5, width=200, height=40)

        # ANALOG CLOCK
        self.analog_clock = AnalogClock(self.root)
        self.analog_clock.clock_frame.place(x=10, y=260, width=380, height=250)

        # CONTENT WINDOW
        self.bg_img = Image.open("result.jpg")
        self.bg_img = self.bg_img.resize((920,350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        # UPDATE DETAILS
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style",20),
                              bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style",20),
                               bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style",20),
                              bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # FOOTER
        footer = Label(self.root, text="SRMS- Student Result Management System\nContact us for any technical issues: 017XX-XXXXXX", 
                     font=("Goudy Old Style", 12), 
                     bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        # Initialize counts
        self.update_counts()
        
        # Set up auto-refresh
        self.auto_refresh()

    def auto_refresh(self):
        self.update_counts()
        self.root.after(5000, self.auto_refresh)  # Refresh every 5 seconds

    def update_counts(self):
        """Fetch and update the counts from the database"""
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # Fetch total courses
            cur.execute("SELECT COUNT(*) FROM course")
            total_courses = cur.fetchone()[0]
            self.lbl_course.config(text=f"Total Courses\n[ {total_courses} ]")

            # Fetch total students
            cur.execute("SELECT COUNT(*) FROM student")
            total_students = cur.fetchone()[0]
            self.lbl_student.config(text=f"Total Students\n[ {total_students} ]")

            # Fetch total results
            cur.execute("SELECT COUNT(*) FROM result")
            total_results = cur.fetchone()[0]
            self.lbl_result.config(text=f"Total Results\n[ {total_results} ]")

        except Exception as ex:
            print(f"Error updating counts: {ex}")  # Print to console for debugging
        finally:
            con.close()

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_course_close)

    def on_course_close(self):
        self.new_win.destroy()
        self.update_counts()

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_student_close)

    def on_student_close(self):
        self.new_win.destroy()
        self.update_counts()

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_result_close)

    def on_result_close(self):
        self.new_win.destroy()
        self.update_counts()
        
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
