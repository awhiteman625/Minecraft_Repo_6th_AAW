from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
step = 0
for step in range(0, 100):
    mc.setBlock(x + step, y + step, z, 53)
    step += 1
