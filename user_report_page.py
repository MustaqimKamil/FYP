from tkinter import *
import mysql.connector
import textwrap
from login_page import uid

global uid
uid = uid()


def open_dashboard():
    window.destroy()

def open_predict():
    window.destroy()

def open_report():
    pass

def open_profile():
    window.destroy()
    import user_profile_page

def done():
    root.destroy()
    global window
    window = Tk()
    close_sidebar()

def openR(session_id):
    window.destroy()
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT fullname, age, date, med_condition, vaccine_stats, cov_symptom, cov_period, result from userinput WHERE session_id = %s"
    cursor.execute(acc, (session_id,))
    result1 = cursor.fetchall()

    for row in result1:
        fullname, age, date, med_condition, vaccine_stats, cov_symptom, cov_period, result = row
        date_formatted = date.strftime("%d %B %Y")

    abb = "SELECT email, phone_number, street, city, zipcode, state from userinfo WHERE user_id = %s"
    cursor.execute(abb, (uid,))
    result2 = cursor.fetchall()

    for row in result2:
        email, phone_number, street, city, zipcode, state = row
        zipcode = str(zipcode)

    global root
    root = Tk()
    root.geometry("792x837")
    root.configure(bg="#ffffff")
    canvas = Canvas(
        root,
        bg="#ffffff",
        height=837,
        width=792,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    report_form_bg = PhotoImage(file=f"report_form_background.png")
    reportBg = canvas.create_image(
        396.0, 418.5,
        image=report_form_bg)

    if result == "No symptoms or complications":
        lowRiskBorder = PhotoImage(file=f"low_risk_border.png")
        border = canvas.create_image(
            395.5, 608.0,
            image=lowRiskBorder)

        canvas.create_text(
            395.5, 602.5,
            text="LOW RISK",
            fill="#1dd100",
            font=("Nunito-Bold", int(25.0)))

        canvas.create_text(
            389.0, 706.5,
            text=result,
            fill="#000000",
            font=("Nunito-Bold", int(11.5)))

        canvas.create_text(
            389.0, 767.5,
            text="Congratulation! Thank you for your prediction session with us.",
            fill="#000000",
            font=("Nunito-Medium", int(11.5)))

    else:
        highRiskBorder = PhotoImage(file=f"high_risk_border.png")
        border = canvas.create_image(
            395.5, 608.0,
            image=highRiskBorder)

        canvas.create_text(
            395.5, 602.5,
            text="HIGH RISK",
            fill="#d01919",
            font=("Nunito-Bold", int(25.0)))

        text = result
        wrapped_text = textwrap.fill(text, width=100)
        canvas.create_text(
            389.0, 708.5,
            text=wrapped_text,
            fill="#d01919",
            font=("Nunito-Bold", int(11.5)))

        canvas.create_text(
            389.0, 767.5,
            text="Please consult to your nearest medical expert for further inspection.",
            fill="#000000",
            font=("Nunito-Medium", int(11.5)))


    canvas.create_text(
        389.0, 677.5,
        text="to have the following complications:",
        fill="#000000",
        font=("Nunito-Bold", int(11.5)))

    canvas.create_text(
        390.0, 524.5,
        text="Based on your data, you have",
        fill="#000000",
        font=("Nunito-Bold", int(11.5)))

    ok_button = PhotoImage(file=f"OK_button.png")
    ok_button_0 = Button(
        image=ok_button,
        borderwidth=0,
        highlightthickness=0,
        command=done,
        relief="flat")

    ok_button_0.place(
        x=365, y=791,
        width=61,
        height=30)

    # -155
    canvas.create_text(
        40.0, 211.0,
        text=street + ", " + zipcode + ", " + city + ", " + state,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # -114
    canvas.create_text(
        555.0, 158.0,
        text=date_formatted,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # -124
    canvas.create_text(
        100.5, 158.0,
        text=email,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # -7
    canvas.create_text(
        41, 158.0,
        text=age,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # - 9
    canvas.create_text(
        615, 105.0,
        text=phone_number,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # -7
    canvas.create_text(
        40.0, 105.0,
        text=fullname,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # -111
    canvas.create_text(
        289.0, 45.0,
        text="REPORT ID: " + str(session_id),
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # x = -54
    canvas.create_text(
        194.0, 265.0,
        text=vaccine_stats,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # x = -54
    canvas.create_text(
        239.0, 296.0,
        text=cov_period,
        fill="#000000",
        font=("Nunito-Medium", int(11.5)),
        anchor="w")

    # x = -15, y = -6
    text1 = med_condition
    wrapped_text1 = textwrap.fill(text1, width=80)
    canvas.create_text(
        193.0, 318.0,
        text=wrapped_text1,
        fill="#ff0000",
        font=("Nunito-Medium", int(11.5)),
        anchor="nw"  # align text to the top-left corner of the bounding box
    )

    # x = -18, y = -6
    text2 = cov_symptom
    wrapped_text2 = textwrap.fill(text2, width=80)
    canvas.create_text(
        190.0, 402.0,
        text=wrapped_text2,
        fill="#ff0000",
        font=("Nunito-Medium", int(11.5)),
        anchor="nw"  # align text to the top-left corner of the bounding box
    )

    cursor.close()
    conn.close()

    root.resizable(False, False)
    root.mainloop()

def deleteTable(canvas, t, i, n, d, delB, opnR, session_id):
    canvas.delete(t)
    tablewidgets.remove(t)
    canvas.delete(i)
    idwidgets.remove(i)
    canvas.delete(n)
    namewidgets.remove(n)
    canvas.delete(d)
    datewidgets.remove(d)
    delB.destroy()
    deletewidgets.remove(delB)
    opnR.destroy()
    openrwidgets.remove(opnR)

    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    deleteSession = "DELETE FROM userinput WHERE session_id = %s"
    cursor.execute(deleteSession, (session_id,))
    conn.commit()

    cursor.close()
    conn.close()

def close_sidebar():
    global y_1, y_2, y_3, img5, img6, tablewidgets, idwidgets, namewidgets, openrwidgets, deletewidgets, datewidgets, window

    window.geometry("1140x700")
    window.configure(bg="#626fe7")
    canvas = Canvas(
        window,
        bg="#626fe7",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    header_img = PhotoImage(file=f"report_page_header.png")
    background = canvas.create_image(
        623.5, 78.5,
        image=header_img)

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


    img5 = PhotoImage(file=f"delete_button_report.png")
    img6 = PhotoImage(file=f"open_report_button.png")
    table = PhotoImage(file=f"table.png")
    y_1 = 155.5
    y_2 = 156.0
    y_3 = 146.0

    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT session_id, fullname, date from userinput WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    tablewidgets = []
    idwidgets = []
    namewidgets = []
    datewidgets = []
    openrwidgets = []
    deletewidgets = []

    for row in result:
        session_id, fullname, date = row
        date_formatted = date.strftime("%B %d, %Y %H:%M")

        table_img = canvas.create_image(
            623.5, y_1,
            image=table)
        tablewidgets.append(table_img)
        y_1 += 40

        id = canvas.create_text(
            156.5, y_2,
            text=session_id,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        idwidgets.append(id)

        name = canvas.create_text(
            480.0, y_2,
            text=fullname,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        namewidgets.append(name)

        date = canvas.create_text(
            865.0, y_2,
            text=date_formatted,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        datewidgets.append(date)
        y_2 += 40

        openRButton = Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda session_id=session_id: openR(session_id),
            relief="flat")

        openRButton.place(
            x=957, y=y_3,
            width=117,
            height=21)
        openrwidgets.append(openRButton)

        delButton = Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        delButton.config(command=lambda t=table_img, i=id, n=name, d=date, delB=delButton, opnR=openRButton, session_id=session_id: deleteTable(canvas, t, i, n, d, delB, opnR, session_id))

        delButton.place(
            x=1090, y=y_3,
            width=13,
            height=18)
        deletewidgets.append(delButton)
        y_3 += 40

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()

def open_sidebar():
    global y_1, y_2, y_3, img5, img6, tablewidgets, idwidgets, namewidgets, openrwidgets, deletewidgets, datewidgets, window

    window.geometry("1140x700")
    window.configure(bg="#626fe7")
    canvas = Canvas(
        window,
        bg="#626fe7",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    header_img = PhotoImage(file=f"report_page_header.png")
    header = canvas.create_image(
        623.5, 78.5,
        image=header_img)

    background_img = PhotoImage(file=f"sidebar_open.png")
    sidebar_open = canvas.create_image(
        127.0, 350.0,
        image=background_img)

    img0 = PhotoImage(file=f"profile_sidebar_open.png")
    profile_sidebar_open_button = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_profile,
        relief="flat")

    profile_sidebar_open_button.place(
        x=10, y=285,
        width=244,
        height=48)

    img1 = PhotoImage(file=f"report_sidebar_open.png")
    report_sidebar_open_button = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    report_sidebar_open_button.place(
        x=10, y=237,
        width=244,
        height=48)

    img2 = PhotoImage(file=f"prediction_sidebar_open.png")
    predict_sidebar_open_button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    predict_sidebar_open_button.place(
        x=10, y=189,
        width=244,
        height=48)

    img3 = PhotoImage(file=f"dashboard_sidebar_open.png")
    dashboard_sidebar_open_button = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    dashboard_sidebar_open_button.place(
        x=10, y=141,
        width=244,
        height=48)

    img4 = PhotoImage(file=f"arrow_sidebar_open.png")
    arrow_sidebar_open_button = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=close_sidebar,
        relief="flat")

    arrow_sidebar_open_button.place(
        x=212, y=30,
        width=31,
        height=31)

    img5 = PhotoImage(file=f"delete_button_report.png")
    img6 = PhotoImage(file=f"open_report_button.png")
    table = PhotoImage(file=f"table.png")
    y_1 = 155.5
    y_2 = 156.0
    y_3 = 146.0

    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT session_id, fullname, date from userinput WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    tablewidgets = []
    idwidgets = []
    namewidgets = []
    datewidgets = []
    openrwidgets = []
    deletewidgets = []

    for row in result:
        session_id, fullname, date = row
        date_formatted = date.strftime("%B %d, %Y %H:%M")

        table_img = canvas.create_image(
            623.5, y_1,
            image=table)
        tablewidgets.append(table_img)
        y_1 += 40

        id = canvas.create_text(
            156.5, y_2,
            text=session_id,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        idwidgets.append(id)

        name = canvas.create_text(
            480.0, y_2,
            text=fullname,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        namewidgets.append(name)

        date = canvas.create_text(
            865.0, y_2,
            text=date_formatted,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        datewidgets.append(date)
        y_2 += 40

        openRButton = Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda session_id=session_id: openR(session_id),
            relief="flat")

        openRButton.place(
            x=957, y=y_3,
            width=117,
            height=21)
        openrwidgets.append(openRButton)

        delButton = Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        delButton.config(command=lambda t=table_img, i=id, n=name, d=date, delB=delButton, opnR=openRButton,
                                        session_id=session_id: deleteTable(canvas, t, i, n, d, delB, opnR, session_id))

        delButton.place(
            x=1090, y=y_3,
            width=13,
            height=18)
        deletewidgets.append(delButton)
        y_3 += 40

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()

window = Tk()
close_sidebar()