import tkinter as tk
from tkinter import messagebox,ttk
import customtkinter as ct


class Nilai (ct.CTkFrame):
    def __init__(self, curr, conn):
        self.curr = curr
        self.conn = conn
        self.setup_ui()

    def setup_ui(self):
        
        self.nama = ct.CTkLabel(master=self,fg_color= '#ccffff', text="nama murid",anchor="e",justify = "right",width=60)
        self.font_nilai = ct.CTkFont('montserrat',15)
        self.nama.configure(font=self.font_nilai)
        self.id = ct.CTkLabel(master=self,fg_color= '#ccffff',text="id murid",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.id_kelas = ct.CTkLabel(master=self,fg_color= '#ccffff',text="id kelas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.id_matkul = ct.CTkLabel(master=self,fg_color= '#ccffff',text="matkul",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.nilai_tugas = ct.CTkLabel(master=self,fg_color= '#ccffff',text="nilai tugas",anchor="e",justify = "right",width=60,font=self.font_nilai)
        self.nilai_ujian = ct.CTkLabel(master=self,fg_color= '#ccffff',text="nilai ujian",anchor="e",justify = "right",width=60,font=self.font_nilai)
        #self.nilai_rata_rata = ct.CTkLabel(master=self,fg_color= '#ccffff',text="rata-rata",anchor="e",justify = "right",width=110,font=('montserrat',17))
        
        self.nama.place(x=180, y=40)
        self.id.place(x=180, y=70)
        self.id_kelas.place(x=180, y=100)
        self.id_matkul.place(x=180, y=130)
        self.nilai_tugas.place(x=180, y=160)
        self.nilai_ujian.place(x=180, y=190)
        #self.nilai_rata_rata.place(x=285, y=340)

        self.entry_nama = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.nama_var, width = 400)
        self.entry_nama.place(x=250, y=40)
        #printing_nama = str(self.nama_var.get())
        #self.label_nama = ct.CTkLabel(master=self, text = printing_nama, font=('montserrat',17))
        #self.label_nama.place(x=405, y=130)
        self.entry_id = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.id_var, width = 400)
        self.entry_id.place(x=250, y=70)
        #printing_id = str(self.id_var.get())
        ##self.label_id = ct.CTkLabel(master=self, text = printing_id, font=('montserrat',17))
        #self.label_id.place(x=405, y=130)
        self.entry_id_kelas = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.id_kelas_var, width = 400)
        self.entry_id_kelas.place(x=250, y=100)
        self.entry_id_matkul = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.id_matkul_var, width = 400)
        self.entry_id_matkul.place(x=250, y=130)
        self.entry_nilai_tugas = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.nilai_tugas_var, width = 400)
        self.entry_nilai_tugas.place(x=250, y=160)
        self.entry_nilai_ujian = ct.CTkEntry(master=self, font=self.font_nilai, textvariable=self.nilai_ujian_var, width = 400)
        self.entry_nilai_ujian.place(x=250, y=190)

        columns = ('id', 'nama', 'kelas', 'matkul', 'nilai tugas', 'nilai ujian', 'rata-rata')
        self.table = ttk.Treeview(master=self, columns=columns, show='headings', height=1000)
        self.table.heading('id', text='ID')
        self.table.heading('nama', text='Nama')
        self.table.heading('kelas', text='Kelas')
        self.table.heading('matkul', text='Matkul')
        self.table.heading('nilai tugas', text='Nilai Tugas')
        self.table.heading('nilai ujian', text='Nilai Ujian')
        self.table.heading('rata-rata', text='Rata-Rata')
        self.table.place(x=140,y=250)

        self.button_cari = ct.CTkButton(master= self, height=80, width=150, text='cari', fg_color="#00df00", font=('montserrat',17), command=lambda: self.execute_cari())
        self.button_ubah = ct.CTkButton(master= self, height=80, width=150, text='ubah', fg_color="#ff7500", font=('montserrat',17))
        self.button_cari.place(x=670, y=40)
        self.button_ubah.place(x=670, y=140)

    def execute_cari(self):
        self.execute_cari_id = 'SELECT DISTINCT siswa.data_siswa.nis, siswa.data_siswa.nama, siswa.data_siswa.kelas, siswa.mata_pelajaran.mataPelajaran FROM nilai LEFT JOIN siswa.data_siswa ON %s = siswa.data_siswa.nis LEFT JOIN siswa.mata_pelajaran ON %s = siswa.mata_pelajaran.mataPelajaran'
    
        self.curr.execute(self.execute_cari_id, args=(self.entry_id.get(), self.entry_id_matkul.get()))
        self.kasar = self.curr.fetchall()
        self.data_show()

    def konfirmasi_murid(self):
        self.apakah_ada = 'SELECT siswa.data_siswa.nis FROM siswa.nilai WHERE siswa.nilai.nis = %s'
        self.curr.execute(self.apakah_ada, args=(self.entry_id.get()))
        self.belum = self.curr.fetchall()
        for a in self.belum:
            if self.entry_id.get() == a:
                continue
            else:
                self.murid_tidak_ada = messagebox.showerror("error", "Murid Tidak Ada")

    #def nambah_data(self):

    #def ubah_nilai_ujian(self):
        #self.mengubah_nilai = 'UPDATE siswa.nilai SET nilai_ujian = %s WHERE siswa.nilai.nis = %s'
        #self.curr.execute(self.mengubah_nilai, args=(self.entry_nilai_ujian.get(), self.entry_id.get()))

    #def murid_tidak_ada(self):


    def data_show(self):
        sample = self.kasar
        for lama in self.table.get_children():
            self.table.delete(lama)
        for isi in sample:
            self.table.insert('', tkinter.END, values=isi[0:])
        return sample,isi

    def item_selected(event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


        self.table.bind('<<TreeviewSelect>>', item_selected)
    
