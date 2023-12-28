import tkinter as tk
from tkinter import messagebox,ttk
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

    def setup_ui(self):
        self.NilaiFrame = ct.CTkFrame(master=self, fg_color='#ccffff')
        self.NilaiFrame.pack(fill='both',expand=True,anchor=tkinter.CENTER)

        self.label()
        
        self.entry()
        
        self.treeview()
    
    def label(self):
        self.nama = ct.CTkLabel(master=self,fg_color= '#ccffff', text="nama murid",anchor="e",justify = "right",width=110,font=('montserrat',17))
        self.id = ct.CTkLabel(master=self,fg_color= '#ccffff',text="id murid",anchor="e",justify = "right",width=110,font=('montserrat',17))
        self.id_kelas = ct.CTkLabel(master=self,fg_color= '#ccffff',text="id kelas",anchor="e",justify = "right",width=110,font=('montserrat',17))
        self.id_matkul = ct.CTkLabel(master=self,fg_color= '#ccffff',text="matkul",anchor="e",justify = "right",width=110,font=('montserrat',17))
        self.nilai_tugas = ct.CTkLabel(master=self,fg_color= '#ccffff',text="nilai tugas",anchor="e",justify = "right",width=110,font=('montserrat',17))
        self.nilai_ujian = ct.CTkLabel(master=self,fg_color= '#ccffff',text="nilai ujian",anchor="e",justify = "right",width=110,font=('montserrat',17))
        #self.nilai_rata_rata = ct.CTkLabel(master=self,fg_color= '#ccffff',text="rata-rata",anchor="e",justify = "right",width=110,font=('montserrat',17))
        
        self.nama.place(x=285, y=100)
        self.id.place(x=285, y=140)
        self.id_kelas.place(x=285, y=180)
        self.id_matkul.place(x=285, y=220)
        self.nilai_tugas.place(x=285, y=260)
        self.nilai_ujian.place(x=285, y=300)
        #self.nilai_rata_rata.place(x=285, y=340)

    def entry(self):
        self.nama_var = tk.StringVar()
        #self.nama_var.trace_add(self.create_message)
        self.id_var = tk.StringVar()
        self.id_kelas_var = tk.StringVar()
        self.id_matkul_var = tk.StringVar()
        self.nilai_tugas_var = tk.StringVar()
        self.nilai_ujian_var = tk.StringVar()

        self.entry_nama = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.nama_var, width = 1000)
        self.entry_nama.place(x=405, y=100)
        #printing_nama = str(self.nama_var.get())
        #self.label_nama = ct.CTkLabel(master=self, text = printing_nama, font=('montserrat',17))
        #self.label_nama.place(x=405, y=130)
        self.entry_id = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.id_var, width = 1000)
        self.entry_id.place(x=405, y=140)
        #printing_id = str(self.id_var.get())
        ##self.label_id = ct.CTkLabel(master=self, text = printing_id, font=('montserrat',17))
        #self.label_id.place(x=405, y=130)
        self.entry_id_kelas = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.id_var, width = 800)
        self.entry_id_kelas.place(x=405, y=180)
        self.entry_id_matkul = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.id_var, width = 800)
        self.entry_id_matkul.place(x=405, y=220)
        self.entry_nilai_tugas = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.id_var, width = 800)
        self.entry_nilai_tugas.place(x=405, y=260)
        self.entry_nilai_ujian = ct.CTkEntry(master=self, font=('montserrat',17), textvariable=self.id_var, width = 800)
        self.entry_nilai_ujian.place(x=405, y=300)

        self.hasil_entry_nama = self.entry_nama.get()
        self.hasil_entry_id = self.entry_id.get()
        self.hasil_entry_id_kelas = self.entry_id_kelas.get()
        self.hasil_entry_id_matkul = self.entry_id_matkul.get()
        self.hasil_entry_nilai_tugas = float(self.entry_nilai_tugas.get())
        self.hasil_entry_nilai_ujian = float(self.entry_nilai_ujian.get())

    def treeview(self):
        columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata-rata')
        table = ttk.Treeview(self, columns=columns, show='headings')
        table.heading('id', text='ID')
        table.heading('nama', text='Nama')
        table.heading('kelas', text='Kelas')
        table.heading('matkul', text='Matkul')
        table.heading('nilai tugas', text='Nilai Tugas')
        table.heading('nilai ujian', text='Nilai Ujina')
        table.heading('rata-rata', text='Rata-Rata')
        
