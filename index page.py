#Author@ikotuncollins1


from tkinter import *

#style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).

screen = Tk()
screen.geometry("700x500")
screen.resizable(width=FALSE,height=FALSE)
screen.title("Data Visualizer")
screen.config(bg="skyblue")
label1 = Label(screen,text="DV1.01")
label1.config(bg="sky blue")
label1.pack()       

#label1.grid_rowconfigure(1, weight=1)
#label1.grid_columnconfigure(1, weight=1)
label2 = Label(screen, text="SELECT AN OPTION TO OPERATE", font=('cred', 14))
label2.config(bg="sky blue")
label2.pack()
#label2.grid_rowconfigure(1, weight=1)
#label2.grid_columnconfigure(1, weight=1)

############################################################################3
###############GRAPH FUNCTION##############################33################
#############################################################################

val = []
def graphFunc():
    graphButton1 = Tk()
    graphButton1.geometry("300x300")
    graphButton1.resizable(FALSE,FALSE)


    xentry = Label(graphButton1, text="Enter Values for X coordinate")
    
    xentry.pack()

    #def val1get():
     #   val1.get()
      #  val1val = val1.get
       # print(val1val)


    val1 = Entry(graphButton1)
    val1.pack()
    val2 = Entry(graphButton1)
    val2.pack()
    val3 = Entry(graphButton1)
    val3.pack()
    val4 = Entry(graphButton1)
    val4.pack()
    val5 = Entry(graphButton1)
    val5.pack()
    val6 = Entry(graphButton1)
    val6.pack()
    val7 = Entry(graphButton1)
    val7.pack()
    val8 = Entry(graphButton1)
    val8.pack()
    #z = Label(graphbutton1, text="X axis Title")
    #z.pack()

    val9 = Entry(graphButton1)
    val9.pack()

    def getInput():
        a = int(val1.get())
        b = int(val2.get())
        c = int(val3.get())
        d = int(val4.get())
        e = int(val5.get())
        f = int(val6.get())
        g = int(val7.get())
        h = int(val8.get())
        global p
        p = str(val9.get())
        graphButton1.destroy()

        global val
        val = [a,b,c,d,e,f,g,h]
        print(val)

    Xbutton = Button(graphButton1, text="X-append", command=getInput)
    Xbutton.pack()


    graphButton1.mainloop()


graphButton = Button(screen, text="Generate Graph - X axis info", command=graphFunc)  
graphButton.pack(ipady=9)
graphButton.config(bg="gray")
############################################################################################
###########################Y---XIS#####################################################
valY = []

def graphFuncY():
    graphButton1 = Tk()
    graphButton1.geometry("300x300")
    graphButton1.resizable(FALSE,FALSE)


    yentry = Label(graphButton1, text="Enter Values for Y coordinate")
    
    yentry.pack()

    #def val1get():
     #   val1.get()
      #  val1val = val1.get
       # print(val1val)


    val1 = Entry(graphButton1)
    val1.pack()
    val2 = Entry(graphButton1)
    val2.pack()
    val3 = Entry(graphButton1)
    val3.pack()
    val4 = Entry(graphButton1)
    val4.pack()
    val5 = Entry(graphButton1)
    val5.pack()
    val6 = Entry(graphButton1)
    val6.pack()
    val7 = Entry(graphButton1)
    val7.pack()
    val8 = Entry(graphButton1)
    val8.pack()
    val9 = Entry(graphButton1)
    val9.pack()


    def getInputY():
        a = int(val1.get())
        b = int(val2.get())
        c = int(val3.get())
        d = int(val4.get())
        e = int(val5.get())
        f = int(val6.get())
        g = int(val7.get())
        h = int(val8.get())

        global i
        i = str(val9.get())

        graphButton1.destroy()

        global valY
        valY = [a,b,c,d,e,f,g,h]
        print(valY)

    ybutton = Button(graphButton1, text="Y-append", command=getInputY)
    ybutton.pack()
    graphButton1.mainloop()


graphButton2 = Button(screen, text="Generate Graph - Y Axis info", command=graphFuncY)  
graphButton2.pack(ipady=9)

def linearGraph():
    import matplotlib.pyplot as plt
    plt.plot(val,valY)
    plt.ylabel(i)
    plt.xlabel(p)
    ax = plt.axes()
    ax.set_facecolor("violet")
    #val.title(" MAFO")
    plt.plot(val,valY)
    plt.show()

Execute = Button(screen, text="Show Linear graph", command=linearGraph)
Execute.pack()

def accessExcel():
    Excel = Button(screen, text="Access Excel Data", command=NONE)
    Excel.pack()


#LEARN How to CODE PROPERLY you dummy

screen.mainloop()


