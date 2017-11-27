from mcpi.minecraft import Minecraft
mc = Minecraft.create()
ans = input("Create a crater? Y/N ")
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x-1, y-1, z-1, 0)
mc.postToChat("Boom!")
