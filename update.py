from tkinter import *


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file = f"update_acc_bg.png")
background = canvas.create_image(
    570.5, 371.5,
    image=background_img)

entry0_img = PhotoImage(file = f"border_tb_long.png")
entry0_bg = canvas.create_image(
    662.5, 208.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 350.0, y = 193,
    width = 625.0,
    height = 28)

entry1_img = PhotoImage(file = f"border_tb_long.png")
entry1_bg = canvas.create_image(
    662.5, 256.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 350.0, y = 241,
    width = 625.0,
    height = 28)

entry2_img = PhotoImage(file = f"border_tb_long.png")
entry2_bg = canvas.create_image(
    662.5, 303.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 350.0, y = 288,
    width = 625.0,
    height = 28)

entry3_img = PhotoImage(file = f"border_tb_long.png")
entry3_bg = canvas.create_image(
    662.5, 350.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 350.0, y = 335,
    width = 625.0,
    height = 28)

entry4_img = PhotoImage(file = f"border_tb_long.png")
entry4_bg = canvas.create_image(
    662.5, 397.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 350.0, y = 382,
    width = 625.0,
    height = 28)

entry5_img = PhotoImage(file = f"border_tb_long.png")
entry5_bg = canvas.create_image(
    662.5, 444.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry5.place(
    x = 350.0, y = 429,
    width = 625.0,
    height = 28)

entry6_img = PhotoImage(file = f"border_tb_long.png")
entry6_bg = canvas.create_image(
    662.5, 491.0,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry6.place(
    x = 350.0, y = 476,
    width = 625.0,
    height = 28)

entry7_img = PhotoImage(file = f"border_tb_short.png")
entry7_bg = canvas.create_image(
    365.0, 538.0,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry7.place(
    x = 290.0, y = 523,
    width = 150.0,
    height = 28)

entry8_img = PhotoImage(file = f"border_tb_short.png")
entry8_bg = canvas.create_image(
    645.0, 538.0,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry8.place(
    x = 570.0, y = 523,
    width = 150.0,
    height = 28)

entry9_img = PhotoImage(file = f"border_tb_short.png")
entry9_bg = canvas.create_image(
    900.0, 538.0,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry9.place(
    x = 825.0, y = 523,
    width = 150.0,
    height = 28)

img0 = PhotoImage(file = f"update_button_update_acc.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 445, y = 590,
    width = 105,
    height = 34)

img1 = PhotoImage(file = f"cancel_button_update_acc.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 589, y = 590,
    width = 105,
    height = 34)

window.resizable(False, False)
window.mainloop()
