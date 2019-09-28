import tkinter
import tkinter.messagebox
import send_message

def showWin():
    win=tkinter.Tk();
    win.title("SendMessage")
    win.geometry("500x300+500+100")
    # button exit
    buttonExit = tkinter.Button(win,text="Quit",command=win.quit)
    buttonExit.place(x=350, y=250, width=100, height=20)
    # lable sqs_queue_url
    labelUrl = tkinter.Label(win,text="sqs_queue_url:",font=("黑体", 15))
    labelUrl.place(x=50, y=50, width=100, height=20)
    # title Send Messages
    labelTitle = tkinter.Label(win,text="Send Messages",font=("黑体", 26))
    labelTitle.place(x=150, y=15, width=200, height=30)
    # Entry inputUrlpip install ipython
    inputUrl = tkinter.Variable()
    entryUrl = tkinter.Entry(win, textvariable=inputUrl)
    inputUrl.set("default")
    entryUrl.place(x=160, y=50, width=300, height=20)
    # button ok
    def getUrl():
        print(inputUrl.get())
        print(textInput.get(0.0,'end'))
        send_message.send(inputUrl.get(),textInput.get(0.0,'end'))
        tkinter.messagebox.showinfo('Prompt', 'Sent successfully!')

    buttonOK = tkinter.Button(win,text="OK",command=getUrl)
    buttonOK.place(x=50, y=250, width=100, height=20)
    # lable message
    labelShow = tkinter.Label(win,text="Show Message:",font=("黑体", 15))
    labelShow.place(x=30, y=80, width=150, height=20)
    # text message
    textInput=tkinter.Text(win,width = 57,height = 8)
    textInput.place(x=50, y=110)
    scroll = tkinter.Scrollbar()
    scroll.place(x=460,y=110,height=125)
    scroll.config(command=textInput.yview)
    textInput.config(yscrollcommand=scroll.set)

    # button clear
    def clear():
        textInput.delete(0.0, 'end')
    buttonClear = tkinter.Button(win,text="Clear",command=clear)
    buttonClear.place(x=200, y=250, width=100, height=20)

    win.mainloop();

showWin()

