from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 50.0
y = 110.0
z = 2.0
mc.player.setPos(x, y, z)
time.sleep(0.5)
x = 100.0
y = 1.0                                                   
z = 22.0
mc.player.setPos(x, y, z)
time.sleep(4)
x = 13.0
y = 11.0
z = 12.0
mc.player.setPos(x, y, z)
time.sleep(2)
x = -111.0
y = 666.0                                                   
z = -122.0
mc.player.setPos(x, y, z)
time.sleep(10)
x = 10.0
y = 110.0
z = 15.0
mc.player.setPos(x, y, z)
