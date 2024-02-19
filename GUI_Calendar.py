from tkinter import *
from tkcalendar import *
import datetime


a_root = Tk()
a_root.title("My Calendar")
# a_root.wm_iconbitmap("your_icon_image.ico")
a_root.geometry("370x260")


current_date = datetime.datetime.now()
d1 = current_date.year
d2 = current_date.month
d3 = current_date.day
c = Calendar(a_root, font="Arial 16", cursor="hand1", selectmode="day", year=d1, month=d2, day=d3)
c.pack(fill="both", expand=True)


a_root.mainloop()
