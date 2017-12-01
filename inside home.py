from mcpi.minecraft import Minecraft
mc = Minecraft.create()
bX = -3
bY = 8
bZ = 60
w = 3
h = 4
L = 3
x, y, z = mc.player.getTilePos()
inside = (bX <= x <= bX + w) and (bY <= y <= bY + h) and (bZ <= z <= bZ + L)
mc.postToChat("The player is at Home: " + str(inside))
