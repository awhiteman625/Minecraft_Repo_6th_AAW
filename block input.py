from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
blockType = int(input("what block id do you want to place? "))
mc.setBlock(x, y, z, blockType)
    
