import subprocess
import time
import tkMessageBox
import ttk
import shutil
from threading import Thread
from Tkinter import *
from shutil import copyfile


import tkFont





root = Tk()

helv36 = tkFont.Font(family='Helvetica',size=15, weight='bold')
        
root.grid_propagate(False)
root.title("simple GUI")
root.geometry("500x500")
#this property is nod defined in doc, wtf
root.resizable(width = False,height = False)


def thread_index():
    global is_running
    is_running = 1
    print("Thread sleeping")
    button_index.config(state=DISABLED)  
    a = int(page_from.get()) + int(page_to.get())
    print(a)
    time.sleep(10);
    print("Thread finished")
    button_index.config(state=NORMAL)
    is_running = 0

def thread_stat():
    is_running = 1
    button_stat.config(state=DISABLED) 
    try:
        time.sleep(1);
        stat()
        print("Stat thread finished")
        is_running = 0
    except :
        is_running = 0
        button_stat.config(state=NORMAL)
        print("Stat thread finished with exception")
        raise
    
def thread_copyfile():
	print("copying file");
	pb.start()
	time.sleep(1)
	try:
		copyfile("c:\\dira\\test_file.txt","c:\\dirb\\testfile.txt");
		pb.stop()
	except IOError:
		print ("CopyFile raised exception: File not found");
		pb.stop()
		
def callback_index():
    thread = Thread(target = thread_index)
    thread.start();
	


def callback_stat():
    thread = Thread(target = thread_stat)
    thread.start();


def callback_copyfile():
	thread = Thread(target = thread_copyfile)
	thread.start();
	
def on_closing():
    global is_running
    if is_running == 1 :
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
        else:
            return
    else:
        root.destroy()
#def callback_donwload():
    
#def callback_stat():
    
is_running = 0;	
page_from = Entry(root)
page_from.grid(row = 0,column = 0,pady = 10,padx = 10)
page_from.insert(END, '1')
page_to = Entry(root)
page_to.grid(row = 1,column = 0,pady = 10,padx = 10)
page_to.insert(END, '2')

button_index = Button(root, text="Index", command=callback_index)
button_index.grid(row = 2,pady = 5)
button_download = Button(root, text="Download", command=callback_index)
button_download.grid(row = 3,pady = 5)
button_stat = Button(root, text="Stat", command=callback_stat)
button_stat.grid(row = 4,pady = 5)

button_stat = Button(root, text="CopyFile", command=callback_copyfile)
button_stat.grid(row = 6,pady = 5)

pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate",maximum = 100)
pb.grid(row = 5,padx = 10,pady = 10);


#var  = StringVar()
#m1 = Message(root,width=100,textvariable = var,relief = RAISED).grid(row=1,column = 0,columnspan = 2,sticky = W)

# text widget is not used, using console window as output
#fr = Frame(root,width = 400,height = 200)
#fr.grid_propagate(False)
#fr.grid(row=2,column = 0,columnspan=3)
#T = Text(fr,font=helv36)
#T.insert(END, "J\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\nJ\n")
#T.config(state=DISABLED)
#T.grid(row=2,column = 0)

#var.set("hi, this is a text message")
#use rowspan columnspan
#http://stackoverflow.com/questions/23304403/tkinter-grid-columnspan-ignored



root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()