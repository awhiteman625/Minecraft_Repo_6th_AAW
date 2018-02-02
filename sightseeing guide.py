from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"lava": (35.7, -1.0, 81.1), "barrier": (-135.8, 64.0, 156.7)}
choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
