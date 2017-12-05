from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mes = input("Enter your username: ")
mc.postToChat(mes)
