from tkinter import *
import textwrap

def open_dashboard():
    pass

def open_predict():
    window.destroy()
    import user_predict_page

def open_report():
    window.destroy()
    import user_report_page

def open_profile():
    window.destroy()
    import user_profile_page

def login():
    window.destroy()
    import login_page

def signup():
    window.destroy()
    import sign_up

def close_sidebar():
    window.geometry("1140x700")
    window.configure(bg="#74a7f3")
    canvas = Canvas(
        window,
        bg="#74a7f3",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    dashboard_bg = PhotoImage(file=f"dashboard_bg.png")
    background = canvas.create_image(
        600.0, 283.0,
        image=dashboard_bg)

    canvas.create_text(
        379.5, 200.5,
        text="What is post COVID-19 complications ?",
        fill="#000000",
        font=("Nunito-SemiBold", int(15.5)))

    canvas.create_text(
        540.0, 260.0,
        text="Post-COVID complications are a wide range of new, returning, or ongoing complication problems \nthat people experience after being infected with the virus that causes COVID-19.",
        fill="#000000",
        font=("Nunito-Light", int(13.0)))

    text = "The Post-COVID-19 Complication Prediction System is a system developed to help users who have been infected with COVID-19 in order to identify the probability for him/her to infect with post-COVID-19 complications. For your information, this system only applies to COVID-19 patients because the data required involves the data of COVID-19 patients. Please proceed to the prediction page to start the prediction session. Thank you."
    wrapped_text = textwrap.fill(text, width=120)
    canvas.create_text(
        602.0, 450.0,
        text=wrapped_text,
        fill="#000000",
        font=("Nunito-Medium", int(13.0)))

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

    window.resizable(False, False)
    window.mainloop()

def open_sidebar():
    window.geometry("1140x700")
    window.configure(bg="#74a7f3")
    canvas = Canvas(
        window,
        bg="#74a7f3",
        height=700,
        width=1140,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    dashboard_bg = PhotoImage(file=f"dashboard_bg.png")
    background = canvas.create_image(
        600.0, 283.0,
        image=dashboard_bg)

    canvas.create_text(
        379.5, 200.5,
        text="What is post COVID-19 complications ?",
        fill="#000000",
        font=("Nunito-SemiBold", int(15.5)))

    canvas.create_text(
        540.0, 260.0,
        text="Post-COVID complications are a wide range of new, returning, or ongoing complication problems \nthat people experience after being infected with the virus that causes COVID-19.",
        fill="#000000",
        font=("Nunito-Light", int(13.0)))

    text = "The Post-COVID-19 Complication Prediction System is a system developed to help users who have been infected with COVID-19 in order to identify the probability for him/her to infect with post-COVID-19 complications. For your information, this system only applies to COVID-19 patients because the data required involves the data of COVID-19 patients. Please proceed to the prediction page to start the prediction session. Thank you."
    wrapped_text = textwrap.fill(text, width=120)
    canvas.create_text(
        602.0, 450.0,
        text=wrapped_text,
        fill="#000000",
        font=("Nunito-Medium", int(13.0)))

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
    prediction_sidebar_open_button = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=open_predict,
        relief="flat")

    prediction_sidebar_open_button.place(
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
        x=212, y=27,
        width=31,
        height=31)

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":

    window = Tk()

    window.geometry("1140x700")
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

    main_dashboard_bg = PhotoImage(file=f"main_dashboard_bg.png")
    background = canvas.create_image(
        570.0, 319.5,
        image=main_dashboard_bg)

    loginBdashboard = PhotoImage(file=f"login_button_main_dashboard.png")
    bLogin = Button(
        image=loginBdashboard,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat")

    bLogin.place(
        x=520, y=363,
        width=100,
        height=35)

    signupBdashboard = PhotoImage(file=f"signup_button_main_dashboard.png")
    bSignup = Button(
        image=signupBdashboard,
        borderwidth=0,
        highlightthickness=0,
        command=signup,
        relief="flat")

    bSignup.place(
        x=520, y=418,
        width=100,
        height=35)

    window.resizable(False, False)
    window.mainloop()

else:
    window = Tk()
    close_sidebar()