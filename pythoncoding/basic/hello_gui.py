# 导入TKinter包的所有内容
from tkinter import *
import tkinter.messagebox as messagebox

# 从Frame派生一个Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)
# 实例化Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()