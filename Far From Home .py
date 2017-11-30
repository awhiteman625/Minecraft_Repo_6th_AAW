from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
hX = 10
hZ = 10
pos = mc.player.getTilePos()
x = pos.x
z = pos.z
distance = math.sqrt((hX - x) ** 2 + (hZ - z) ** 2)
nearby = distance >= 40
mc.postToChat("Your house is nearby: " + str(nearby))

                     
