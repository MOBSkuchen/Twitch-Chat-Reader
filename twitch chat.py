import socket, keyboard, time
from tkinter import *
def error(text):
    error = Label(master=root, bg='red', text=text)
    error.place(x=0, y=40, width=310, height=40)
def say(textS):
    import win32com.client as wcc
    class Sprecher(object):
        def __init__(self):
            self.speaker = wcc.Dispatch("SAPI.SpVoice")
            self.sprechen()
        def sprechen(self):
            text_ = str(textS)
            tonSchnelle = int(0)
            tonLage = int(0)
            tonVolume = int(100)
            self.speaker.Rate = tonSchnelle
            self.speaker.Volume = tonVolume
            text = """<pitch middle="{0}" > {1} </pitch> """.format(tonLage, text_)
            self.speaker.Speak(text)
    a = Sprecher()
def piston(new_value):
    global text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12
    text_1 = text_2
    text_2 = text_3
    text_3 = text_4
    text_4 = text_5
    text_5 = text_6
    text_6 = text_7
    text_7 = text_8
    text_8 = text_9
    text_9 = text_10
    text_10 = text_11
    text_11 = text_12
    text_12 = new_value
def disconnect():
    global Loading, Started
    Loading = False
    loadEssentials("none")
def close():
    global Loading
    Loading = False
    time.sleep(0.5)
    root.destroy()
def start_software():
    global Started
    Started = True
def close_software():
    global Started
    Started = False
def clear():
    global text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12
    text_1 = ""
    text_2 = ""
    text_3 = ""
    text_4 = ""
    text_5 = ""
    text_6 = ""
    text_7 = ""
    text_8 = ""
    text_9 = ""
    text_10 = ""
    text_11 = ""
    text_12 = ""
    piston("")
def render_base():
    global root, entryName
    root = Tk()
    root.config(background="white")
    root.title("Twitch Chat")
    root.geometry("840x480")
    entryName = Entry(master=root, bg='white')
    entryName.place(x=150, y=150, width=500, height=27)
    btnConnect = Button(master=root, bg='cyan', text='Connect', command=join_chat)
    btnConnect.place(x=325, y=100, width=200, height=35)
    btnclose = Button(master=root, bg='cyan', text='Close', command=close)
    btnclose.place(x=325, y=50, width=200, height=35)
    btndisconnect = Button(master=root, bg='cyan', text='Disconnect', command=disconnect)
    btndisconnect.place(x=325, y=0, width=200, height=35)
    btnStartSoftware = Button(master=root, bg='cyan', text='Start Software', command=start_software)
    btnStartSoftware.place(x=625, y=0, width=200, height=35)
    btnclosesoftware = Button(master=root, bg='cyan', text='Close Software', command=close_software)
    btnclosesoftware.place(x=625, y=50, width=200, height=35)
    Clear = Button(master=root, bg='cyan', text='Clear Chat', command=clear)
    Clear.place(x=625, y=100, width=200, height=35)
    consoledsgb = Label(master=root, bg='cyan', text="")
    consoledsgb.place(x=0, y=0, height=90, width=320)
    root.mainloop()
global Started
Started = False
def loadEssentials(name):
    global irc, SERVER, PORT, CHANNEL,PASS,OWNER, counter
    global text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12
    text_1 = ""
    text_2 = ""
    text_3 = ""
    text_4 = ""
    text_5 = ""
    text_6 = ""
    text_7 = ""
    text_8 = ""
    text_9 = ""
    text_10 = ""
    text_11 = ""
    text_12 = ""
    counter = int(0)
    if not name == "none":
        SERVER = "irc.twitch.tv"
        PORT = 6667
        PASS = "XXXXXXXXXXXXXXXXXXX" # Oauth of twitch
        BOT = "Ebot"
        CHANNEL = name
        OWNER = "" # Your Twitch Name
        irc = socket.socket()
        try:
            irc.connect((SERVER, PORT))
        except ConnectionResetError:
            error("Connecttion refused, please try again.")
            return False
        irc.send(("PASS " + PASS + "\n" +
                  "NICK " + BOT + "\n"
                                  "JOIN #" + CHANNEL + "\n").encode())
    else:
        return
def join_chat():
    name = str(entryName.get())
    time.sleep(1)
    loadEssentials(name)
    global counter, Loading
    Loading = True
    while Loading:
        readbuffer_join = irc.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        console1 = Label(master=root, bg='white', text=text_1)
        console1.place(x=0, y=200, width=840, height=20)
        console2 = Label(master=root, bg='white', text=text_2)
        console2.place(x=0, y=220, width=840, height=20)
        console3 = Label(master=root, bg='white', text=text_3)
        console3.place(x=0, y=240, width=840, height=20)
        console4 = Label(master=root, bg='white', text=text_4)
        console4.place(x=0, y=260, width=840, height=20)
        console5 = Label(master=root, bg='white', text=text_5)
        console5.place(x=0, y=280, width=840, height=20)
        console6 = Label(master=root, bg='white', text=text_6)
        console6.place(x=0, y=300, width=840, height=20)
        console7 = Label(master=root, bg='white', text=text_7)
        console7.place(x=0, y=320, width=840, height=20)
        console8 = Label(master=root, bg='white', text=text_8)
        console8.place(x=0, y=340, width=840, height=20)
        console9 = Label(master=root, bg='white', text=text_9)
        console9.place(x=0, y=360, width=840, height=20)
        console10 = Label(master=root, bg='white', text=text_10)
        console10.place(x=0, y=380, width=840, height=20)
        console11 = Label(master=root, bg='white', text=text_11)
        console11.place(x=0, y=400, width=840, height=20)
        console12 = Label(master=root, bg='white', text=text_12)
        console12.place(x=0, y=420, width=840, height=20)
        root.update()
        for line in readbuffer_join.split("\n"):
            loadingComplete(line)
            back = getMash(line, "all")
            if not back == None and not "tmi.twitch" in back:
                piston(back)
                message = getMash(line, "only_message")
                if Started == True:
                    with open("start_config.twitch", "r+") as configuration:
                        config = configuration.read()
                        for cmds in config.split("\n"):
                            active, dooer = cmds.split(";")
                            if (active) in message:
                                if dooer.startswith("exe:"):
                                    exe = dooer.replace("exe:", "")
                                    keyboard.press(exe)
                                elif dooer.startswith("say:"):
                                    saye = dooer.replace("say:", "")
                                    say(saye)
                                else:
                                    pass
                            else:
                                pass
            else:
                pass
def getMash(line,scope):
    try:
        message = (line.split(":",2))[2]
        seperate = line.split(":", 2)
        user = seperate[1].split("!", 1)[0]
        mash = (user + " : " + message)
        if scope == "all":
            return mash
        elif scope == "only_user":
            return user
        elif scope == "only_message":
            return message
    except:
        return
def loadingComplete(line):
    if ("End of /NAMES list" in line):
        console13 = Label(master=root, bg='lime', text="Connected to " + CHANNEL + "'s Channel.")
        console13.place(x=0, y=0, width=310, height=40)
        return False
    else:
        return True
render_base()
