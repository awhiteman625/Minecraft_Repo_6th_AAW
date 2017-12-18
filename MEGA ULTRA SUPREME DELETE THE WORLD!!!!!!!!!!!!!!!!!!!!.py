from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-127, y-63, z-127, x+127, y+63, z+127, 0)
    time.sleep(0.1)
