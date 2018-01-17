from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    #Write function to create tre at specified cordanates

x, y, z = mc.player.getTilePos()

growTree(x + 1, y, z)
