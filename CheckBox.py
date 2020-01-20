from tkinter import*

from ButtonControl import changeVal
from ConfigReader import configAppend


def showWindow():
    #初始化Tk()
    myWindow = Tk()
    #设置标题
    myWindow.title('添加软件')
    #标签控件布局
    Label(myWindow, text="软件名称").grid(row=0)
    Label(myWindow, text="完整路径").grid(row=1)
    #Entry控件布局
    entry1=Entry(myWindow)
    entry2=Entry(myWindow)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    Button(myWindow, text='添加', command = lambda : configAppend(entry1.get(),entry2.get())).grid(row=2, column=0,sticky=W, padx=10, pady=10)
    Button(myWindow, text='取消', command=None).grid(row=2, column=1, sticky=W, padx=10, pady=10)

    #进入消息循环
    myWindow.mainloop()


# showWindow()

def showCheckBox(frame, **d):
    # 初始化Tk()
    myWindow2 = Tk()
    # 设置标题
    myWindow2.title('添加软件')

    # 进入消息循环
    boxValue = {}
    for k in d.keys():
        val = IntVar
        Checkbutton(myWindow2, text = k, command = lambda : changeVal(val), variable = val).pack()
        # boxValue[k] = val
    # return boxValue
    myWindow2.mainloop()


