import tkinter as tk
import text_adder
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from PIL import Image

BG_colorBirumuda = "#90E0EF"
BUTTON_CLRPURPLE = "#999DE8"
ADMIN_NAME = 'admin'
PASSWORD = '123'
FONT_colorBlue = "#023E8A"
BG_ColorFont = "#FFFFB0"


class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x350")
        self.root.config(background=BG_colorBirumuda)
        self.root.title("Tambahkan Teks atau Watermark ke Gambar")
        self.current_frame = None
        self.add_watermark_frame = AddWatermarkFrame(self.root)
        self.add_text_frame = AddTextFrame(self.root)
        self.option_frame = OptionFrame(self.root, self.add_watermark_frame, self.add_text_frame)
        self.login_frame = LoginFrame(self.root, self.option_frame)
        self.login_frame.pack()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def mainloop(self, *args, **kwargs):
        self.root.mainloop()

class LoginFrame():
    def __init__(self, master, option_frame):
        self.option_frame = option_frame
        self.frame = tk.Frame(master, background= BG_colorBirumuda)
        self.heading_label = tk.Label(self.frame,
                                      bg="#FFFFB0",
                                      text="Aplikasi Untuk Menambahkan Watermark / Teks Ke Gambar",
                                      font=("homework",18),
                                      fg=FONT_colorBlue)
        self.heading_label.pack()

        self.line = tk.Canvas(self.frame, width=500, height=3, background="#999DE8")

        canvas_height = 20
        canvas_width = 530
        y = int(canvas_height / 2)
        self.line.create_line(0, y, canvas_width, y)
        self.line.pack()

        tk.Label(self.frame, text="Username",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        # username entry
        self.username_entry = tk.Entry(self.frame, width=30)
        self.username_entry.pack(pady=25)

        tk.Label(self.frame, text="Password",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        self.password_entry = tk.Entry(self.frame, width=30)
        self.password_entry.pack(pady=25)

        # LOGIN BUTTON
        self.login_button = tk.Button(self.frame,
                                      text="Login",
                                      background=BUTTON_CLRPURPLE,
                                      command=self.login,
                                      font=("georgia", 10),
                                      height=1,
                                      width=15,
                                      fg='white')
        self.login_button.pack(pady=10)

        # login error message
        self.login_error_message = tk.Label(self.frame, text='', fg='red')
        self.login_error_message.pack(pady=10)

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == '123':
            self.frame.pack_forget()
            self.option_frame.pack()
        else:
            self.login_error_message.config(text='Username atau password salah')

class OptionFrame():
    def __init__(self, master, add_watermark_frame, add_text_frame):
        self.frame = tk.Frame(master, background=BG_colorBirumuda)
        self.add_watermark_frame = add_watermark_frame
        self.add_text_frame = add_text_frame

        self.heading_label = tk.Label(self.frame,
                                      bg="#FFFFB0",
                                      text="Silahkan menu yang sesuai dengan Anda inginkan",
                                      font=("homework",20),
                                      fg=FONT_colorBlue)
        self.heading_label.pack()

        self.line2 = tk.Canvas(self.frame, width=500, height=3, background="#999DE8")

        canvas_height = 20
        canvas_width = 530
        y = int(canvas_height / 2)
        self.line2.create_line(0, y, canvas_width, y)
        self.line2.pack()

        self.add_text_button = tk.Button(self.frame,
                                         text="Tambah teks",
                                         background=BUTTON_CLRPURPLE,
                                         command=self.add_text,
                                         font=("georgia", 13),
                                         height=1,
                                         width=15,
                                         fg='white')
        self.add_text_button.pack(pady=30)

        tk.Label(self.frame, text="Atau",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        self.add_watermark_button = tk.Button(self.frame,
                                              text="Tambah watermark",
                                              background=BUTTON_CLRPURPLE,
                                              command=self.add_watermark,
                                              font=("georgia", 13),
                                              height=1,
                                              width=17,
                                              fg='white')
        self.add_watermark_button.pack(pady=30)

    def add_watermark(self):
        self.frame.pack_forget()
        self.add_watermark_frame.pack()

    def add_text(self):
        self.frame.pack_forget()
        self.add_text_frame.pack()

    def pack(self, *args, **kwargs):
        self.frame.pack()

class AddWatermarkFrame():
    def __init__(self, master):
        self.frame = tk.Frame(master, background=BG_colorBirumuda)
        self.file_path_var = tk.StringVar(value='(*keterangan*)')

        tk.Label(self.frame, text="Pilih gambar yang ingin diwatermark",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        tk.Button(self.frame,
                  text="Pilih Gambar",
                  command=self.open_file,
                  font=("georgia", 10),
                  height=1,
                  width=15,
                  fg="#FFF8DC",
                  background=BUTTON_CLRPURPLE).pack(pady=20)

        tk.Label(self.frame, text="",
                 bg='white',
                 font=("georgia", 11),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda,
                 textvariable=self.file_path_var).pack(pady=20)

        tk.Label(self.frame, text="Tambahkan watermark pada foto",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        self.watermark_text_entry = tk.Entry(self.frame, width=50)
        self.watermark_text_entry.pack(pady=10)

        tk.Button(self.frame,
                  text="Tambakan watermark",
                  command=self.add_watermark,
                  font=("georgia", 10),
                  height=1,
                  width=20,
                  fg="#FFF8DC",
                  background=BUTTON_CLRPURPLE).pack(pady=20)

    def add_watermark(self):
        if not self.file_path_var.get():
            return

        image = plt.imread(self.file_path_var.get()).astype(np.uint8)
        text = self.watermark_text_entry.get()

        text_adder.add_watermark_to_image(image, text)
        Image.open('image_modified.jpg').show()

    def open_file(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.file_path_var.set(path)

    def back(self):
        pass

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)

class AddTextFrame():
    def __init__(self, master):
        self.frame = tk.Frame(master, background=BG_colorBirumuda)
        self.file_path_var = tk.StringVar(value='(*keterangan*)')

        tk.Label(self.frame, text="Pilih gambar yang ingin ditambahkan teks",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        tk.Button(self.frame,
                  text="Pilih Gambar",
                  command=self.open_file,
                  font=("georgia", 10),
                  height=1,
                  width=15,
                  fg="#FFF8DC",
                  background=BUTTON_CLRPURPLE).pack(pady=20)

        tk.Label(self.frame, text="",
                 bg='white',
                 font=("georgia", 11),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda,
                 textvariable=self.file_path_var).pack(pady=20)

        tk.Label(self.frame, text="Tambahkan teks pada foto",
                 bg='white',
                 font=("homework", 20),
                 fg=FONT_colorBlue,
                 background=BG_colorBirumuda).pack()

        self.text_entry = tk.Entry(self.frame, width=50)
        self.text_entry.pack(pady=10)

        tk.Button(self.frame,
                  text="Tambakan teks",
                  command=self.add_text,
                  font=("georgia", 10),
                  height=1,
                  width=20,
                  fg="#FFF8DC",
                  background=BUTTON_CLRPURPLE).pack(pady=20)

    def add_text(self):
        if not self.file_path_var.get():
            return

        image = plt.imread(self.file_path_var.get()).astype(np.uint8)
        text = self.text_entry.get()

        text_adder.add_text_to_image(image, text)
        Image.open('image_modified.jpg').show()

    def open_file(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.file_path_var.set(path)

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)

Main().mainloop()