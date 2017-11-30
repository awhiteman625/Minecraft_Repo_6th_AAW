from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
hBY = mc.getHeight(x, z)
ag = hBY >= 0
mc.postToChat("The player is above ground: " + str(ag))
