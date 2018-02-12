from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def brokenBlocks():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
height, width = 5, 10

for e in range(height):
    for w in range(width):
        block = brokenBlocks()
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
