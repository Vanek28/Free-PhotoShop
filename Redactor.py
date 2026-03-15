from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance

win = CTk()
win.geometry("950x750")
win.title("Редактор зображень")
set_appearance_mode('light')

img_copy = None
original_img = None
img = None
img_CTk = None
label = None


def load_image():
    global original_img, img, img_CTk, label, btn_file, img_copy, x, y
    global button1, button2, button3, btn4, btn5, btn6, btn7, btn8, btn9, slider1, ent1, ent2, btn_save

    file_path = filedialog.askopenfilename(filetypes=[("Зображення", "*.png *.jpg *.jpeg")])

    if file_path:
        original_img = Image.open(file_path)
        img = original_img.copy()
        img_copy = img.copy()

        x = 350
        y = 350

        btn_file.destroy()

        l_frame = CTkFrame(win, width=200, height=750, corner_radius=0)
        l_frame.place(relx=0, rely=0, anchor="nw")

        main_font = ("Verdana", 12, "bold")
        btn_color = "#1f538d"
        hover_c = "#14375e"

        button1 = CTkButton(l_frame, text="Повернути", command=rotate1, fg_color=btn_color, hover_color=hover_c,
                            font=main_font)
        button2 = CTkButton(l_frame, text="Чорно-білий", command=bl_wh, fg_color=btn_color, hover_color=hover_c,
                            font=main_font)
        button3 = CTkButton(l_frame, text="Блюр", command=blur1, fg_color=btn_color, hover_color=hover_c,
                            font=main_font)
        btn4 = CTkButton(l_frame, text="Контур", command=contour1, fg_color=btn_color, hover_color=hover_c,
                         font=main_font)
        btn5 = CTkButton(l_frame, text="Деталі", command=detail1, fg_color=btn_color, hover_color=hover_c,
                         font=main_font)
        btn6 = CTkButton(l_frame, text="Ембосс", command=emboss1, fg_color=btn_color, hover_color=hover_c,
                         font=main_font)
        btn7 = CTkButton(l_frame, text="Загострити", command=sharpen1, fg_color=btn_color, hover_color=hover_c,
                         font=main_font)
        btn8 = CTkButton(l_frame, text="Скинути", command=back, fg_color="#c0392b", hover_color="#a93226",
                         font=main_font)

        slider1 = CTkSlider(l_frame, from_=0, to=100, command=enchant1, button_color=btn_color)
        ent1 = CTkEntry(l_frame, placeholder_text="Ширина")
        ent2 = CTkEntry(l_frame, placeholder_text="Висота")
        btn9 = CTkButton(l_frame, text="Задати розмір", command=resize1, fg_color="#34495e", font=main_font)

        button1.pack(pady=10, padx=20, fill="x")
        button2.pack(pady=10, padx=20, fill="x")
        button3.pack(pady=10, padx=20, fill="x")
        btn4.pack(pady=10, padx=20, fill="x")
        btn5.pack(pady=10, padx=20, fill="x")
        btn6.pack(pady=10, padx=20, fill="x")
        btn7.pack(pady=10, padx=20, fill="x")
        btn8.pack(pady=10, padx=20, fill="x")
        slider1.pack(pady=15, padx=20)
        ent1.pack(pady=5, padx=20)
        ent2.pack(pady=5, padx=20)
        btn9.pack(pady=10, padx=20)

        img_CTk = CTkImage(light_image=img, size=(x, y))
        label = CTkLabel(win, text="", image=img_CTk)
        label.place(relx=0.6, rely=0.45, anchor="center")

        btn_save = CTkButton(win, text="Зберегти фото", command=save_image, fg_color="#27ae60", hover_color="#219150",
                             font=main_font, width=150, height=40)
        btn_save.place(relx=0.97, rely=0.96, anchor="se")


def save_image():
    global img
    if img:
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPG", "*.jpg")])
        if path:
            img.save(path)


def update_image():
    global img_CTk, label, x, y
    img_CTk = CTkImage(light_image=img, size=(x, y))
    label.configure(image=img_CTk)


def rotate1():
    global img, original_img
    try:
        original_img = original_img.rotate(90, expand=True)
        img = original_img.copy()
        update_image()
    except:
        pass


def bl_wh():
    global img, original_img
    try:
        original_img = original_img.convert('L')
        img = original_img.copy()
        update_image()
    except:
        pass


def blur1():
    global img, original_img
    try:
        original_img = original_img.filter(ImageFilter.BLUR)
        img = original_img.copy()
        update_image()
    except:
        pass


def contour1():
    global img, original_img
    try:
        original_img = original_img.filter(ImageFilter.CONTOUR)
        img = original_img.copy()
        update_image()
    except:
        pass


def detail1():
    global img, original_img
    try:
        original_img = original_img.filter(ImageFilter.DETAIL)
        img = original_img.copy()
        update_image()
    except:
        pass


def emboss1():
    global img, original_img
    try:
        original_img = original_img.filter(ImageFilter.EMBOSS)
        img = original_img.copy()
        update_image()
    except:
        pass


def sharpen1():
    global img, original_img
    try:
        original_img = original_img.filter(ImageFilter.SHARPEN)
        img = original_img.copy()
        update_image()
    except:
        pass


def enchant1(value):
    global img
    try:
        enhancer = ImageEnhance.Contrast(original_img)
        img = enhancer.enhance(float(value) / 50)
        update_image()
    except:
        pass


def back():
    global img, original_img, img_copy, x, y
    try:
        original_img = img_copy.copy()
        img = original_img.copy()
        x = 350
        y = 350
        update_image()
    except:
        pass


def resize1():
    global ent1, ent2, x, y
    try:
        x = int(ent1.get())
        y = int(ent2.get())
        ent1.delete(0, END)
        ent2.delete(0, END)
        update_image()
    except:
        ent1.delete(0, END)
        ent2.delete(0, END)


btn_file = CTkButton(win, text="Обрати фото", command=load_image, width=200, height=40, font=("Verdana", 12, "bold"))
btn_file.pack(pady=350)

button1 = button2 = button3 = btn4 = btn5 = btn6 = btn7 = btn8 = btn9 = None
slider1 = ent1 = ent2 = btn_save = None

win.mainloop()