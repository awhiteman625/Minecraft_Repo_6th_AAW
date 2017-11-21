from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
air = 0
while True:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y-1, z-1, x-1, y+3, z+1, air)
    sleep(0.1)
    
