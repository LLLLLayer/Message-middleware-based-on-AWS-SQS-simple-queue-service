import tkinter
import tkinter.messagebox
import receive_message

def showWin():
    win=tkinter.Tk();
    win.title("ShowMessage")
    win.geometry("500x300+500+100")
    # button exit
    buttonExit = tkinter.Button(win,text="Quit",command=win.quit)
    buttonExit.place(x=350, y=260, width=100, height=20)
    # title Send Messages
    labelTitle = tkinter.Label(win,text="Show Messages",font=("黑体", 26))
    labelTitle.place(x=150, y=15, width=200, height=30)

    # lable sqs_queue_url
    labelUrl = tkinter.Label(win,text="sqs_queue_url:",font=("黑体", 15))
    labelUrl.place(x=50, y=50, width=100, height=20)
    # Entry inputUrl
    inputUrl = tkinter.Variable()
    entryUrl = tkinter.Entry(win, textvariable=inputUrl)
    inputUrl.set("default")
    entryUrl.place(x=160, y=50, width=300, height=20)

    # lable num_msgs
    labelNum = tkinter.Label(win,text="um_msgs:",font=("黑体", 15))
    labelNum.place(x=50, y=75, width=100, height=20)
    # Entry inputUrl
    inputNum = tkinter.Variable()
    entryNum = tkinter.Entry(win, textvariable=inputNum)
    inputNum.set("1")
    entryNum.place(x=160, y=75, width=300, height=20)

    # lable wait_time
    labelWait = tkinter.Label(win,text="wait_time:",font=("黑体", 15))
    labelWait.place(x=50, y=100, width=100, height=20)
    # Entry inputWait
    inputWait = tkinter.Variable()
    entryWait = tkinter.Entry(win, textvariable=inputWait)
    inputWait.set("0")
    entryWait.place(x=160, y=100, width=300, height=20)

    # lable visibility_time
    labelVis = tkinter.Label(win,text="visibility_time:",font=("黑体", 15))
    labelVis.place(x=50, y=125, width=100, height=20)
    # Entry inputWait
    inputVis = tkinter.Variable()
    entryVis = tkinter.Entry(win, textvariable=inputVis)
    inputVis.set("5")
    entryVis.place(x=160, y=125, width=300, height=20)

    # lable message
    labelShow = tkinter.Label(win,text="Show Message:",font=("黑体", 15))
    labelShow.place(x=30, y=150, width=150, height=20)
    # text message
    textInput=tkinter.Text(win,width = 57,height = 5)
    textInput.place(x=50, y=170)
    scroll = tkinter.Scrollbar()
    scroll.place(x=460,y=170,height=80)
    scroll.config(command=textInput.yview)
    textInput.config(yscrollcommand=scroll.set)

    # button ok
    def func():
        str=receive_message.receive(inputUrl.get(),int(inputNum.get()),int(inputWait.get()),int(inputVis.get()))
        tkinter.messagebox.showinfo('Prompt', 'Send successfully!')
        if str=="":
            textInput.insert(tkinter.INSERT, 'No news yet!')
        textInput.insert(tkinter.INSERT,str)

    buttonOK = tkinter.Button(win,text="OK",command=func)
    buttonOK.place(x=50, y=260, width=100, height=20)

    # button clear
    def clear():
        textInput.delete(0.0, 'end')
    buttonClear = tkinter.Button(win,text="Clear",command=clear)
    buttonClear.place(x=200, y=260, width=100, height=20)

    win.mainloop();

showWin()

