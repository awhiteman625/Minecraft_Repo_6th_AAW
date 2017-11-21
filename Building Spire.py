from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
height = 2
block = 1
sideHeight = height
pointHeight = 4
baseHeight = 1
mc.setBlocks(x+1, y, z+1, x+3, y+sideHeight-1, z+3, block)
mc.setBlocks(x+2, y, z+2, x+2, y+pointHeight-1, z+2, block)
mc.setBlocks(x, y, z, x+4, y+baseHeight-1, z+4, block)

