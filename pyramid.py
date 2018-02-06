from mcpi.minecraft import Minecraft
mc = Minecraft.create()
height = 10
levels = range(height)
x, y, z = mc.player.getTilePos()
y += height

for level in levels:
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, 24)
    y += 1
