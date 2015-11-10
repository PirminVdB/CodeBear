__author__ = 'PirminVDB'
import tkinter as tk
import APPS.MVC as MVC

class SommatieScherm(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.addButton = tk.Button(self, text='Add', width=8)
        self.addButton.pack(side='left')
        self.removeButton = tk.Button(self, text='Remove', width=8)
        self.removeButton.pack(side='left')

class HoofdScherm(tk.Toplevel, MVC.ChangeListener):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My Money').pack(side='left')
        self.moneyCtrl = tk.Entry(self, width=8)
        self.moneyCtrl.pack(side='left')

    def SetMoney(self, money):
        self.moneyCtrl.delete(0,'end')
        self.moneyCtrl.insert('end', str(money))

    def state_changed(self, change_event):
        self.SetMoney(change_event.get_model().getMoney())

class PrintScherm(MVC.ChangeListener):
    def __init__(self):
        pass

    def state_changed(self, change_event):
        print("Geld " + str(change_event.get_model().getMoney()))

class Model(MVC.Model):
    def __init__(self):
        super().__init__()
        self.Money = 0
        pass

    def addMoney(self, value):
        self.Money += value
        self._fire_state_changed()

    def removeMoney(self, value):
        self.Money -= value
        self._fire_state_changed()

    def getMoney(self):
        return self.Money

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.hoofdscherm = HoofdScherm(root)
        self.model.add_change_listener("hoofdscherm", self.hoofdscherm)
        self.hoofdscherm2 = HoofdScherm(root)
        self.model.add_change_listener("hoofdscherm2", self.hoofdscherm2)
        self.printscherm = PrintScherm()
        self.model.add_change_listener("printscherm", self.printscherm)
        self.sommatiescherm = SommatieScherm(self.hoofdscherm)
        self.sommatiescherm.addButton.config(command=self.AddMoney)
        self.sommatiescherm.removeButton.config(command=self.RemoveMoney)
        #self.MoneyChanged(self.model.myMoney.get())

    def AddMoney(self):
        self.model.addMoney(10)

    def RemoveMoney(self):
        self.model.removeMoney(10)

    """def MoneyChanged(self, money):
        self.hoofdscherm.SetMoney(money)"""

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()