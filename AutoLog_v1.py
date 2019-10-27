from tkinter import *
from tkinter import filedialog
from handwr_recog import handwr_recog
from process_info import process_info
from GDSY_input import GDSY_input
log_img = ''
API_key = 'API-key.json'
text_string = ''
db_file = ''

def chooseFile():
    global log_img
    log_img = filedialog.askopenfilename(parent=master, \
                                         initialdir= "/", \
                                         title='Select image file')
    Entry.insert(E1, 0, log_img)

def chooseFile2():
    global db_file
    db_file = filedialog.askopenfilename(parent=master, \
                                         initialdir= "/", \
                                         title='Select GEODASY database')
    Entry.insert(E2, 0, db_file)
    
def process():
    global text_string
    text_string = handwr_recog(API_key, log_img)
    Entry.insert(T1, "1.0", text_string)
    
def save():
    global text_string
    text_string = T1.get("1.0","end-1c")

def input_info():
    log_data = process_info(text_string)
    GDSY_input(db_file, log_data)
  
master = Tk()
master.geometry("450x600")
master.title("AutoLog_v1")

E1_label = Label(master, text="Image file:").place(x=20, y=25)
E1 = Entry(master, width=28)
E1.place(x=90, y=26)

selectfile_button1 = Button(master, text="Select file", \
                        command=chooseFile).place(x=275, y=22)
process_button = Button(master, text="Process", height=1, width=8,\
                        command=process).place(x=350, y=22)

T1 = Text(master, width=50, height=25)
T1.place(x=21, y=60)

save_button = Button(master, text="Save", \
                     command=save).place(x=21, y=470)

E2_label = Label(master, text="Database location:").place(x=20, y=510)
E2 = Entry(master, width=33)
E2.place(x=132, y=511)

selectfile_button2 = Button(master, text="Select file", \
                            command=chooseFile2).place(x=350, y=507)

input_button = Button(master, text="Input to GEODASY", \
                      command=input_info).place(x=304, y=550)
master.mainloop()

