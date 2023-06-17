import tkinter as tk
from PIL import ImageTk, Image

def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = tk.Label(image=image_list[img_no-1])
    label.grid(row=1, column=0, columnspan=3)

    button_forward = tk.Button(root, text="Forward", command=lambda: forward(img_no+1))
    if img_no == 4:
        button_forward = tk.Button(root, text="Forward", state=tk.DISABLED)

    button_back = tk.Button(root, text="Back", command=lambda: back(img_no-1))
    print(img_no)

    if img_no == 1:
        button_back = tk.Button(root, text="Back", state=tk.DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = tk.Label(image=image_list[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)

    button_forward = tk.Button(root, text="Forward", command=lambda: forward(img_no + 1))
    button_back = tk.Button(root, text="Back", command=lambda: back(img_no - 1))
    print(img_no)

    if img_no == 1:
        button_back = tk.Button(root, text="Back", state=tk.DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


root = tk.Tk()
root.title("Image Viewer")
root.geometry("700x700")

image_no_1 = ImageTk.PhotoImage(Image.open("image path"))
image_no_2 = ImageTk.PhotoImage(Image.open("image path"))
image_no_3 = ImageTk.PhotoImage(Image.open("image path"))
image_no_4 = ImageTk.PhotoImage(Image.open("image path"))

image_list = [image_no_1, image_no_2, image_no_3, image_no_4]

label = tk.Label(image=image_no_1)
label.grid(row=1, column=0, columnspan=3)

button_back = tk.Button(root, text="Back", command=lambda: back(4))
button_exit = tk.Button(root, text="Exit", command=root.quit)
button_forward = tk.Button(root, text="Forward", command=lambda: forward(1))

button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()
