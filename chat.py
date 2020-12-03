from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import json



data = json.load(open('data.json'))
low = dict((k.lower() if isinstance(k, str) else k, v.lower() if isinstance(v, str) else v) for k,v in data.items())



# Create send function
def send():
    current = time.strftime('%H:%M:%S')
    global window,e
    match = e.get()
    sen = e.get().lower()
    if (sen == "hi" or sen == "hey" or sen == "hello" or sen == "hii" or sen == "hiiiiiiiiiiiiiii" or sen == "hiii" or sen == "heyy" or sen == "heyyy" or sen == "heyyyyyyyyyyyyyyy" or sen == "hlo" or sen == "helo" or sen == "heloo") :
        window.insert(END, "  ")
        window.insert(END,"You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END,"Bot : " + "Hello!!" + ".")

    elif (sen == "how are you?" or sen == "how are you.." or sen == "how are you" or sen == "hii" or sen == "how are you." or sen == "how are u?" or sen == "how are u.." or sen == "how are u." or sen == "how are u" or sen == "how r u.." or sen == "how r you." or sen == "how r u?" or sen == "how r you?" or sen == "how r u") :
        window.insert(END, "  ")
        window.insert(END,"You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END,"Bot : " + "I am fine" + "." + "What about you ?")


    elif (sen == "Fine" or sen == "fine." or sen == "Fine." or sen == "fine"):
        window.insert(END, "  ")
        window.insert(END, "You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END, "Bot : " + "Good to hear this!!" + " :)")

    elif (sen == "What is the time now?" or sen == "time?" or sen == "time." or sen == "time" or sen == "Time" or sen == "What is the time now" or sen == "What is the time" or sen == "What is the current time?" or sen == "What is the current time" or sen == "Current time" or sen == "Current time." or sen == "Current time?" or sen == "Current Time" or sen == "Current Time?" or sen == "current time" or sen == "current time?") :
        window.insert(END, "  ")
        window.insert(END,"You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END,"Bot : " + "This is current time " + " " + current + ".")

    elif(match in low):
        window.insert(END, "  ")
        window.insert(END,"You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END, "Bot : " + str(low[match]))

    elif (sen == "bye") :
        window.insert(END, "  ")
        window.insert(END,"You : " + e.get().capitalize())
        window.insert(END, "  ")
        window.insert(END,"Bot : " + "Bye!!" + "." )

    else:
        window.insert(END, "  ")
        window.insert(END, "Bot : " + "Sorry!! I can't recognize!!" + " :(")




    e.delete(0,'end')

# Create save function
def save():
    fd = filedialog.asksaveasfilename(initialdir = 'C:/Users/sanju/Desktop',title = "Save",filetypes=(("All Files", "*.*"),))

# Create delt function
def delt():
    window.delete(ANCHOR)

# Create clear function
def clear():
    window.delete(0,END)

# Create abt function
def abt():
    msg = messagebox.showinfo("About Us","This is a bot with whom anyone can chat!! \n You can search dictionary words also!!")

# Create start function
def start():
    child.withdraw()
    global root,e,window
    root = Toplevel()
    root.title("ChatBot")
    root.geometry("600x400")

    icon = PhotoImage(file='bot.png')

    # Setting icon of chatbot window
    root.iconphoto(False, icon)

    # Create menu bar
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Add items in menu
    add = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=add)
    add.add_command(label="Home",command = home)
    add.add_command(label="Save", command=save)
    add.add_command(label="Exit", command=root.quit)

    ed = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit", menu=ed)
    ed.add_command(label="Delete (Single Line)", command=delt)
    ed.add_command(label="Clear Screen", command=clear)

    # ed = Menu(my_menu,tearoff = 0)
    # my_menu.add_cascade(label = "Options",menu = ed)
    # ed.add_command(label = "Change Window Color",command = col)
    # ed.add_command(label = "Clear Screen",command = clear)

    ed = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="About", menu=ed)
    ed.add_command(label="About this", command=abt)

    # Add scroll bar in chat window
    my_frame = Frame(root)
    scroll = Scrollbar(my_frame, orient=VERTICAL)

    # Create Chat Window
    window = Listbox(my_frame, bg="black", fg="green", width=80, height=20, yscrollcommand=scroll.set)

    # Configure scrollbar
    scroll.config(command=window.yview)
    scroll.pack(side=RIGHT, fill=Y)
    my_frame.pack()

    window.pack(pady=5)

    # Take input from user
    e = Entry(root, width=30, font=("Helvetica", 20))
    e.place(y=335, height=40, relx=0.009)

    # Create send button
    btn = Button(root, text="Send", bg="#1261A0", activebackground="light green", command=send)
    btn.place(x=490, y=335, height=40, width=100)

    root.mainloop()



# Create home function
def home():
    global child,root
    root.withdraw()
    child.withdraw()
    child = Toplevel()
    child.title("Home")
    child.geometry("400x400")
    icon = PhotoImage(file = "bot.png")

    child.iconphoto(False,icon)

    about = Label(child, text="Welcome!!", font=("Helvetica", 20))
    about.pack(pady=30)

    img = ImageTk.PhotoImage(Image.open('chat.png'))
    lab = Label(image=img)
    lab.pack(pady=10)

    start_btn = Button(child, text="Start", width=20, bg="light green", activebackground="orange", command=start,relief="raised")
    start_btn.pack(pady=20)

    txt = Label(child, text="Press start button to start the chat with bot!!", relief="raised", fg="red")
    txt.pack(pady=20, padx=30)


    child.mainloop()



child = Tk()
child.title("Home")
child.geometry("400x400")
icon = PhotoImage(file='bot.png')

# Setting icon of chatbot window
child.iconphoto(False, icon)



about = Label(child, text="Welcome!!",font=("Helvetica",20))
about.pack(pady = 30)

# Adding image in home page
img = ImageTk.PhotoImage(Image.open('chat.png'))
lab = Label(image = img).pack(pady = 10)

start_btn = Button(child,text = "Start",width = 20,bg = "light green",activebackground = "orange",command = start,relief = "raised")
start_btn.pack(pady = 20)

txt = Label(child,text = "Press start button to start the chat with bot!!",relief = "raised",fg = "red")
txt.pack(pady = 20,padx = 30)


child.mainloop()




