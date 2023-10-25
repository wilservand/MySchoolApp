import pymysql
class mainDB:
    print("Login")

    def connect(self):
        while True:
            try:
                username = str(input("Username: "))
                passwords = str(input("Password: "))
                con = pymysql.connect(host='localhost',
                                      user=username,
                                      password=passwords,
                                      database='siswa',
                                      )
                cur = con.cursor()
                return con, cur

            except:
                print("Username atau Password Salah!!!")
                continue

