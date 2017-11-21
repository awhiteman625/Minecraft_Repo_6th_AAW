import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x1, y1, z1 = mc.player.getTilePos()
time.sleep(10)
x2, y2, z2 = mc.player.getTilePos()
xd = x2 - x1
yd = y2 - y1
zd = z2 - z1
mc.postToChat("The Player has Moved: X: " + str(xd) + ", Y: " + str(yd) + ", z: " + str(zd))
