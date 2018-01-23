from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

def melon():
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y - 1, z 103)
    time.sleep(2)

melon()
melon()
melon()
melon()
melon()
melon()
