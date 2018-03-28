# -*-coding:utf-8-*-
from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = Label(self, text='Hello, world!')
        self.hello_label.pack()
        self.quit_button = Button(self, text='Quit', command=self.quit)
        self.quit_button.pack()

app = Application()
# 窗口标题:
app.master.title('Hello World')
# 窗口大小
app.master.geometry('800x600')
# 主消息循环:
app.mainloop()