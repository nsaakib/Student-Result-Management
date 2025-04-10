from tkinter import *
import time
import math

class AnalogClock:
    def __init__(self, parent):
        self.parent = parent
        self.clock_frame = LabelFrame(self.parent, text="Analog Clock", font=("times new roman", 15), bg="white")
        self.clock_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.canvas_width = 350
        self.canvas_height = 220
        self.canvas = Canvas(self.clock_frame, width=self.canvas_width, height=self.canvas_height, bg="white", bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.center_x = self.canvas_width / 2
        self.center_y = self.canvas_height / 2
        self.clock_radius = min(self.center_x, self.center_y) - 20

        self.update_clock()

    def update_clock(self):
        hr = int(time.strftime("%I"))
        mi = int(time.strftime("%M"))
        sc = int(time.strftime("%S"))
        am_pm = time.strftime("%p")

        self.canvas.delete("all")

        # Draw clock face
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                self.center_x + self.clock_radius, self.center_y + self.clock_radius, outline="black", width=2)

        # Draw hour markers
        for i in range(12):
            angle = (i * math.pi / 6) - (math.pi / 2)  
            x = self.center_x + (self.clock_radius - 15) * math.cos(angle)
            y = self.center_y + (self.clock_radius - 15) * math.sin(angle)
            number = 12 if i == 0 else i  
            self.canvas.create_text(x, y, text=str(number), font=("arial", 10))

        # Draw minute markers
        for i in range(60):
            if i % 5 != 0:
                angle = i * math.pi / 30 - math.pi / 2
                x = self.center_x + (self.clock_radius - 5) * math.cos(angle)
                y = self.center_y + (self.clock_radius - 5) * math.sin(angle)
                self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="black")

        # Hour hand
        hr_angle = (hr * 30 + mi * 0.5) * math.pi / 180 - math.pi / 2
        hr_x = self.center_x + (self.clock_radius * 0.4) * math.cos(hr_angle)
        hr_y = self.center_y + (self.clock_radius * 0.4) * math.sin(hr_angle)
        self.canvas.create_line(self.center_x, self.center_y, hr_x, hr_y, fill="black", width=4)

        # Minute hand
        mi_angle = (mi * 6 + sc * 0.1) * math.pi / 180 - math.pi / 2
        mi_x = self.center_x + (self.clock_radius * 0.6) * math.cos(mi_angle)
        mi_y = self.center_y + (self.clock_radius * 0.6) * math.sin(mi_angle)
        self.canvas.create_line(self.center_x, self.center_y, mi_x, mi_y, fill="blue", width=3)

        # Second hand
        sc_angle = sc * 6 * math.pi / 180 - math.pi / 2
        sc_x = self.center_x + (self.clock_radius * 0.7) * math.cos(sc_angle)
        sc_y = self.center_y + (self.clock_radius * 0.7) * math.sin(sc_angle)
        self.canvas.create_line(self.center_x, self.center_y, sc_x, sc_y, fill="red", width=2)

        # Center dot
        self.canvas.create_oval(self.center_x - 5, self.center_y - 5, self.center_x + 5, self.center_y + 5, fill="black")

        # AM/PM indicator
        self.canvas.create_text(self.center_x, self.center_y + self.clock_radius - 10, text=am_pm, font=("arial", 10))

        self.canvas.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    clock_app = AnalogClock(root)
    root.mainloop()