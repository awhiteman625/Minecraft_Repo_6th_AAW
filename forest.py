from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    mc.setBlocks (x, y, z, x, y + 3, z, 17)
    mc.setBlock(x, y + 5, z, 18)
    mc.setBlocks(x - 1, y + 4, z - 1, x + 1, y + 4, z + 1, 18)
    mc.setBlock(x, y + 4, z, 17)

x, y, z = mc.player.getTilePos()

growTree(x + 1, y, z)
