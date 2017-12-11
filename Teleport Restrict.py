from mcpi.minecraft import Minecraft
mc = Minecraft.create()
v = True
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
if not -127 < x < 127:
    v = False
if not -63 < y <63:
    v = False
if not -127 < z < 127:
    v = False
if v:
    mc.player.setPos(x, y, z)
else:
    mc.postToChat("Please enter a valid location")
