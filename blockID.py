from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103
def wool():
    return 35
def lava():
    return 11
def water():
    return 9
def TNT():
    return 46
def flower():
    return 37
def diamondBlock():
    return 57

block = melon()
x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, block)
