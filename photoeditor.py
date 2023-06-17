from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

root = Tk()
root.title("Photo Editor App")
root.geometry("640x640")

def load_image():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1

def apply_blur(event):
    global img_path, img1, img_blur
    for m in range(0, v1.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img_blur = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(img_blur)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1

def apply_brightness(event):
    global img_path, img1, img_brightness
    for m in range(0, v2.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img_brightness = ImageEnhance.Brightness(img).enhance(m)
        img1 = ImageTk.PhotoImage(img_brightness)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1

img1 = None
img_blur = None
img_brightness = None

def save_image():
    global img_path, img1, img_blur, img_brightness
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[
        ("All Files", "*.*"), ("PNG file", "*.png"), ("JPEG file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            img_blur.save(file)
        elif canvas2.image == img_blur:
            img_blur.save(file)
        elif canvas2.image == img_brightness:
            img_brightness.save(file)

blur_label = Label(root, text="Blur:", font=("Arial", 17, "bold"), width=9, anchor="e")
blur_label.place(x=15, y=8)
v1 = IntVar()
blur_scale = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=apply_blur)
blur_scale.place(x=150, y=10)

brightness_label = Label(root, text="Brightness:", font=("Arial", 17, "bold"))
brightness_label.place(x=8, y=50)
v2 = IntVar()
brightness_scale = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=apply_brightness)
brightness_scale.place(x=150, y=55)

canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

select_btn = Button(root, text="Select Image", bg="black", fg="gold",
                    font=("Arial", 15, "bold"), relief=GROOVE, command=load_image)
select_btn.place(x=100, y=595)

save_btn = Button(root, text="Save", width=12, bg="black", fg="gold",
                    font=("Arial", 15, "bold"), relief=GROOVE, command=save_image)
save_btn.place(x=280, y=595)

exit_btn = Button(root, text="Exit", width=12, bg="black", fg="gold",
                    font=("Arial", 15, "bold"), relief=GROOVE, command=root.destroy)
exit_btn.place(x=460, y=595)

root.mainloop()
