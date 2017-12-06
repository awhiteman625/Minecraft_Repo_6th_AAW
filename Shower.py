from mcpi.minecraft import Minecraft
mc = Minecraft.create()
sX = 82
sY = -6
sZ = 23
w = 4
h = 3
L = 3
x, y, z = mc.player.getTilePos()
if sX <= x < sX + w and sY <= y < sY + h and sZ <= z < sZ + L:
    mc.setBlocks(sX, sY, sZ, sX + w, sY + h, sZ + L, 8)
else:
    mc.setBlocks(sX, sY, sZ, sX + w, sY + h, sZ + L, 0)
