from tkinter import *
from photoeditor import *
from interface import *


def staff():

    def submitt():
        pname = uia.get()
        m1 = ma.get()
        m2 = mar.get()
        m3 = marks.get()
        avg = (int(m1)+int(m2)+int(m3))
        labe = Label(window, text="Patient's name "+pname,
                     font="Arial").place(x=500, y=750)
        lab = Label(window, text="The Total amount is " +
                    str(avg), font="Arial").place(x=500, y=750)

    window = Tk()
    window.geometry('800x800')
    window.title("Patient details")

    l = Label(window, text="Fill up the following details",
              font="Arial").place(x=300, y=10)

    user_name = Label(window, text="Patient's Name",
                      font="Arial").place(x=500, y=55)
    uia = Entry(window)
    uia.place(x=300, y=60)

    sub = Label(window, text="Select the Gender",
                font="Arial").place(x=110, y=140)
    var = StringVar()
    R1 = Radiobutton(window, text="Male", variable=var,
                     value="Male", font="Arial")
    R1.place(x=300, y=100)
    R2 = Radiobutton(window, text="Female", variable=var,
                     value="Female", font="Arial")
    R2.place(x=300, y=140)
    R3 = Radiobutton(window, text="OTHERS", variable=var,
                     value="OTHERS", font="Arial")
    R3.place(x=300, y=180)

    sub = Label(window, text="Select the \n Consulted Doctor",
                font="Arial").place(x=80, y=260)
    listbox = Listbox(window, height=4, width=20, font="Helvetica")
    listbox.insert(1, "Dr. Arpit Sharma")
    listbox.insert(2, "Dr. Kanishka Kathait")
    listbox.insert(3, "Dr. Mitali Chaudhary")
    listbox.insert(4, "Dr. Vrinda Kumar")
    listbox.place(x=300, y=230)

    sub = Label(window, text="Enter FEES of consultation",
                font="Arial").place(x=200, y=350)
    l1 = Label(window, text="consultation Fee").place(x=540, y=390)
    l2 = Label(window, text="Medication fee").place(x=540, y=430)
    l3 = Label(window, text="Medical reports'fee").place(x=540, y=470)
    ma = Entry(window)
    ma.place(x=300, y=390)
    mar = Entry(window)
    mar.place(x=300, y=430)
    marks = Entry(window)
    marks.place(x=300, y=470)
    button = Button(window, text='Submit details', bd=10, width=25,
                    bg="black", fg="teal", command=submitt).place(x=300, y=600)

    window.mainloop()


try:
    ch = int(input("Enter Designation : 1. Staff \n 2. Doctor \n 3. Patient \n 4.Exit  "))
    # print("1.")
    if (ch == 1):
        staff()
    if (ch == 2):
        print("Select one of the options:")
        op = int(input("1. Report viewer/Xray Viewer \n 2. Report editor\n "))
        try:
            if (op == 1):
                from photoviewer import *
            if(op==2):
                from photoeditor import *
            else:
                print("TRY AGAIN!!!!!")
        except:
            print("TRY AGAIN!! WRONG OPTION!")
                
     # doctor()
    if (ch == 3):
        print("DISPLAYING REPORT::::")
        from photoviewer import *
        # image viewer function
    if(ch==4):
        exit(0)
    else:
        print("TRY AGAIN")
except ValueError:
    print("LOGIN FAILED!!")
