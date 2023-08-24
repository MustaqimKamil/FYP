import mysql.connector
from tkinter import *

def uid():
    global user_id
    return user_id

def proceed():
    root.destroy()
    window.destroy()
    uid()
    import user_dashboard

def retry():
    root.destroy()

def login():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT user_id, username, password from userinfo"
    cursor.execute(acc)
    result = cursor.fetchall()

    match_found = False

    for row in result:
        if (username.get() == row[1]) and (password.get() == row[2]):
            global user_id
            user_id = row[0]

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

def signup():
    window.destroy()
    import sign_up

window = Tk()

window.geometry("1140x700+200+50")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=700,
    width=1140,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

username = StringVar()
password = StringVar()

background_img = PhotoImage(file=f"background_login.png")
background = canvas.create_image(
    252.5, 510.0,
    image=background_img)

# login button
img0 = PhotoImage(file=f"login_button_login.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat")

b0.place(
    x=744, y=477,
    width=100,
    height=33)

# sign up link
img1 = PhotoImage(file=f"signup_button_login.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=signup,
    relief="flat")

b1.place(
    x=829, y=523,
    width=43,
    height=18)

# username text field
entry0_img = PhotoImage(file=f"username_login.png")
entry0_bg = canvas.create_image(
    794.0, 353.5,
    image=entry0_img)

entry0 = Entry(
    textvariable=username,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=580.0, y=340,
    width=428.0,
    height=25)

# password text field
entry1_img = PhotoImage(file=f"password_login.png")
entry1_bg = canvas.create_image(
    794.0, 435.5,
    image=entry1_img)

entry1 = Entry(
    show="*",
    textvariable=password,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry1.place(
    x=580.0, y=422,
    width=428.0,
    height=25)

window.resizable(False, False)
window.mainloop()