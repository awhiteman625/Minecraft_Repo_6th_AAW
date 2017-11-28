from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 6
y = 5
z = 28
BT = 103
mc.setBlock(x, y, z, BT)
mc.setBlock(x, y + up, z, BT)
