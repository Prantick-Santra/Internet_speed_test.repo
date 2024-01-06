from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up=str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp=Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="light grey")

lab=Label(sp, text="Internet Speed Test", font=("Time New Roman",28,"bold"))
lab.place(x=40,y=40,height=30,width=420)

lab=Label(sp, text="Download Speed", font=("Time New Roman",25,"bold"))
lab.place(x=40,y=120,height=30,width=420)

lab_down=Label(sp, text="00", font=("Time New Roman",28,"bold"))
lab_down.place(x=40,y=180,height=30,width=420)

lab=Label(sp, text="Upload Speed", font=("Time New Roman",25,"bold"))
lab.place(x=40,y=240,height=30,width=420)

lab_up=Label(sp, text="00", font=("Time New Roman",28,"bold"))
lab_up.place(x=40,y=320,height=30,width=420)

button=Button(sp,text="Check Speed", font=("Time New Roman",25,"bold"), relief=RAISED,bg="light blue",command=speedcheck)
button.place(x=40,y=400,height=30,width=420)

sp.mainloop()

