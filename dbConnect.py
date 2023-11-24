import pymysql
class mainDB:
    print("Login")

    def connect(self):
        while True:
            try:
                username = str(input("Username: "))
                passwords = str(input("Password: "))
                con = pymysql.connect(host='database-myschool.ciqnmiwbcceb.us-east-1.rds.amazonaws.com', port=3306,

                                      user=username,
                                      password=passwords,
                                      database="siswa",

                                      )
                cur = con.cursor()
                return con, cur


            except:
                print("Username atau Password Salah!!!")
                continue

