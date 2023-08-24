import mysql.connector
from tkinter import *
import datetime
import textwrap
from login_page import uid

global uid
uid = uid()

def retry():
    root.destroy()

def open_dashboard():
    window.destroy()
    import user_dashboard

def open_predict():
    pass

def open_report():
    window.destroy()
    import user_report_page

def open_profile():
    window.destroy()
    import user_profile_page

def addMedCond():
    medcondwidgets = []
    addmedwidgets = []
    deletemedwidgets = []

    global y_1, b_1, z_1, med_cond, list_med

    med_condition = StringVar()
    list_med.append(med_condition)

    y_1 += 40
    predict = OptionMenu(
        window,
        med_condition,
        *med_cond)
    predict.place(
        x=403, y=y_1,
        width=163,
        height=27)
    medcondwidgets.append(predict)

    b_1 += 40
    addPredict = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addMedCond,
        relief="flat")
    addPredict.place(
        x=572, y=b_1,
        width=20,
        height=20)
    addmedwidgets.append(addPredict)

    def deleteMedCond():
        if medcondwidgets:
            dropdown = medcondwidgets.pop()
            dropdown.destroy()
        if addmedwidgets:
            button = addmedwidgets.pop()
            button.destroy()
        if deletemedwidgets:
            button = deletemedwidgets.pop()
            button.destroy()
        list_med.pop()

    z_1 += 40
    deletePredict = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=deleteMedCond,
        relief="flat")
    deletePredict.place(
        x=598, y=z_1,
        width=16,
        height=22)
    deletemedwidgets.append(deletePredict)

def addCovSymptom():
    CovSympwidgets = []
    addCovwidgets = []
    deleteCovwidgets = []

    global y_2, b_2, z_2, cov_symp, list_cov

    cov_symptom = StringVar()
    list_cov.append(cov_symptom)

    y_2 += 40
    predict = OptionMenu(
        window,
        cov_symptom,
        *cov_symp)
    predict.place(
        x=786, y=y_2,
        width=163,
        height=27)
    CovSympwidgets.append(predict)

    b_2 += 40
    addPredict = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addCovSymptom,
        relief="flat")
    addPredict.place(
        x=955, y=b_2,
        width=20,
        height=20)
    addCovwidgets.append(addPredict)

    def deleteCovSymptom():
        if CovSympwidgets:
            dropdown = CovSympwidgets.pop()
            dropdown.destroy()
        if addCovwidgets:
            button = addCovwidgets.pop()
            button.destroy()
        if deleteCovwidgets:
            button = deleteCovwidgets.pop()
            button.destroy()
        list_cov.pop()

    z_2 += 40
    deletePredict = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=deleteCovSymptom,
        relief="flat")
    deletePredict.place(
        x=981, y=z_2,
        width=16,
        height=22)
    deleteCovwidgets.append(deletePredict)

def done():
    root.destroy()
    global window
    window = Tk()
    close_sidebar()

def sid():
    global session_id
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    cursor.execute("SELECT session_id FROM userinput ORDER BY session_id DESC LIMIT 1")

    session_id = cursor.fetchone()[0]

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

def predict():
    global id, fullname, age, vaccine_status, covid_period
    med_condition_values = [x.get() for x in list_med]
    cov_symptom_values = [y.get() for y in list_cov]

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

    if "" in med_condition_values or "" in cov_symptom_values or vaccine_status.get() == "" or covid_period.get() == "" or fullname.get() == "" or age.get() == "":
        text = "Please fill in the blanks"
        errorBox(text)

    elif any(med_condition_values.count(x.get()) > 1 for x in list_med) or any(
            cov_symptom_values.count(y.get()) > 1 for y in list_cov):
        text = "You can't have similar value selected for the medical conditions and Covid-19 symptoms"
        wrapped_text1 = textwrap.fill(text, width=40)
        errorBox(wrapped_text1)

    elif len(age.get()) > 3 or not age.get().isdigit():
        text = "Please insert valid age"
        errorBox(text)

    else:

        conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
        cursor = conn.cursor()

        med_condition_values_string = ', '.join(med_condition_values)
        cov_symptom_values_string = ', '.join(cov_symptom_values)
        vaccine = vaccine_status.get()
        period = covid_period.get()
        now = datetime.datetime.now()

        user_input = []
        user_input.append(age.get())
        user_input.append(vaccine)
        user_input.append(period)
        for mc in list_med:
            user_input.append(mc.get())
        for mc in list_cov:
            user_input.append(mc.get())

        user_input = [str(item) for item in user_input]
        user_input = set(user_input)
        user_input = list(user_input)
        user_input = sorted(user_input)

        values = []
        all_input = ["Tiredness or Fatigue", "Difficult to Breath", "Cough or Sore Throat", "Chest Pain",
                     "Fast-beating Heart", "Fever", "Change in Smell or Taste", "Difficult to concentrate", "Headache",
                     "Sleep Problems", "Dizziness when you Stand Up", "Diarrhea", "Stomach Pain",
                     "Joint or Muscle Pain",
                     "Rash", "Low level of Oxygen in Blood (Sp02 less than 95%)", "Diabetes", "Obesity", "Asthma"]

        if any(symptom in user_input for symptom in all_input):
            if "Tiredness or Fatigue" in user_input:
                values += ["Tiredness or Fatigue", "Difficult to Breath", "Cough or Sore Throat"]
            if "Difficult to Breath" in user_input:
                values += ["Difficult to Breath"]
            if "Cough or Sore Throat" in user_input:
                values += ["Tiredness or Fatigue", "Cough or Sore Throat", "Headache"]
            if "Chest Pain" in user_input:
                values += ["Cough or Sore Throat", "Chest Pain", "Headache"]
            if "Fast-beating Heart" in user_input:
                values += ["Fast-beating Heart", "Fever"]
            if "Fever" in user_input:
                values += ["Tiredness or Fatigue", "Chest Pain", "Fever", "Headache"]
            if "Change in Smell or Taste" in user_input:
                values += ["Tiredness or Fatigue", "Chest Pain", "Change in Smell or Taste", "Headache"]
            if "Difficult to concentrate" in user_input:
                values += ["Fast-beating Heart", "Difficult to concentrate"]
            if "Headache" in user_input:
                values += ["Tiredness or Fatigue", "Difficult to Breath", "Cough or Sore Throat", "Chest Pain"]
            if "Sleep Problems" in user_input:
                values += ["Difficult to Breath", "Cough or Sore Throat", "Sleep Problems"]
            if "Dizziness when you Stand Up" in user_input:
                values += ["Cough or Sore Throat", "Fast-beating Heart", "Difficult to concentrate"]
            if "Diarrhea" in user_input:
                values += ["Fast-beating Heart", "Sleep Problems"]
            if "Joint or Muscle Pain" in user_input:
                values += ["Cough or Sore Throat", "Joint or Muscle Pain"]
            if "Diabetes" in user_input:
                values += ["Cough or Sore Throat", "Chest Pain", "Change in Smell or Taste", "Difficult to concentrate",
                           "Headache"]
            if "Obesity" in user_input:
                values += ["Cough or Sore Throat", "Chest Pain", "Joint or Muscle Pain"]
            if "Asthma" in user_input:
                values += ["Difficult to concentrate", "Sleep Problems"]
        else:
            values.append("No symptoms or complications")

        if values[0] == "No symptoms or complications":
            values = ''.join(values)
        else:
            values = set(values)
            values = list(values)
            values = sorted(values)
            values = ', '.join(values)

        insertquery = "INSERT INTO userinput(user_id, fullname, age, med_condition, date, cov_symptom, vaccine_stats, cov_period, result) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insertquery, (
        uid, fullname.get().upper(), age.get(), med_condition_values_string, now, cov_symptom_values_string, vaccine,
        period, values))

        conn.commit()

        sid()

        window.destroy()

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

        def disable_event():
            pass

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
                389.0, 706.5,
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
        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.mainloop()

def close_sidebar():
    global y_1, y_2, b_1, b_2, z_1, z_2, img5, img6
    window.geometry("1140x700+200+50")
    window.configure(bg="#4d72ab")

    img5 = PhotoImage(file=f"add_predict.png")
    img6 = PhotoImage(file=f"delete_predict.png")
    canvas = Canvas(
        window,
        bg="#4d72ab",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background_prediction_page.png")
    background = canvas.create_image(
        508.5, 350.0,
        image=background_img)

    img0 = PhotoImage(file=f"profile_sidebar_close.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_profile,
        relief="flat")

    b0.place(
        x=10, y=285,
        width=92,
        height=48)

    img1 = PhotoImage(file=f"report_sidebar_close.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    b1.place(
        x=10, y=237,
        width=92,
        height=48)

    img2 = PhotoImage(file=f"predict_sidebar_close.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    b2.place(
        x=10, y=189,
        width=92,
        height=48)

    img3 = PhotoImage(file=f"dashboard_sidebar_close.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    b3.place(
        x=10, y=141,
        width=92,
        height=48)

    img4 = PhotoImage(file=f"arrow_sidebar_close.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=open_sidebar,
        relief="flat")

    b4.place(
        x=40, y=27,
        width=31,
        height=31)

    global vaccine_status, covid_period, fullname, age
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT fullname, age from userinfo WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    for row in result:
        fullname, age = row

    fullname = StringVar(value=fullname)
    age = StringVar(value=age)

    entry0_img = PhotoImage(file=f"fullname_predict.png")
    entry0_bg = canvas.create_image(
        664.0, 183.5,
        image=entry0_img)

    entry0 = Entry(
        textvariable=fullname,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry0.place(
        x=391, y=169,
        width=546,
        height=27)

    entry1_img = PhotoImage(file=f"age_predict.png")
    entry1_bg = canvas.create_image(
        453.0, 231.5,
        image=entry1_img)

    entry1 = Entry(
        textvariable=age,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry1.place(
        x=391, y=217,
        width=124,
        height=27)

    vaccine_stats = ["1st dose", "2nd dose", "1st booster dose", "2nd booster dose"]
    vaccine_status = StringVar()

    entry2_img = PhotoImage(file=f"vaccine_predict.png")
    entry2_bg = canvas.create_image(
        798.5, 231.5,
        image=entry2_img)

    entry2 = OptionMenu(
        window,
        vaccine_status,
        *vaccine_stats)

    entry2.place(
        x=660, y=217,
        width=277,
        height=27)

    period = ["2 weeks", "1 month", "3 month and above"]
    covid_period = StringVar()

    entry3_img = PhotoImage(file=f"period_predict.png")
    entry3_bg = canvas.create_image(
        746.0, 279.5,
        image=entry3_img)

    entry3 = OptionMenu(
        window,
        covid_period,
        *period)

    entry3.place(
        x=555, y=265,
        width=382,
        height=27)

    y_1 = y_2 = 313
    b_1 = b_2 = 317
    z_1 = z_2 = 316
    # medical condition dropdown menu

    global med_cond, list_med
    med_cond = ["Diabetes", "Obesity", "Asthma"]
    med_cond = sorted(med_cond)
    med_cond.insert(0, "No Symptom")
    list_med = []
    med_condition = StringVar()
    list_med.append(med_condition)

    entry4_img = PhotoImage(file=f"med_cond_predict.png")
    entry4_bg = canvas.create_image(
        484.5, 327.5,
        image=entry4_img)

    OptionMenu(
        window,
        med_condition,
        *med_cond).place(
        x=403, y=y_1,
        width=163,
        height=27)

    global cov_symp, list_cov
    # covid symptom dropdown menu
    cov_symp = ["Tiredness or Fatigue", "Difficult to Breath", "Cough or Sore Throat", "Chest Pain",
                "Fast-beating Heart", "Fever", "Change in Smell or Taste", "Difficult to concentrate", "Headache",
                "Sleep Problems", "Dizziness when you Stand Up", "Diarrhea", "Stomach Pain", "Joint or Muscle Pain",
                "Rash", "Low level of Oxygen in Blood (Sp02 less than 95%)", "Depression or Anxiety", "Ear infection",
                "Change in Menstrual Cycle"]
    cov_symp = sorted(cov_symp)
    cov_symp.insert(0, "No Symptom")
    list_cov = []
    cov_symptom = StringVar()
    list_cov.append(cov_symptom)

    entry5_img = PhotoImage(file=f"med_cond_predict.png")
    entry5_bg = canvas.create_image(
        867.5, 327.5,
        image=entry5_img)

    OptionMenu(
        window,
        cov_symptom,
        *cov_symp).place(
        x=786, y=y_2,
        width=163,
        height=27)

    # add med cond dropdown menu
    Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addMedCond,
        relief="flat").place(
        x=572, y=b_1,
        width=20,
        height=20)

    # add cov symp dropdown menu
    Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addCovSymptom,
        relief="flat").place(
        x=955, y=b_2,
        width=20,
        height=20)

    img9 = PhotoImage(file=f"prediction_button.png")
    b9 = Button(
        image=img9,
        borderwidth=0,
        highlightthickness=0,
        command=predict,
        relief="flat")

    b9.place(
        x=571, y=623,
        width=100,
        height=35)

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()

def open_sidebar():
    global y_1, y_2, b_1, b_2, z_1, z_2, img5, img6
    window.geometry("1140x700+200+50")
    window.configure(bg="#4d72ab")

    img5 = PhotoImage(file=f"add_predict.png")
    img6 = PhotoImage(file=f"delete_predict.png")
    canvas = Canvas(
        window,
        bg="#4d72ab",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background_sidebar_open_predict.png")
    background = canvas.create_image(
        508.5, 350.0,
        image=background_img)

    img0 = PhotoImage(file=f"profile_sidebar_open.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_profile,
        relief="flat")

    b0.place(
        x=10, y=285,
        width=238,
        height=48)

    img1 = PhotoImage(file=f"report_sidebar_open.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=open_report,
        relief="flat")

    b1.place(
        x=10, y=237,
        width=238,
        height=48)

    img2 = PhotoImage(file=f"prediction_sidebar_open.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    b2.place(
        x=10, y=189,
        width=238,
        height=48)

    img3 = PhotoImage(file=f"dashboard_sidebar_open.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=open_dashboard,
        relief="flat")

    b3.place(
        x=10, y=141,
        width=238,
        height=48)

    img4 = PhotoImage(file=f"arrow_sidebar_open.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=close_sidebar,
        relief="flat")

    b4.place(
        x=198, y=27,
        width=31,
        height=31)

    global vaccine_status, covid_period, fullname, age
    conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="postcovid19")
    cursor = conn.cursor()

    acc = "SELECT fullname, age from userinfo WHERE user_id = %s"
    cursor.execute(acc, (uid,))
    result = cursor.fetchall()

    for row in result:
        fullname, age = row

    fullname = StringVar(value=fullname)
    age = StringVar(value=age)

    entry0_img = PhotoImage(file=f"fullname_predict.png")
    entry0_bg = canvas.create_image(
        664.0, 183.5,
        image=entry0_img)

    entry0 = Entry(
        textvariable=fullname,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry0.place(
        x=391, y=169,
        width=546,
        height=27)

    entry1_img = PhotoImage(file=f"age_predict.png")
    entry1_bg = canvas.create_image(
        453.0, 231.5,
        image=entry1_img)

    entry1 = Entry(
        textvariable=age,
        bd=0,
        bg="#ffffff",
        highlightthickness=0)

    entry1.place(
        x=391, y=217,
        width=124,
        height=27)

    vaccine_stats = ["1st dose", "2nd dose", "1st booster dose", "2nd booster dose"]
    vaccine_status = StringVar()

    entry2_img = PhotoImage(file=f"vaccine_predict.png")
    entry2_bg = canvas.create_image(
        798.5, 231.5,
        image=entry2_img)

    entry2 = OptionMenu(
        window,
        vaccine_status,
        *vaccine_stats)

    entry2.place(
        x=660, y=217,
        width=277,
        height=27)

    period = ["2 weeks", "1 month", "3 month and above"]
    covid_period = StringVar()

    entry3_img = PhotoImage(file=f"period_predict.png")
    entry3_bg = canvas.create_image(
        746.0, 279.5,
        image=entry3_img)

    entry3 = OptionMenu(
        window,
        covid_period,
        *period)

    entry3.place(
        x=555, y=265,
        width=382,
        height=27)

    y_1 = y_2 = 313
    b_1 = b_2 = 317
    z_1 = z_2 = 316
    # medical condition dropdown menu

    global med_cond, list_med
    med_cond = ["Diabetes", "Obesity", "Asthma"]
    med_cond = sorted(med_cond)
    med_cond.insert(0, "No Symptom")
    list_med = []
    med_condition = StringVar()
    list_med.append(med_condition)

    entry4_img = PhotoImage(file=f"med_cond_predict.png")
    entry4_bg = canvas.create_image(
        484.5, 327.5,
        image=entry4_img)

    OptionMenu(
        window,
        med_condition,
        *med_cond).place(
        x=403, y=y_1,
        width=163,
        height=27)

    global cov_symp, list_cov
    # covid symptom dropdown menu
    cov_symp = ["Tiredness or Fatigue", "Difficult to Breath", "Cough or Sore Throat", "Chest Pain",
                "Fast-beating Heart", "Fever", "Change in Smell or Taste", "Difficult to concentrate", "Headache",
                "Sleep Problems", "Dizziness when you Stand Up", "Diarrhea", "Stomach Pain", "Joint or Muscle Pain",
                "Rash", "Low level of Oxygen in Blood (Sp02 less than 95%)", "Depression or Anxiety", "Ear infection",
                "Change in Menstrual Cycle"]
    cov_symp = sorted(cov_symp)
    cov_symp.insert(0, "No Symptom")
    list_cov = []
    cov_symptom = StringVar()
    list_cov.append(cov_symptom)

    entry5_img = PhotoImage(file=f"med_cond_predict.png")
    entry5_bg = canvas.create_image(
        867.5, 327.5,
        image=entry5_img)

    OptionMenu(
        window,
        cov_symptom,
        *cov_symp).place(
        x=786, y=y_2,
        width=163,
        height=27)

    # add med cond dropdown menu
    Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addMedCond,
        relief="flat").place(
        x=572, y=b_1,
        width=20,
        height=20)

    # add cov symp dropdown menu
    Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=addCovSymptom,
        relief="flat").place(
        x=955, y=b_2,
        width=20,
        height=20)

    img9 = PhotoImage(file=f"prediction_button.png")
    b9 = Button(
        image=img9,
        borderwidth=0,
        highlightthickness=0,
        command=predict,
        relief="flat")

    b9.place(
        x=571, y=623,
        width=100,
        height=35)

    cursor.close()
    conn.close()

    window.resizable(False, False)
    window.mainloop()


window = Tk()

close_sidebar()
