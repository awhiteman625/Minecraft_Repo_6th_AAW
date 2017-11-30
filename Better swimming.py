from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = mc.getBlock(x, y, z)
BT = mc.getBlock(x, y + 1, z)
UW = blockType == 9 and BT == 9
mc.postToChat("The player is under water: " + str(UW))
