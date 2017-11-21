from mcpi.minecraft import Minecraft
mc = Minecraft.create()
X, Y, Z = mc.player.getPos()
mc.setBlocks(X+2, Y, Z-4, X+4, Y+3, Z-2, 35, 6)
mc.setBlocks(X+2, Y, Z+4, X+4, Y+3, Z+2, 35, 6)
mc.setBlocks(X+8, Y, Z-4, X+10, Y+3, Z-2, 35, 6)
mc.setBlocks(X+8, Y, Z+4, X+10, Y+3, Z+2, 35, 6)
mc.setBlocks(X+2, Y+4, Z-4, X+10, Y+7, Z+4, 35, 6)
mc.setBlocks(X+3, Y+5, Z-3, X+9, Y+6, Z+3, 46, 1)
mc.setBlock(X+3, Y+7, Z-1, X+1, Y+9, Z+1, 35, 6)
mc.setBlock(X+1, Y+8, Z-1, 49)
mc.setBlock(X+1, Y+8, Z+1, 49)

