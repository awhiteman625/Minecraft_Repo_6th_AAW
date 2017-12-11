import random
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
c = 1
while c <= 1:
    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
    mc.player.setTilePos(x, y, z)
    c += 1
    time.sleep(3)
    

