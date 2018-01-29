from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    if color == "white":
        blockState = 0
    elif color == "orange":
        blockState = 1
    elif color == "magenta":
        blockState = 2
    elif color == "light blue":
        blockState = 3
    elif color == "yellow":
        blockState = 4
    elif color == "lime":
        blockState = 5
    elif color == "pink":
        blockState = 6
    elif color == "gray":
        blockState = 7
    elif color == "light gray":
        blockState = 8
    elif color == "cyan":
        blockState = 9
    elif color == "purple":
        blockState = 10
    elif color == "blue":
        blockState = 11
    elif color == "brown":
        blockState = 12
    elif color == "green":
        blockState = 13
    elif color == "red":
        blockState = 14
    elif color == "black":
        blockState = 15
    else:
        mc.postToChat("Invalid color input. Auto-setting wool color to 'Pink'")
        blockState = 6

    return blockState

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, 35, state)
