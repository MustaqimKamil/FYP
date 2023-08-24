from tkinter import *
import mysql.connector
from login_page import uid
import textwrap
import re

global uid
uid = uid()

def open_dashboard():
    window.destroy()
    import user_dashboard

def open_predict():
    window.destroy()
    import user_predict_page

def open_report():
    window.destroy()
    import user_report_page

def open_profile():
    pass

def logout():
    window.destroy()

def delete_acc():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    abb = "DELETE FROM userinfo WHERE user_id = %s"
    cursor.execute(abb, (uid,))
    conn.commit()

    acc = "DELETE FROM userinput WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    conn.commit()

    cursor.close()
    conn.close()
    window.destroy()
    import user_dashboard

def delete():
    root1 = Tk()
    root1.geometry("250x100+650+250")
    root1.title("Message Box")

    label = Label(root1, text="Are you sure you wanted to delete?", fg="red")
    label.pack()

    button_frame = Frame(root1)
    button_frame.pack(side=BOTTOM)

    confirm_button = Button(button_frame, text="Confirm", command=delete_acc)
    confirm_button.pack(side=LEFT, padx=5)

    cancel_button = Button(button_frame, text="Cancel", command=root1.destroy)
    cancel_button.pack(side=LEFT, padx=5)

    root1.resizable(False, False)
    root1.mainloop()

def cancel_update():
    root.destroy()
    global window
    window = Tk()
    close_sidebar()

def retry():
    root1.destroy()

def update_data():
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
        global root1

        root1 = Tk()
        root1.geometry("250x100+650+250")
        root1.title("Error")

        label = Label(root1, text=text, fg="red")
        label.pack()

        button = Button(root1, text="Ok", command=retry)
        button.pack()

        root1.resizable(False, False)
        root1.mainloop()

    if updUsername.get() == "" or updPassword.get() == "" or updfullname.get() == "" or updAge.get() == "" or \
            updEmail.get() == "" or updPhNumber.get() == "" or updStreet.get() == "" or city.get() == city_set or \
            updZipcode.get() == "" or state.get() == state_set:
        text="Please fill in the blanks"
        errorBox(text)

    elif not validate_username(updUsername.get()):
        text = "Your username must more than 5 charachter and include alphabet or number only"
        wrapped_text= textwrap.fill(text, width=40)
        errorBox(wrapped_text)

    elif not validate_password(updPassword.get()):
        text = "Your password must more than 8 charachter and include uppercase, symbol and number"
        wrapped_text = textwrap.fill(text, width=40)
        errorBox(wrapped_text)

    elif not validate_age(updAge.get()):
        text = "Please insert valid age"
        errorBox(text)

    elif "@" not in updEmail.get():
        text="Please insert valid email"
        errorBox(text)

    elif not validate_phone_number(updPhNumber.get()):
        text = "Please insert valid phone number"
        errorBox(text)

    elif not validate_zipcode(updZipcode.get()):
        text = "Please insert valid zipcode"
        errorBox(text)


    else:
        conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
        cursor = conn.cursor()

        upd = "UPDATE userinfo SET username = %s, password = %s, fullname = %s, age = %s, email = %s, phone_number = %s, " \
              "street = %s, city = %s, zipcode = %s, state = %s WHERE user_id = %s"

        value = (
            updUsername.get(), updPassword.get(), updfullname.get().upper(), updAge.get(), updEmail.get(), updPhNumber.get(),
            updStreet.get().upper(), city.get(), updZipcode.get(), state.get(), uid)

        cursor.execute(upd, value)

        # Commit the changes to the database
        conn.commit()

        cursor.close()
        conn.close()

        root.destroy()
        global window
        window = Tk()
        close_sidebar()

def update():

    window.destroy()
    global root, updUsername, updPassword, updfullname, updAge, updEmail, updPhNumber, updStreet, city, updZipcode,\
        state, city_set, state_set, entry7

    root = Tk()

    root.geometry("1140x700")
    root.configure(bg="#ffffff")
    canvas = Canvas(
        root,
        bg="#ffffff",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"update_acc_bg.png")
    background = canvas.create_image(
        570.5, 371.5,
        image=background_img)

    #username
    entry0_img = PhotoImage(file=f"border_tb_long.png")
    entry0_bg = canvas.create_image(
        662.5, 208.0,
        image=entry0_img)

    updUsername = StringVar()
    updPassword = StringVar()
    updfullname = StringVar()
    updAge = StringVar()
    updEmail = StringVar()
    updPhNumber = StringVar()
    updStreet = StringVar()
    city = StringVar()
    updZipcode = StringVar()
    state = StringVar()

    entry0 = Entry(
        textvariable=updUsername,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry0.place(
        x=350.0, y=193,
        width=625.0,
        height=28)

    #password
    entry1_img = PhotoImage(file=f"border_tb_long.png")
    entry1_bg = canvas.create_image(
        662.5, 256.0,
        image=entry1_img)

    entry1 = Entry(
        textvariable=updPassword,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry1.place(
        x=350.0, y=241,
        width=625.0,
        height=28)

    #fullname
    entry2_img = PhotoImage(file=f"border_tb_long.png")
    entry2_bg = canvas.create_image(
        662.5, 303.0,
        image=entry2_img)

    entry2 = Entry(
        textvariable=updfullname,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry2.place(
        x=350.0, y=288,
        width=625.0,
        height=28)

    #age
    entry3_img = PhotoImage(file=f"border_tb_long.png")
    entry3_bg = canvas.create_image(
        662.5, 350.0,
        image=entry3_img)

    entry3 = Entry(
        textvariable=updAge,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry3.place(
        x=350.0, y=335,
        width=625.0,
        height=28)

    #email
    entry4_img = PhotoImage(file=f"border_tb_long.png")
    entry4_bg = canvas.create_image(
        662.5, 397.0,
        image=entry4_img)

    entry4 = Entry(
        textvariable=updEmail,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry4.place(
        x=350.0, y=382,
        width=625.0,
        height=28)

    #phone number
    entry5_img = PhotoImage(file=f"border_tb_long.png")
    entry5_bg = canvas.create_image(
        662.5, 444.0,
        image=entry5_img)

    entry5 = Entry(
        textvariable=updPhNumber,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry5.place(
        x=350.0, y=429,
        width=625.0,
        height=28)

    #street
    entry6_img = PhotoImage(file=f"border_tb_long.png")
    entry6_bg = canvas.create_image(
        662.5, 491.0,
        image=entry6_img)

    entry6 = Entry(
        textvariable=updStreet,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry6.place(
        x=350.0, y=476,
        width=625.0,
        height=28)

    #zipcode
    entry8_img = PhotoImage(file=f"border_tb_short.png")
    entry8_bg = canvas.create_image(
        645.0, 538.0,
        image=entry8_img)

    entry8 = Entry(
        textvariable=updZipcode,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry8.place(
        x=570.0, y=523,
        width=150.0,
        height=28)

    city_set = "Select a city"
    state_set = "Select a state"
    # state
    entry9_img = PhotoImage(file=f"border_tb_short.png")
    entry9_bg = canvas.create_image(
        900.0, 538.0,
        image=entry9_img)

    def get_selected_value(event):
        global entry7
        if state.get() == "JOHOR":
            entry7.destroy()
            city.set(city_set)
            city_option = ["PASIR GUDANG", "JOHOR BAHRU"]
            city_option = sorted(city_option)

            entry7 = OptionMenu(
                root,
                city,
                *city_option)

            entry7.place(
                x=290.0, y=523,
                width=150.0,
                height=28)

        elif state.get() == "MELAKA":
            entry7.destroy()
            city.set(city_set)
            city_option = ["KOTA HILIR", "MASJID TANAH"]
            city_option = sorted(city_option)

            entry7 = OptionMenu(
                root,
                city,
                *city_option)

            entry7.place(
                x=290.0, y=523,
                width=150.0,
                height=28)

    state.set(state_set)
    state_option = ["JOHOR", "MELAKA"]
    state_option = sorted(state_option)

    entry9 = OptionMenu(
        root,
        state,
        *state_option,
        command=get_selected_value)

    entry9.place(
        x=825.0, y=523,
        width=150.0,
        height=28)

    # city
    entry7_img = PhotoImage(file=f"border_tb_short.png")
    entry7_bg = canvas.create_image(
        365.0, 538.0,
        image=entry7_img)

    city.set(city_set)
    city_option = ["PASIR GUDANG", "JOHOR BAHRU"]
    city_option = sorted(city_option)

    entry7 = OptionMenu(
        root,
        city,
        *city_option,)

    entry7.place(
        x=290.0, y=523,
        width=150.0,
        height=28)


    img0 = PhotoImage(file=f"update_button_update_acc.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=update_data,
        relief="flat")

    b0.place(
        x=445, y=590,
        width=105,
        height=34)

    img1 = PhotoImage(file=f"cancel_button_update_acc.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=cancel_update,
        relief="flat")

    b1.place(
        x=589, y=590,
        width=105,
        height=34)

    root.resizable(False, False)
    root.mainloop()

def close_sidebar():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT username, password, email, phone_number, street, city, zipcode, state from userinfo WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    for row in result:
        username, password, email, phone_number, street, city, zipcode, state = row
        zipcode = str(zipcode)

    window.geometry("1140x700")
    window.configure(bg="#66589d")
    canvas = Canvas(
        window,
        bg="#66589d",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"sidebar_close.png")
    sidebar_close = canvas.create_image(
        51.0, 350.0,
        image=background_img)

    img0 = PhotoImage(file=f"profile_sidebar_close.png")
    profile_sidebar_close_button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_profile,
        relief="flat")

    profile_sidebar_close_button.place(
        x=10, y=285,
        width=92,
        height=48)

    img1 = PhotoImage(file=f"report_sidebar_close.png")
    report_sidebar_close_button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    report_sidebar_close_button.place(
        x=10, y=237,
        width=92,
        height=48)

    img2 = PhotoImage(file=f"predict_sidebar_close.png")
    predict_sidebar_close_button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    predict_sidebar_close_button.place(
        x=10, y=189,
        width=92,
        height=48)

    img3 = PhotoImage(file=f"dashboard_sidebar_close.png")
    dashboard_sidebar_close_button = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    dashboard_sidebar_close_button.place(
        x=10, y=141,
        width=92,
        height=48)

    img4 = PhotoImage(file=f"arrow_sidebar_close.png")
    arrow_sidebar_close_button = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=open_sidebar,
        relief="flat")

    arrow_sidebar_close_button.place(
        x=40, y=27,
        width=31,
        height=31)

    user_profile_bg = PhotoImage(file=f"user_profile_bg.png")
    background = canvas.create_image(
        647.5, 315.5,
        image=user_profile_bg)

    update_button_profile = PhotoImage(file=f"update_button_profile.png")
    buttonUpdate = Button(
        image=update_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=update,
        relief="flat")

    buttonUpdate.place(
        x=414, y=526,
        width=78,
        height=31)

    delete_button_profile = PhotoImage(file=f"delete_button_profile.png")
    buttonDelete = Button(
        image=delete_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=delete,
        relief="flat")

    buttonDelete.place(
        x=549, y=526,
        width=78,
        height=31)

    dashboard_button_profile = PhotoImage(file=f"dashboard_button_profile.png")
    buttonDashboard = Button(
        image=dashboard_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    buttonDashboard.place(
        x=872, y=307,
        width=118,
        height=31)

    predict_button_profile = PhotoImage(file=f"predict_button_profile.png")
    buttonPredict = Button(
        image=predict_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    buttonPredict.place(
        x=872, y=347,
        width=118,
        height=31)

    report_button_profile = PhotoImage(file=f"report_button_profile.png")
    buttonReport = Button(
        image=report_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    buttonReport.place(
        x=872, y=388,
        width=118,
        height=31)

    logout_button_profile = PhotoImage(file=f"logout_button_profile.png")
    buttonLogout = Button(
        image=logout_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=logout,
        relief="flat")

    buttonLogout.place(
        x=892, y=526,
        width=78,
        height=31)

    # x = -57, y = +2.5
    canvas.create_text(
        348.5, 223,
        text=username,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        351.5, 261,
        text=password,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        312, 299,
        text=email,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        391.0, 337,
        text=phone_number,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    address = street + ", " + zipcode + ", " + city + ", " + state
    wrapped_text1 = textwrap.fill(address, width=50)
    canvas.create_text(
        390, 375,
        text=wrapped_text1,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()

def open_sidebar():
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT username, password, email, phone_number, street, city, zipcode, state from userinfo WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    for row in result:
        username, password, email, phone_number, street, city, zipcode, state = row
        zipcode = str(zipcode)

    window.geometry("1140x700")
    window.configure(bg="#66589d")
    canvas = Canvas(
        window,
        bg="#66589d",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    user_profile_bg = PhotoImage(file=f"user_profile_bg.png")
    background = canvas.create_image(
        647.5, 315.5,
        image=user_profile_bg)

    update_button_profile = PhotoImage(file=f"update_button_profile.png")
    buttonUpdate = Button(
        image=update_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=update,
        relief="flat")

    buttonUpdate.place(
        x=414, y=526,
        width=78,
        height=31)

    delete_button_profile = PhotoImage(file=f"delete_button_profile.png")
    buttonDelete = Button(
        image=delete_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=delete,
        relief="flat")

    buttonDelete.place(
        x=549, y=526,
        width=78,
        height=31)

    dashboard_button_profile = PhotoImage(file=f"dashboard_button_profile.png")
    buttonDashboard = Button(
        image=dashboard_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    buttonDashboard.place(
        x=872, y=307,
        width=118,
        height=31)

    predict_button_profile = PhotoImage(file=f"predict_button_profile.png")
    buttonPredict = Button(
        image=predict_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    buttonPredict.place(
        x=872, y=347,
        width=118,
        height=31)

    report_button_profile = PhotoImage(file=f"report_button_profile.png")
    buttonReport = Button(
        image=report_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    buttonReport.place(
        x=872, y=388,
        width=118,
        height=31)

    logout_button_profile = PhotoImage(file=f"logout_button_profile.png")
    buttonLogout = Button(
        image=logout_button_profile,
        borderwidth=0,
        highlightthickness=0,
        command=logout,
        relief="flat")

    buttonLogout.place(
        x=892, y=526,
        width=78,
        height=31)

    # x = -57, y = +2.5
    canvas.create_text(
        348.5, 223,
        text=username,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        351.5, 261,
        text=password,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        312, 299,
        text=email,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    canvas.create_text(
        391.0, 337,
        text=phone_number,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    address = street + ", " + zipcode + ", " + city + ", " + state
    wrapped_text1 = textwrap.fill(address, width=50)
    canvas.create_text(
        390, 375,
        text=wrapped_text1,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    background_img = PhotoImage(file=f"sidebar_open.png")
    sidebar_close = canvas.create_image(
        127.0, 350.0,
        image=background_img)

    img0 = PhotoImage(file=f"profile_sidebar_open.png")
    profile_sidebar_close_button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_profile,
        relief="flat")

    profile_sidebar_close_button.place(
        x=10, y=285,
        width=244,
        height=48)

    img1 = PhotoImage(file=f"report_sidebar_open.png")
    report_sidebar_close_button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    report_sidebar_close_button.place(
        x=10, y=237,
        width=244,
        height=48)

    img2 = PhotoImage(file=f"prediction_sidebar_open.png")
    predict_sidebar_close_button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    predict_sidebar_close_button.place(
        x=10, y=189,
        width=244,
        height=48)

    img3 = PhotoImage(file=f"dashboard_sidebar_open.png")
    dashboard_sidebar_close_button = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    dashboard_sidebar_close_button.place(
        x=10, y=141,
        width=244,
        height=48)

    img4 = PhotoImage(file=f"arrow_sidebar_open.png")
    arrow_sidebar_close_button = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=close_sidebar,
        relief="flat")

    arrow_sidebar_close_button.place(
        x=212, y=30,
        width=31,
        height=31)

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()

window = Tk()

close_sidebar()