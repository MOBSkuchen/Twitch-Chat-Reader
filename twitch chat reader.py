import socket, time
def loadEssentials(name):
    if not name == "none":
        global irc, CHANNEL
        SERVER = "irc.twitch.tv"
        PORT = 6667
        PASS = "XXXXXXXXXXXXXXXXXX"  # Oauth of twitch
        BOT = "Ebot"
        CHANNEL = name
        OWNER = ""  # Your Twitch Name, not needed lol
        irc = socket.socket()
        try:
            irc.connect((SERVER, PORT))
        except ConnectionResetError:
            print("Connecttion refused, please try again.")
            return False
        irc.send(("PASS " + PASS + "\n" +
                  "NICK " + BOT + "\n"
                                  "JOIN #" + CHANNEL + "\n").encode())
    else:
        return
def join_chat(name):
    time.sleep(1)
    loadEssentials(name)
    global counter, Loading
    Loading = True
    while Loading:
        readbuffer_join = irc.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n"):
            loadingComplete(line)
            back = getMash(line, "all")
            if not back == None and not "tmi.twitch" in back:
                print(back)
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
        print(f"Connected {CHANNEL}'s Channel")
        return False
    else:
        return True
join_chat() # Channel
