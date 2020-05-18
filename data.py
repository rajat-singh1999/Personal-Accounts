import datetime
import sqlite3


class Data:
    def __init__(self, email):
        self.email = email

    def load(self, x):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        self.email = x
        row = cur.execute('Select * from user where email = :email', {'email': self.email})
        k = []
        for i in row:
            for j in i:
                k.append(j)
        return k
    def addEntry(self, x):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        with conn:
            cur.execute('INSERT INTO user VALUES(:a, :b, :c, :d)', {'a': x[0], 'b': x[1], 'c': x[2], 'd': x[3]})
        conn.commit()
    # def get_user(self, email):
    #     if email in self.users:
    #         return self.users[email]
    #     else:
    #         return -1
    #
    # def add_user(self, email, password, name):
    #     if email.strip() not in self.users:
    #         self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
    #         self.save()
    #         return 1
    #     else:
    #         print("Email exists already")
    #         return -1
    #
    # def validate(self, email, password):
    #     if self.get_user(email) != -1:
    #         return self.users[email][0] == password
    #     else:
    #         return False
    #
    # def save(self):
    #     with open(self.filename, "w") as f:
    #         for user in self.users:
    #             f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
    #
    # @staticmethod
    # def get_date():
    #     return str(datetime.datetime.now()).split(" ")[0]
