from tkinter import *

from CheckBox import showWindow, showCheckBox
from ConfigReader import configReader

# 初始化Tk()
from OpenSoft import openSofts

myFrame = Tk()
# 设置标题
myFrame.title("打开软件")
# 设置窗口大小
width = 380
height = 300
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myFrame.winfo_screenwidth()
# 这里将位置稍作抬高,以避免窗口内容过低
screenheight = myFrame.winfo_screenheight() - 300
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myFrame.geometry(alignstr)
# 设置窗口是否可变长、宽，True：可变，False：不可变
myFrame.resizable(width=False, height=True)

# 获取软件列表
d = configReader()

# 添加和打开按钮
Button(myFrame, text='添加软件', command = showWindow).pack(anchor="n")
# tkinter要求command的函数不应含有参数,若需要带有参数应当以lambda形式回调
# temp = d
Button(myFrame, text='查看列表', command = lambda: showCheckBox(myFrame, **d)).pack(anchor="n")

openSoft = Button(myFrame, text='打开软件', command=lambda: openSofts(**d)).pack(anchor="n")

# 进入消息循环
myFrame.mainloop()
