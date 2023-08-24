import mysql.connector
from tkinter import *
import re
import textwrap

def retry():
    root.destroy()

def signup():

    def login_from_signup():
        root.destroy()
        window.destroy()
        import login_page

    def validate_username(username):
        if len(username) < 5:
            return False

        if re.search(r"[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", username):
            return False

        return True

    def validate_password(password):
        if len(password) < 5:
            return False

        if not re.search(r"[A-Z]", password):
            return False

        if not re.search(r"[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
            return False

        if not re.search(r"\d", password):
            return False

        return True

    def validate_age(age):
        if len(age) > 3:
            return False

        if not age.isdigit():
            return False

        return True

    def validate_phone_number(phone):
        if len(phone) < 9:
            return False

        if not phone.isdigit():
            return False

        return True

    def validate_zipcode(zipcode):
        if len(zipcode) < 5:
            return False

        if not zipcode.isdigit():
            return False

        return True

    def errorBox(text):
        global root

        root = Tk()
        root.geometry("250x100+650+250")
        root.title("Error")

        label = Label(root, text=text, fg="red")
        label.pack()

        button = Button(root, text="Ok", command=retry)
        button.pack()

        root.resizable(False, False)
        root.mainloop()

    if username.get() == "" or password.get() == "" or fullname.get() == "" or age.get() == "" or email.get() == "" or phone.get() == "" or street.get() == "" or city.get() == city_set or zipcode.get() == "" or state.get() == state_set:
        text = "Please fill in the blanks"
        errorBox(text)

    elif not validate_username(username.get()):
        text = "Your username must more than 5 charachter and include alphabet or number only"
        wrapped_text= textwrap.fill(text, width=40)
        errorBox(wrapped_text)

    elif not validate_password(password.get()):
        text = "Your password must more than 8 charachter and include uppercase, symbol and number"
        wrapped_text = textwrap.fill(text, width=40)
        errorBox(wrapped_text)

    elif not validate_age(age.get()):
        text = "Please insert valid age"
        errorBox(text)

    elif "@" not in email.get():
        text = "Please insert valid email"
        errorBox(text)

    elif not validate_phone_number(phone.get()):
        text = "Please insert valid phone number"
        errorBox(text)

    elif not validate_zipcode(zipcode.get()):
        text = "Please insert valid zipcode"
        errorBox(text)

    else:
        conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
        cursor = conn.cursor()

        check_query = "SELECT username FROM userinfo"
        cursor.execute(check_query)
        result = cursor.fetchall()

        match_found = False

        for row in result:
            if (username.get() == row[0]):
                text = "Username already exist"
                errorBox(text)

                match_found = True
                break

        if not match_found:
            insertquery = "INSERT INTO userinfo(username, password, fullname, age, email, phone_number, street, city, zipcode, state)" \
                          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value = (username.get(), password.get(), fullname.get().upper(), age.get(), email.get(), phone.get(),
                     street.get().upper(), city.get(), zipcode.get(), state.get())

            cursor.execute(insertquery, value)
            conn.commit()

            # message box
            root = Tk()
            root.geometry("250x100+650+250")
            root.title("Message Box")

            label = Label(root, text="Sign up successfully!", fg="green")
            label.pack()

            button = Button(root, text="Login", command=login_from_signup)
            button.pack()

            root.resizable(False, False)
            root.mainloop()

        cursor.close()
        conn.close()

def login():
    window.destroy()
    import login_page

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

#value
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()
email = StringVar()
phone = StringVar()
street = StringVar()
city = StringVar()
zipcode = StringVar()
state = StringVar()

# background
background_img = PhotoImage(file=f"background_signin.png")
background = canvas.create_image(
    570.0, 350.0,
    image=background_img)

# sign up button
img0 = PhotoImage(file=f"signup_button_signin.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=signup,
    relief="flat")

b0.place(
    x=730, y=510,
    width=100,
    height=38)

# log in button
img1 = PhotoImage(file=f"login_button_signin.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat")

b1.place(
    x=830, y=559,
    width=43,
    height=18)

# username
entry0_img = PhotoImage(file=f"username_signin.png")
entry0_bg = canvas.create_image(
    338.0, 346.5,
    image=entry0_img)

entry0 = Entry(
    textvariable=username,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=148.0, y=333,
    width=380.0,
    height=25)

# password
entry1_img = PhotoImage(file=f"password_signin.png")
entry1_bg = canvas.create_image(
    338.0, 405.5,
    image=entry1_img)

entry1 = Entry(
    textvariable=password,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry1.place(
    x=148.0, y=392,
    width=380.0,
    height=25)

# fullname
entry2_img = PhotoImage(file=f"fullname_signin.png")
entry2_bg = canvas.create_image(
    338.0, 464.5,
    image=entry2_img)

entry2 = Entry(
    textvariable=fullname,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry2.place(
    x=148.0, y=451,
    width=380.0,
    height=25)

# age
entry3_img = PhotoImage(file=f"age_signin.png")
entry3_bg = canvas.create_image(
    786.0, 227.5,
    image=entry3_img)

entry3 = Entry(
    textvariable=age,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry3.place(
    x=596.0, y=214,
    width=380.0,
    height=25)

# Email address
entry4_img = PhotoImage(file=f"email_signin.png")
entry4_bg = canvas.create_image(
    786.0, 286.5,
    image=entry4_img)

entry4 = Entry(
    textvariable=email,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry4.place(
    x=596.0, y=273,
    width=380.0,
    height=25)

# Phone number
entry5_img = PhotoImage(file=f"phone_number_signin.png")
entry5_bg = canvas.create_image(
    786.0, 346.5,
    image=entry5_img)

entry5 = Entry(
    textvariable=phone,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry5.place(
    x=596.0, y=333,
    width=380.0,
    height=25)

# Street
entry6_img = PhotoImage(file=f"street_signin.png")
entry6_bg = canvas.create_image(
    786.0, 405.5,
    image=entry6_img)

entry6 = Entry(
    textvariable=street,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry6.place(
    x=596.0, y=392,
    width=380.0,
    height=25)

# Zip code
entry8_img = PhotoImage(file=f"zipcode_signin.png")
entry8_bg = canvas.create_image(
    786.5, 464.5,
    image=entry8_img)

entry8 = Entry(
    textvariable=zipcode,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry8.place(
    x=757.0, y=451,
    width=59.0,
    height=25)

city_set = "Select a city"
state_set = "Select a state"

# state
entry9_img = PhotoImage(file=f"state_signin.png")
entry9_bg = canvas.create_image(
    910.0, 464.5,
    image=entry9_img)

def get_selected_value(event):
    global entry7
    if state.get() == "JOHOR":
        entry7.destroy()
        city.set(city_set)
        city_option = ["PASIR GUDANG", "JOHOR BAHRU"]
        city_option = sorted(city_option)

        entry7 = OptionMenu(
            window,
            city,
            *city_option)

        entry7.place(
            x=596.0, y=451,
            width=132.0,
            height=25)

    elif state.get() == "MELAKA":
        entry7.destroy()
        city.set(city_set)
        city_option = ["KOTA HILIR", "MASJID TANAH"]
        city_option = sorted(city_option)

        entry7 = OptionMenu(
            window,
            city,
            *city_option)

        entry7.place(
            x=596.0, y=451,
            width=132.0,
            height=25)

state.set(state_set)
state_option = ["JOHOR", "MELAKA"]
state_option = sorted(state_option)

entry9 = OptionMenu(
    window,
    state,
    *state_option,
    command=get_selected_value)

entry9.place(
    x=844.0, y=451,
    width=132.0,
    height=25)

# City
entry7_img = PhotoImage(file=f"city_signin.png")
entry7_bg = canvas.create_image(
    662.0, 464.5,
    image=entry7_img)

city.set(city_set)
city_option = ["PASIR GUDANG", "JOHOR BAHRU"]
city_option = sorted(city_option)

entry7 = OptionMenu(
    window,
    city,
    *city_option, )

entry7.place(
    x=596.0, y=451,
    width=132.0,
    height=25)

window.resizable(False, False)
window.mainloop()
