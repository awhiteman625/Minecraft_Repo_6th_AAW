from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a = 0
w = 9
while True:
    x, y, z = mc.player.getTilePos()
    BB = mc.getBlock(x, y-1, z)
    if BB != a and BB != w:
        mc.setBlock(x, y-1, z, 41)
