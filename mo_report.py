from tkinter import *
import mysql.connector
import textwrap

def btn_clicked():
    print("Button Clicked")

def done():
    root.destroy()
    global window
    window = Tk()
    start()

def logout():
    window.destroy()

def openR(user_id,session_id):

    window.destroy()
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT fullname, age, date, med_condition, vaccine_stats, cov_symptom, cov_period from userinput WHERE session_id = %s"
    cursor.execute(acc, (session_id,))
    result1 = cursor.fetchall()

    for row in result1:
        fullname, age, date, med_condition, vaccine_stats, cov_symptom, cov_period = row
        date_formatted = date.strftime("%d %B %Y")

    abb = "SELECT email, phone_number, street, city, zipcode, state from userinfo WHERE user_id = %s"
    cursor.execute(abb, (user_id,))
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

    highRiskBorder = PhotoImage(file=f"high_risk_border.png")
    border = canvas.create_image(
        395.5, 608.0,
        image=highRiskBorder)

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

    canvas.create_text(
        395.5, 602.5,
        text="HIGH RISK",
        fill="#d01919",
        font=("Nunito-Bold", int(25.0)))

    canvas.create_text(
        389.0, 767.5,
        text="Please consult to your nearest medical expert for further inspection.",
        fill="#000000",
        font=("Nunito-Medium", int(11.5)))

    canvas.create_text(
        389.0, 706.5,
        text="cough, fever, cough, fever, cough, fever, cough, fever, cough, fever ",
        fill="#000000",
        font=("Nunito-Bold", int(11.5)))

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

def deleteTable(canvas, t, uid, sid, n, a, d, delB, opnR, session_id):
    canvas.delete(t)
    tablewidgets.remove(t)
    canvas.delete(uid)
    uidwidgets.remove(uid)
    canvas.delete(sid)
    sidwidgets.remove(sid)
    canvas.delete(n)
    namewidgets.remove(n)
    canvas.delete(a)
    agewidgets.remove(a)
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

def start():
    global tablewidgets, uidwidgets, sidwidgets, namewidgets, agewidgets, datewidgets, openrwidgets, deletewidgets
    window.geometry("1140x700")
    window.configure(bg="#b97434")
    canvas = Canvas(
        window,
        bg="#b97434",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"mo_report_bg.png")
    background = canvas.create_image(
        569.0, 99.0,
        image=background_img)

    img0 = PhotoImage(file=f"mo_logout_report.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=logout,
        relief="flat")

    b0.place(
        x=1045, y=19,
        width=78,
        height=31)

    delButton = PhotoImage(file=f"mo_delete_button_report.png")
    opnReport = PhotoImage(file=f"mo_open_report_button.png")
    table = PhotoImage(file=f"mo_table_report.png")
    y_1 = 172.5
    y_2 = 163
    y_3 = 173.0

    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT user_id, session_id, fullname, age, date from userinput"
    cursor.execute(acc)
    result = cursor.fetchall()

    tablewidgets = []
    uidwidgets = []
    sidwidgets = []
    namewidgets = []
    agewidgets = []
    datewidgets = []
    openrwidgets = []
    deletewidgets = []

    for row in result:
        user_id, session_id, fullname, age, date = row
        date_formatted = date.strftime("%B %d, %Y %H:%M")

        table_img = canvas.create_image(
            569.0, y_1,
            image=table)
        tablewidgets.append(table_img)
        y_1 += 40

        uid = canvas.create_text(
            41.5, y_3,
            text=user_id,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        uidwidgets.append(uid)

        sid = canvas.create_text(
            106.5, y_3,
            text=session_id,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        sidwidgets.append(sid)

        name = canvas.create_text(
            286.0, y_3,
            text=fullname,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        namewidgets.append(name)

        a = canvas.create_text(
            758.5, y_3,
            text=age,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        agewidgets.append(a)

        date = canvas.create_text(
            880.0, y_3,
            text=date_formatted,
            fill="#000000",
            font=("Nunito-ExtraBold", int(11.5)))
        datewidgets.append(date)
        y_3 += 40

        repOpen = Button(
            image=opnReport,
            borderwidth=0,
            highlightthickness=0,
            command=lambda user_id=user_id, session_id=session_id: openR(user_id, session_id),
            relief="flat")

        repOpen.place(
            x=972, y=y_2,
            width=109,
            height=21)
        openrwidgets.append(repOpen)

        butDelete = Button(
            image=delButton,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        butDelete.config(
            command=lambda t=table_img, uid=uid, sid=sid, n=name, a=a, d=date, delB=butDelete, opnR=repOpen,
                           session_id=session_id: deleteTable(canvas, t, uid, sid, n, a, d, delB, opnR, session_id))

        butDelete.place(
            x=1096, y=y_2,
            width=13,
            height=18)
        deletewidgets.append(butDelete)
        y_2 += 40

    window.resizable(False, False)
    window.mainloop()


window = Tk()
start()