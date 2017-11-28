from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = int(input("Enter your points: "))
if p > 2:
    mc.player.setPos(112, 10, 112)
elif p <= 2:
    mc.player.setPos(0, 12, 20)
elif p > 4:
    mc.player.setPos(60, 20, 32)
elif p > 6:
    mc.player.setPos(32, 18, -38)
else:
    mc.postToChat("I don't know what to do with that info.")
