import mysql.connector
from tkinter import *

def proceed():
    root.destroy()
    window.destroy()
    import mo_report

def retry():
    root.destroy()

def login():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT username, password from moinfo"
    cursor.execute(acc)
    result = cursor.fetchall()

    match_found = False

    for row in result:
        if (username.get() == row[0]) and (password.get() == row[1]):

            def disable_event():
                pass

            global root
            # message box
            root = Tk()
            root.geometry("250x100+650+250")
            root.title("Message Box")
            root.focus_set()

            label = Label(root, text="Log in successfully!", fg="green")
            label.pack()

            button = Button(root, text="Continue", command=proceed)
            button.pack()

            root.resizable(False, False)
            root.protocol("WM_DELETE_WINDOW", disable_event)
            root.mainloop()

            match_found = True
            break

    if not match_found:
        root = Tk()
        root.geometry("250x100+650+250")
        root.title("Warning")

        label = Label(root, text="Log in unsuccessfully!", fg="red")
        label.pack()

        button = Button(root, text="Retry", command=retry)
        button.pack()

        root.resizable(False, False)
        root.mainloop()

    cursor.close()
    conn.close()


window = Tk()

window.geometry("1140x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1140,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"mo_login_bg.png")
background = canvas.create_image(
    609.0, 294.5,
    image=background_img)

img0 = PhotoImage(file = f"mo_login_button.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 314, y = 585,
    width = 100,
    height = 35)

username = StringVar()
password = StringVar()

entry0_img = PhotoImage(file = f"mo_username.png")
entry0_bg = canvas.create_image(
    366.5, 406.0,
    image = entry0_img)

entry0 = Entry(
    textvariable=username,
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 102, y = 390,
    width = 529,
    height = 30)

entry1_img = PhotoImage(file = f"mo_password.png")
entry1_bg = canvas.create_image(
    366.5, 492.0,
    image = entry1_img)

entry1 = Entry(
    textvariable=password,
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 102, y = 476,
    width = 529,
    height = 30)

window.resizable(False, False)
window.mainloop()