from tkinter import * 
import time 
def clock():
    current_time=time.strftime("%I:%M:%S %p")
    clock_lbl['text']=current_time 
    clock_lbl.after(200,clock )
root=Tk()
root.title("Digital Clock")
root.resizable(0,0)
current_time=time.strftime("%I:%M:%S %p")
clock_lbl=Label(root,font=('berlin 80'),text=current_time)
clock_lbl.pack()
clock()
root.mainloop()

