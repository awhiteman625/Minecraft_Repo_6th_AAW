from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
s = 0
x, y, z = mc.player.getPos()
BA = mc.getBlock(x, y+2, z)
while BA == 8 or BA == 9:
    time.sleep(1)
    pos = mc.player.getPos()
    BA = mc.getBlock(pos.x, pos.y + 2, pos.z)
    s = s + 1
    mc.postToChat("Current score: " + str(s))

mc.postToChat("Final score: " + str(s))
if s > 6:
    FP = mc.player.getTilePos()
    mc.setBlocks(FP.x-5, FP.y+10, FP.z-5, FP.x+5, FP.y+10, FP.z+5, 38)
    
