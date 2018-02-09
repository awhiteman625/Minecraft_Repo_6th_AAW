from mcpi.minecraft import Minecraft
mc = Minecraft.create()

depth = 0
x, y, z = mc.player.getTilePos()
for error in range(1, 51):
    depth += 1
    block = mc.getBlock(x, y, z)
    if block == 56:
        mc.postToChat("There is a diamond ore " + str(depth) + " blocks below you")
        break
    else:
        y -= 1
else:
    mc.postToChat("There is no diamond ore below you")
