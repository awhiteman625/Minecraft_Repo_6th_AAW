from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x, y, z = mc.player.getTilePos()
FX = x-2
FY = y-1
FZ = z-2
w = 5
L = 5
B = 41
mc.setBlocks(FX, FY, FZ, FX+w, FY, FZ+L, B)
while FX <= x <= FX+w and FZ <= z <= FZ+L:
    if B == 41:
        B = 57
        mc.setBlocks(FX, FY, FZ, FX+w, FY, FZ+L, B)
        x, y, z = mc.player.getTilePos()
        time.sleep(0.5)
    else:
        B = 41
        mc.setBlocks(FX, FY, FZ, FX+w, FY, FZ+L, B)
        x, y, z = mc.player.getTilePos()
        time.sleep(0.5)
