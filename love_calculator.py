import tkinter as tk
import math
import random
import time
import turtle

class Love_Calculator_app:
    def __init__(self, window):
        self.window = window
        self.window.title("Love Calculator App")
        self.window.geometry("350x200")  # Fixed format
        self.window.resizable(False, False)

        # Canvas for drawing heart
        self.canvas = tk.Canvas(window, width=350, height=200, bg="white")
        self.canvas.pack()

        # Labels and Entries
        self.your_name_label = tk.Label(window, text="Your Name", bg="pink", relief="sunken")
        self.your_name_label.place(x=10, y=20)

        self.your_name_entry = tk.Entry(window)
        self.your_name_entry.place(x=10, y=50)

        self.your_crush_name_label = tk.Label(window, text="Your Crush Name", bg="pink", relief="sunken")
        self.your_crush_name_label.place(x=180, y=20)

        self.your_crush_name_entry = tk.Entry(window)
        self.your_crush_name_entry.place(x=180, y=50)

        # Button to calculate love percentage
        self.calculate_button = tk.Button(window, text="Calculate", bg="cyan", command=self.calculate_love)
        self.calculate_button.place(x=20, y=130)

        # Result label
        self.result_label = tk.Label(window, text="", relief="ridge", bg="pink", width=25)
        self.result_label.place(x=150, y=130)

        # Turtle initialization
        self.heart_turtle = turtle.RawTurtle(self.canvas)
        self.heart_turtle.speed(0)
        self.heart_turtle.hideturtle()

    def calculate_love(self):
        your_name = self.your_name_entry.get()
        your_crush_name = self.your_crush_name_entry.get()

        if your_name and your_crush_name:
            self.calculate_button.config(state="disabled")

            # Reset turtle
            self.heart_turtle.clear()
            self.heart_turtle.penup()
            self.heart_turtle.goto(0, -10)
            self.heart_turtle.pendown()
            self.heart_turtle.color("#f73487")
            self.heart_turtle.width(3)

            # Heart shape equations
            def heart_x(t):
                return 15 * math.sin(t) ** 3

            def heart_y(t):
                return 12 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

            # Scaling
            scale_factor = 10
            self.heart_turtle.penup()
            for i in range(0, 360, 2):
                t = math.radians(i)
                x = heart_x(t) * scale_factor
                y = heart_y(t) * scale_factor
                self.heart_turtle.goto(x, y)
                self.heart_turtle.pendown()

            # Show love percentage
            time.sleep(1)  # Simulate processing time
            love_percentage = random.randint(1, 100)
            result_text = f"Your Love Percentage: {love_percentage}%"
            self.result_label.config(text=result_text)

            self.calculate_button.config(state="normal")
        else:
            self.result_label.config(text="Please Enter Both Names!")

# Create Tkinter window
window = tk.Tk()
app = Love_Calculator_app(window)
window.mainloop()
