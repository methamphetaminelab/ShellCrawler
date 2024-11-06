import random
from roomsList import rooms

def placeChecker(dungeon, room, width, height, roomX, roomY):
    roomWidth = len(room[0])
    roomHeight = len(room)

    if roomX + roomHeight > height or roomY + roomWidth > width or roomX < 0 or roomY < 0: # если не заходит за границы
        return False

    for i in range(roomHeight):
        for j in range(roomWidth):
            if dungeon[roomX + i][roomY + j] != '.': # если точка размещения не пуста
                return False
    return True

def placeSpawnRoom(dungeon, width, height):
    room = random.choice(list(rooms.values()))

    roomHeight = len(room)
    roomWidth = len(room[0])

    roomX = random.randint(1, height - roomHeight - 1)
    roomY = random.randint(1, width - roomWidth - 1)

    if placeChecker(dungeon, room, width, height, roomX, roomY):
        for i in range(roomHeight):
            for j in range(roomWidth):
                dungeon[roomX + i][roomY + j] = room[i][j] # ставим комнату спавна

        spawnPoint = (roomX + roomHeight // 2 , roomY + roomWidth // 2)
        dungeon[spawnPoint[0]][spawnPoint[1]] = 'S' # ставим спавн

    return dungeon

def placeRoom():
    pass

def generateDungeon(width, height):
    dungeon = [['.' for _ in range(width)] for _ in range(height)]

    dungeon = placeSpawnRoom(dungeon, width, height)

    for row in dungeon:
        print(''.join(row))