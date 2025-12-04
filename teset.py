from customtkinter import *
from playsound import playsound
import threading
from tkinter import filedialog
import qrcode
from tkinter import messagebox


def play_music():
    while True:
        playsound("c418_aria_math.mp3", block=True)

# Start the thread properly
threading.Thread(target=play_music, daemon=True).start()
def gen():
    link = str(entry.get().strip())
    qr = qrcode.QRCode()
    qr.add_data(link)
    img = qr.make_image()
    img.save(filepath)
    messagebox.showinfo(title="Generation successful", message=f"The QR code is on this path: {filepath}")
def pathy():
    global filepath
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files","*.png"), ("All files", "*.*")]
    )
   
set_appearance_mode("dark")
set_default_color_theme("blue")

win = CTk()
win.title("Qr code maker")
win.geometry("800x800")
win.configure(fg_color="#00FF00")  # hex color
welcome = CTkLabel(win, text="Welcome", font=("Arial", 35), text_color="purple")
welcome.grid(column=1,row=0,columnspan=2)
label = CTkLabel(win, text="Enter link: ", font=("Arial", 35), text_color="blue")
label.grid(column =1, row=2)
entry = CTkEntry(win, font=("impact",30))
entry.grid(column=2,row=2)
CTkButton(win,command=pathy ,hover_color="firebrick" ,text="Choose path to store", font=("consolas",30), text_color="#00ff00",fg_color="black").grid(column=1,row=3)
CTkButton(win,command=gen ,hover_color="maroon" ,text="Generate", font=("consolas",30), text_color="#00ff00",fg_color="black").grid(column=1,row=4)
win.mainloop()
