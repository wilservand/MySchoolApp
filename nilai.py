import tkinter
from tkinter import messagebox
import customtkinter as ct
from PIL import ImageTk, Image
from main import *
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

class Nilai (ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
        self.nilai_frames = {}
        self.setup_ui()
        self.frame_nilai()
        self.pilihan_menu = pilihan_menu(self)
        self.show_nilai_button = ct.CTkButton(master=self.pilihan_menu,text="show nilai murid",
                                           command=lambda: self.pindah_show_nilai())
        self.show_nilai_button.configure(height = 20, width = 50)
        self.show_nilai_button.place(x = 70, y = 70)
        #(130, 180, window=self.profile_button, anchor=tkinter.CENTER)
        self.ubah_nilai_tugas_button = ct.CTkButton(master=self.pilihan_menu,text="ubah nilai tugas murid",
                                           command=lambda: self.pindah_ubah_nilai_tugas())
        self.ubah_nilai_tugas_button.configure(height = 20, width = 50)
        self.ubah_nilai_tugas_button.place(x = 120, y = 70)
        self.ubah_nilai_ujian_button = ct.CTkButton(master=self.pilihan_menu,text="ubah nilai ujian murid",
                                           command=lambda: self.pindah_ubah_nilai_ujian())
        self.ubah_nilai_ujian_button.configure(height = 20, width = 50)
        self.ubah_nilai_ujian_button.place(x = 170, y = 70)

    def setup_ui(self):
        self.NilaiFrame = ct.CTkFrame(master=self, fg_color='#ccffff')
        self.NilaiFrame.pack(fill='both',expand=True,anchor=tkinter.CENTER)

        self.testLabel = ct.CTkLabel(master=self.NilaiFrame, text="Nilai Page", font=self.font, text_color='black')
        self.testLabel.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

    def frame_nilai(self):
        show_nilai_frame = show_nilai(self,self.controller)
        ubah_nilai_tugas_frame = ubah_nilai_tugas(self,self.controller)
        ubah_nilai_ujian_frame = ubah_nilai_ujian(self,self.controller)
        self.nilai_frames [show_nilai] = show_nilai_frame
        self.nilai_frames [ubah_nilai_tugas]= ubah_nilai_tugas_frame
        self.nilai_frames [ubah_nilai_ujian]= ubah_nilai_ujian_frame

    def change_dashFrame(self,frame_name):
        for frame in self.nilai_frames.values():
            frame.place_forget()

        if frame_name is not None:
            new_frame = self.nilai_frames[frame_name]
            new_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def pindah_show_nilai(self):
        self.change_dashFrame(show_nilai)

    def pindah_ubah_nilai_tugas(self):
        self.change_dashFrame(ubah_nilai_tugas)

    def pindah_ubah_nilai_ujian(self):
        self.change_dashFrame(ubah_nilai_ujian)

class pilihan_menu(ct.CTkCanvas):
    def __init__(self,parent):
        super().__init__(parent, width=280, height=70, bg=('grey'), bd=0)
        self.button_callback = None
        self.menu_logo = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Desain tanpa judul.jpg")
        new_size = (150, 75)
        self.menu_logo_resized = self.menu_logo.resize(new_size)
        self.menu_logo_tk = ImageTk.PhotoImage(self.menu_logo_resized)
        self.create_image(130,55, image=self.menu_logo_tk, anchor=tkinter.CENTER)
        self.menu_button = ct.CTkButton(self, text="MySchool Menu", command=lambda : self.button_callback())
        self.create_window(130,120, window=self.menu_button, anchor=tkinter.CENTER)

class show_nilai(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)

class ubah_nilai_tugas(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)

class ubah_nilai_ujian(ct.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.curr = curr_dbApp
        self.conn = conn_dbApp
        self.font = ct.CTkFont(family='montserrat', size=17)
