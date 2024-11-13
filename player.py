import curses
from dungeonGenerator import generateChests, generateEnemies, generateFloor
import random

playerPos = [1, 1]

def movePlayer(dungeon, key, roomsCoords):
    global playerPos
    x, y = playerPos
    curses.curs_set(0)

    if '▼' not in dungeon:
        floorRoom = random.choice(roomsCoords)

    dungeon[x][y] = "."

    if key == curses.KEY_UP and dungeon[x - 1][y] not in ['╔', '═', '╗', '║', '╚', '╝']:
        x -= 1
    elif key == curses.KEY_DOWN and dungeon[x + 1][y] not in ['╔', '═', '╗', '║', '╚', '╝']:
        x += 1
    elif key == curses.KEY_LEFT and dungeon[x][y - 1] not in ['╔', '═', '╗', '║', '╚', '╝']:
        y -= 1
    elif key == curses.KEY_RIGHT and dungeon[x][y + 1] not in ['╔', '═', '╗', '║', '╚', '╝']:
        y += 1

    playerPos = [x, y]

    if dungeon[x][y] in ['-', '|']:
        dungeon = markClosestRoom(dungeon, playerPos, roomsCoords, floorRoom)

    dungeon[x][y] = "◆"
    return dungeon

def markClosestRoom(dungeon, playerPos, roomsCoords, floorRoom):
    def manhattanDistance(room, pos):
        roomX1, roomY1, roomX2, roomY2 = room
        roomCenter = [(roomX1 + roomX2) // 2, (roomY1 + roomY2) // 2]
        return abs(roomCenter[0] - pos[0]) + abs(roomCenter[1] - pos[1])

    closestRoom = min(roomsCoords, key=lambda room: manhattanDistance(room, playerPos))
    roomX1, roomY1, roomX2, roomY2 = closestRoom

    if closestRoom == floorRoom and '▼' not in dungeon:
        dungeon = generateFloor(dungeon, roomX1, roomY1, roomX2, roomY2)
    else:

        length = abs(roomX2 - roomX1) + 1
        width = abs(roomY2 - roomY1) + 1
        chestsCount = length * width // 3
        enemiesCount = chestsCount

        dungeon = generateChests(dungeon, roomX1, roomY1, roomX2, roomY2, random.randint(0, chestsCount))
        dungeon = generateEnemies(dungeon, roomX1, roomY1, roomX2, roomY2, random.randint(0, enemiesCount))

    return dungeon

