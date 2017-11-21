from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
try:
    blockType = int(input("what block id do you want to place? "))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("You did not enter a number! Enter a number next time.")

