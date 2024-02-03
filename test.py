from tkinter import *

root = Tk()
root.title("File")
root.minsize(200, 200)  # width, height
root.geometry("500x500+50+50")

# Create Label in our window
image = PhotoImage(file="caption.gif")
img = Label(root, image=image)
img.pack()
root.mainloop()
