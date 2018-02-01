from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x, y, z = mc.player.getTilePos()
blocks = [81, 57, 35, 7, 118,
          61, 20, 42, 87, 86]
blockToPlace = random.choice(blocks)
mc.setBlock(x, y, z, blockToPlace)
