__author__ = 'PirminVDB'
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        master.config(menu=self.get_menu())

        self.label = tk.Label(self)
        self.label["text"] = 0
        self.label.pack(side="left")

        self.button = tk.Button(self)
        self.button["text"] = "Click me!"
        self.button["command"] = lambda:self.button_clicked(self.label)
        self.button.pack(side="left")

        self.quit_button = tk.Button(self)
        self.quit_button["text"] = "QUIT"
        self.quit_button["fg"] = "red"
        self.quit_button["command"] = root.destroy
        self.quit_button.pack(side="bottom")

    def button_clicked(self, label):
        self.label["text"] += 1

    def donothing(self):
        print("tekst")

    def about(self):
        print("this is the about")
        """
        about_window = tk.Tk()
        temp = tk.Label(self)
        temp["text"] = 0
        temp.pack(side="left")
        about_window.mainloop()
        """

    def get_menu(self):
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        return menubar

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()