import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def returned_press(event):
    print("Returned press")

def log(event):
    print(event)

app = tk.Tk()
app.title("Disgustingly Good")
window_w = 600
window_h = 400
screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()
app.geometry(f"{window_w}x{window_h}+{(screen_w - window_w) // 2}+{(screen_h - window_h) // 2}")

message = ttk.Label(app, text="Hello world!")
message.pack()

image = Image.open("./assets/OIP.png")
image = ImageTk.PhotoImage(image)
image_label = ttk.Label(app, image=image, padding=10)
image_label.pack()

button = ttk.Button(app, text="Save me")
button.bind("<Return>", returned_press)
button.bind("<Return>", log, add="+")
button.focus()
button.pack(expand=True)

app.mainloop()