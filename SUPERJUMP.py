from mcpi.minecraft import Minecraft
mc = Minecraft.create()
position = mc.player.getTilePos()
x = position.x + 8
y = position.y + 3
z = position.z + 21
mc.player.setTilePos()
