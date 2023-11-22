#p
import time
import numpy as np

class nilai:
    def __init__(self, con,cur):
        self.con=con
        self.cur=cur
    def home(self):
        while True:
            a = int(input("selamat datang di page \"nilai\", mau lanjut ke menu mana? \n 1 = mencari murid \n  2 = mengubah nilai \n 9 = kembali \n:"))
            if a == 1:
                self.cari_murid()
            elif a == 2:
                self.mengubah_nilai_mana()
            elif a == 9:
                break
            else:
                print("Masukkan Pilihan yang Benar!!!")
                continue

    def mengubah_nilai_mana(self):
        a = int(input("selamat datang di page \"nilai\", mau lanjut ke menu mana? \n 1 = menngubah nilai tugas \n 2 = mengubah nilai ujian  \n 9 = kembali \n:"))
        if a == 1:
            self.mengubah_nilai_tugas()
        if a == 2:
            self.__mengubah_nilai_ujian()
        if a == 9:
            self.home()
    def cari_murid(self):
        id = int(input("silahkan masukan ID murid:"))
        a = 'SELECT * FROM `nilai` WHERE `id` = %s'
        self.cur.execute(a, id)
        result = cur.fetchall()
        print(result)
        repeat = int(input("cari murid lain? \n 1 = iya \n 9 = back to home \n 0 = tidak \n :"))

        if repeat == 1 :
            self.cari_murid()
            return repeat, id, a, result
        else:
            self.home()
            return repeat, id, a, result
    def mengubah_nilai_tugas(self):
        with self.con.cursor() as cur:
            id = int(input("silahkan masukan ID murid:"))
            perubahan_nilai_baru = float(input("nilai tugas yang baru:"))
            b = 'SELECT `nama`, `id` FROM `nilai` WHERE `id` = %s'
            cur.execute(b, id)
            result = cur.fetchall()
            print (result)
            confirmation = int(input("\n yakin mau diubah? \n 1 = iya \n 9 = kembali \n 0 = tidak \n :"))
            if confirmation == 1 :
                time.sleep(2)
            else:
                self.mengubah_nilai_mana()
                return id, perubahan_nilai_baru, b, result, confirmation
            a = 'UPDATE `nilai` SET `nilai_tugas` = %s WHERE `id` = %s'
            cur.execute(a, args= (perubahan_nilai_baru, id))
            self.con.commit()
            c = 'SELECT * FROM `nilai` WHERE `id` = %s'
            cur.execute(c, id)
            result2 = cur.fetchall()
            print (result2)
            self.nangkap_nilai_tugas(id)
            repeat = int(input("lanjut ubah nilai tugas murid lain? \n 1 = iya \n 0 = tidak \n :"))
            if repeat == 1 :
                self.mengubah_nilai_tugas()
                return repeat, id, perubahan_nilai_baru, a, b, c, result2, confirmation
            else:
                self.home()
                return repeat, id, perubahan_nilai_baru, a, b, c, result2, confirmation
    def __mengubah_nilai_ujian(self):
        with self.con.cursor() as cur:
            id = int(input("silahkan masukan ID murid:"))
            perubahan_nilai_baru = float(input("nilai ujian yang baru:"))
            b = 'SELECT `nama`, `id` FROM `nilai` WHERE `id` = %s'
            cur.execute(b, id)
            result = cur.fetchall()
            print (result)
            confirmation = int(input("\n yakin mau diubah? \n 1 = iya \n 9 = kembali \n 0 = tidak \n :"))
            if confirmation == 1 :
                time.sleep(2)
            else:
                self.mengubah_nilai_mana()
                return id, perubahan_nilai_baru, b, confirmation
            a = 'UPDATE `nilai` SET `nilai_ujian` = %s WHERE `id` = %s'
            cur.execute(a, args= (perubahan_nilai_baru, id))
            self.con.commit()
            c = 'SELECT * FROM `nilai` WHERE `id` = %s'
            cur.execute(c, id)
            result2 = cur.fetchall()
            print(result2)
            self.nangkap_nilai_tugas(id)
            repeat = int(input("lanjut ubah nilai ujian murid lain? \n 1 = iya \n 0 = tidak \n :"))
            if repeat == 1 :
                self.__mengubah_nilai_ujian()
                return repeat, id, perubahan_nilai_baru, a, b, c, result2, confirmation
            else:
                self.home()
                return repeat, id, perubahan_nilai_baru, a, b, c, result2, confirmation
    def nangkap_nilai_tugas(self, id2):
        with self.con.cursor() as cur:
            d = 'SELECT `nilai_tugas` FROM `nilai` WHERE `id` = %s'
            cur.execute(d, id2)
            e = cur.fetchone()
            nilai_e = e['nilai_tugas']
            print (nilai_e)
            self.nangkap_nilai_ujian(id2,nilai_e)
    def nangkap_nilai_ujian(self, id2, e):
        with self.con.cursor() as cur:
            f = 'SELECT `nilai_ujian` FROM `nilai` WHERE `id` = %s'
            cur.execute(f, id2) 
            g = cur.fetchone()
            nilai_g = g['nilai_ujian']
            print (nilai_g)
            self.ngitung_rata_rata(id2,e,nilai_g)
    def ngitung_rata_rata(self, id2,e,g):
        with self.con.cursor() as cur:
            i=np.mean([e,g])
            f = 'UPDATE `nilai` SET `rata_rata` = %s WHERE `id` = %s'
            cur.execute(f, args=(i,id2))
            self.con.commit()
            return e,g,h,i,f
