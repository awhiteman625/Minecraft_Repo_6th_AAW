from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)
if gift == 0:
    mc.postToChat("Place an Offering at the Pedistal " + str(x) + " " + str(y) + " " + str(z))
elif gift == 0:
    mc.postToChat("Get a Life!")
    time.sleep(0.5)
    mc.player.setTilePos(45, 3, -12)
else:
    mc.player.setTilePos(45, 1, -9)
    mc.postToChat("Ya rich man!")
