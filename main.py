from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from work import Work
from data import Data


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    path = ""
    def loginBtn(self):
        jump = db.load(x=self.email.text)
        self.path = jump[3]

        if len(jump) != 0:
            if jump[2] != self.password.text:
                pop = Popup(title='Invalid Login',
                            content=Label(text='Invalid username or password.'),
                            size_hint=(None, None), size=(400, 400))
                pop.open()
            else:
                self.email.text
                self.email.text = ""
                self.password.text = ""
                sm.current = "menu"
        else:
            pop = Popup(title='Invalid Login',
                        content=Label(text='Invalid username or password.'),
                        size_hint=(None, None), size=(400, 400))
            pop.open()

    def createBtn(self):
        self.email.text = ""
        self.password.text = ""
        sm.current = "create"





class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        sm.current = "login"

    def createBtn(self):
        n = self.namee.text
        email = self.email.text
        password = self.password.text
        wk = self.namee.text + ".xlsx"

        l = [email, n, password, wk]

        Work.create_worksheet(wk)

        db.addEntry(l)

        self.namee.text = ""
        self.email.text = ""
        self.password.text = ""
        sm.current = "login"


class Menu(Screen):

    def addExpenseBt(self):
        sm.current = "takeE"

    def addIncomeBt(self):
        sm.current = "takeI"

    def sumExpenseBt(self):
        sm.current = "showE"

    def sumIncomeBt(self):
        sm.current = "showI"

    def remaingBt(self):
        sm.current = "rem"

    def reset(self):
        sm.current = "res"

    def backBt(self):
        sm.current = "login"


class Rem(Screen):
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        sum = wk.remaning(jump[3])
        pop = Popup(title='Invalid Login',
                            content=Label(text=f'Sum of Expenses: {sum}'),
                            size_hint=(None, None), size=(400, 400))
        pop.open()

    def backBtn(self):
        self.email.text = ""
        sm.current = "menu"


class ShowE(Screen):
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        sum = wk.sumOfExpense(jump[3])
        pop = Popup(title='Invalid Login',
                            content=Label(text=f'Sum of Expenses: {sum}'),
                            size_hint=(None, None), size=(400, 400))
        pop.open()

    def backBtn(self):
        self.email.text = ""
        sm.current = "menu"

class ShowI(Screen):
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        sum = wk.sumOfIncome(jump[3])
        pop = Popup(title='Invalid Login',
                            content=Label(text=f'Sum of Incomes: {sum}'),
                            size_hint=(None, None), size=(400, 400))
        pop.open()

    def backBtn(self):
        self.email.text = ""
        sm.current = "menu"


class TakeE(Screen):
    amt = ObjectProperty(None)
    appli = ObjectProperty(None)
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        e = jump[3]
        print(f"{self.amt.text} will be saved in {jump[3]}")
        wk.addexpense(amt=self.amt.text, name=self.appli.text, filename=jump[3])

    def backBtn(self):
        self.amt.text = ""
        self.appli.text = ""
        sm.current = "menu"


class TakeI(Screen):
    amt = ObjectProperty(None)
    sou = ObjectProperty(None)
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        e = jump[3]
        print(f"{self.amt.text} will be saved in {jump[3]}")
        wk.addincome(amt=self.amt.text, name=self.sou.text, filename=jump[3])

    def backBtn(self):
        self.amt.text = ""
        self.sou.text = ""
        sm.current = "menu"


class Res(Screen):
    email = ObjectProperty(None)

    def submitBtn(self):
        jump = db.load(x=self.email.text)
        wk.reset(jump[3])

    def backBtn(self):
        self.email.text = ""
        sm.current = "menu"


class WindowManager(ScreenManager):
    pass


global E
kv = Builder.load_file("gui.kv")
sm = WindowManager()
db = Data(" ")
wk = Work(" ")
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), Menu(name="menu"), Res(name="res"), ShowE(name="showE"), ShowI(name="showI") , ShowI(name="showI"), Rem(name="rem"), TakeE(name="takeE"), TakeI(name="takeI")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
