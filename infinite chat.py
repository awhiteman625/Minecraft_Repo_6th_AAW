from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input("Enter your username: ")
while True: 
    mes = input("Enter your message: ")
    if mes != "exit":
        mc.postToChat(str(name) + ": " + str(mes))
    else:
        break
