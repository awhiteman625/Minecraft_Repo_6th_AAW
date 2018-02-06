from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def setPillar(x, y, z, height):
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, 155, 1)
    mc.setBlock(x - 1, y + height - 1, z, 156, 12)
    mc.setBlock(x + 1, y + height - 1, z, 156, 13)
    mc.setBlock(x, y + height - 1, z + 1, 156, 15)
    mc.setBlock(x, y + height - 1, z - 1, 156, 14)
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, 155, 1)
    mc.setBlock(x - 1, y + 1, z, 156, 0)
    mc.setBlock(x + 1, y + 1, z, 156, 1)
    mc.setBlock(x, y + 1, z + 1, 156, 3)
    mc.setBlock(x, y + 1, z - 1, 156, 2)
    mc.setBlocks(x, y, z, x, y + height, z, 155, 2)

x, y, z = mc.player.getTilePos()
x += 2

for pillar in range(1, 21):
    setPillar(x, y, z, 15)
    x += 5
    z += 5
