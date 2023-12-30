import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct
from main import *
import statistics as st
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

class kelas (ct.CTk):
    def __init__(self,curr,conn):
        super().__init__()


        self.curr = curr
        self.conn = conn
        self.font = ct.CTkFont(family='montserrat', size=17)


    def setup_uiKelas(self,masterss):

        self.nama = ct.CTkLabel(master=masterss,fg_color= '#ccffff', text="nama Kelas",anchor="e",justify = "right",width=60)
        self.font_kelas = ct.CTkFont('montserrat',15)
        self.nama.configure(font=self.font_kelas)
        self.tingkat = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="tingkat kelas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.wali = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="wali kelas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.ketua = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="ketua kelas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.jumlah = ct.CTkLabel(master=masterss,fg_color= '#ccffff',text="jumlah murid",anchor="e",justify = "right",width=60,font=self.font_nilai)
        
        self.nama.place(x=180, y=40)
        self.tingkat(x=180, y=70)
        self.wali.place(x=180, y=100)
        self.ketua.place(x=180, y=130)
        self.jumlah.place(x=180, y=160)

        self.nama_var = tk.StringVar()
        self.tingkat_var = tk.StringVar()
        self.wali_var = tk.StringVar()
        self.ketua_var = tk.StringVar()
        self.jumlah_var = tk.StringVar()

        self.entry_nama = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.nama_var, width = 400)
        self.entry_nama.place(x=250, y=40)
        self.entry_tingkat = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_var, width = 400)
        self.entry_tingkat.place(x=250, y=70)
        self.entry_wali = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.id_kelas_var, width = 400)
        self.entry_wali.place(x=250, y=100)
        self.entry_ketua = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.ketua_var, width = 400)
        self.entry_ketua.place(x=250, y=130)
        self.entry_jumlah = ct.CTkEntry(master=masterss, font=self.font_nilai, textvariable=self.jumlah_var, width = 400)
        self.entry_jumlah.place(x=250, y=160)

        self.columns = ('nama', 'tingkat', 'wali', 'ketua', 'jumlah')
        self.table = ttk.Treeview(master=masterss, columns=self.columns, show='headings', height=1000)
        self.table.heading('nama', text='nama kelas')
        self.table.column('nama', minwidth=0, width=60, stretch=False)
        self.table.heading('tingkat', text='tingkat kelas')
        self.table.column('tingkat', minwidth=0, width=100, stretch=False)
        self.table.heading('wali', text='wali kelas')
        self.table.column('wali', minwidth=0, width=60, stretch=False)
        self.table.heading('ketua', text='ketua kelas')
        self.table.column('ketua', minwidth=0, width=100, stretch=False)
        self.table.heading('jumlah', text='jumlah')
        self.table.column('jumlah', minwidth=0, width=80, stretch=False)

        self.table.place(x=140,y=250)

        self.button_save = ct.CTkButton(master= masterss, height=80, width=150, text='save', fg_color="0000FF", font=('montserrat',17), command=self.nambah_data)
        self.button_edit = ct.CTkButton(master= masterss, height=80, width=150, text='edit', fg_color="#ff7500", font=('montserrat',17), command=ubah_data)
        self.button_save.place(x=670, y=40)
        self.button_edit.place(x=670, y=80)

    def nambah_data(self):
        self.nambah_data_murid = "INSERT INTO kelas (`nama_kelas`, `tingkat_kelas`, `wali_kelas`, `ketua_kelas`, `jumlah`) VALUES ('+ nama','+ tingkat','+ wali','+ ketua','+ jumlah')"
        # result = self.curr.fetchone()
		# # print(result)
        self.conn.commit()
        self.data_show()

    def ubah_data(self, kelas, nama):
        self.ubah_data_murid = "UPDATE kelas SET (`nama_kelas`, `tingkat_kelas`, `wali_kelas`, `ketua_kelas`, `jumlah`) VALUES ('+ nama','+ tingkat','+ wali','+ ketua','+ jumlah'"
        self.curr.execute(self.ubah_data_murid, (kelas, nama))
		self.conn.commit()
        self.data_show()

    def data_show(self):
        sample = self.masuk
        for lama in self.table.get_children():
            self.table.delete(lama)
        for isi in sample:
            self.table.insert('', tkinter.END, values=isi[0:])
        return sample,isi
