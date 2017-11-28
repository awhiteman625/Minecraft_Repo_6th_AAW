from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x, y, z = mc.player.getPos()
x = x + random.randint(-10, 10)
mc.player.setPos(x, y, z)
