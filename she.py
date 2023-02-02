import tkinter.filedialog  # 注意次数要将文件对话框导入
from tkinter import filedialog, Label, Entry, Button, Tk
from tkinter.constants import RAISED
import time
import threading
from apscheduler.schedulers.blocking import BlockingScheduler


class she_clazz:
    file_path = ''


def AddProduct():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')
    if selectFileName != '':
        lb.config(text=selectFileName)
        she_cla.file_path = str(selectFileName)
    else:
        lb.config(text='您没有选择任何文件')
        she_cla.file_path = ''


def she():
    t = threading.Thread(target=she_file)
    t.start()


def she_file():
    sched = BlockingScheduler()
    sched.add_job(action, 'interval', seconds=120)
    sched.start()


def action():
    file = open(she_cla.file_path, mode='w')
    timeResTime = time.time()
    file.write(str(timeResTime))
    file.close()


she_cla = she_clazz()

root = Tk()
root.config(bg='#87CEEB')
root.title("定时读取文件小工具")
root.geometry('250x120')
btn = Button(root, text='选择文件', relief=RAISED, command=AddProduct)
btn.grid(row=1, column=0)

lb = Label(root, text='', bg='#87CEEB')
lb.grid(row=1, column=1, padx=5, pady=10)
Button(root, text='执行', command=she, width=15).grid(row=2, column=0, padx=10,
                                                    pady=10)
path_var = tkinter.StringVar()
# 显示窗口
root.mainloop()
