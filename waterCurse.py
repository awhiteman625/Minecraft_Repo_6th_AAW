import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
c = 0
while c < 30:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x, y, z, x, y+1, z, 8)
    time.sleep(1)
    c += 1
