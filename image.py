#!/usr/bin/python3


# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
gui = Tk()

# Define the geometry of the window
gui.configure(background='grey')
gui.title("Velocity Bus")
gui.geometry("800x480")
gui.resizable(width=False, height=False)

# # Setup for the Velocity Image
# frame = Frame(gui, width=745, height=475)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("VelocityTopView.jpg"))

# # Create a Label Widget to display the Image
# label = Label(frame, image = img)
# label.pack()

# Create the canvas, size in pixels.
canvas = Canvas(width=800, height=480)

# Pack the canvas into the Frame.
canvas.pack(anchor= CENTER)

# Load the Aircraft image file.
VelocityTopView = ImageTk.PhotoImage(file='VelocityTopView.jpg')

# Put image on canvas.
canvas.create_image(400, 240, image=VelocityTopView)

leftLightColor = 'white'
rightLightColor = 'white'
canvas.create_oval(30, 400, 40, 475, fill=leftLightColor)
canvas.create_oval(765, 400, 775, 475, fill=rightLightColor)

# Strings for variable data
batteryVoltageString = "Battery 12.5v"
canvas.create_text(50,50, text=batteryVoltageString)



gui.mainloop()