import random
from roomsList import rooms

def generateClearDungeon(width, height):
    dungeon = [["." for _ in range(width)] for _ in range(height)]
    
    top = "╔" + "═" * width + "╗"
    bot = "╚" + "═" * width + "╝"
    dungeon.insert(0, list(top))
    dungeon.append(list(bot))

    for row in dungeon[1:-1]:
        row.insert(0, "║")
        row.append("║")

    return dungeon

def fillRoomWithDots(dungeon, roomX1, roomY1, roomX2, roomY2):
    for x in range(roomX1, roomX2 + 1):
        for y in range(roomY1, roomY2 + 1):
            if dungeon[x][y] == " ":
                dungeon[x][y] = "."
    return dungeon

def generateEnemies(dungeon, roomX1, roomY1, roomX2, roomY2, enemiesCount):
    placedEnemies = 0
    if enemiesCount > 2:
        enemiesCount = 2

    dungeon = fillRoomWithDots(dungeon, roomX1, roomY1, roomX2, roomY2)

    while placedEnemies < enemiesCount:
        enemyX = random.randint(roomX1, roomX2)
        enemyY = random.randint(roomY1, roomY2)
        
        if dungeon[enemyX][enemyY] == ".":
            if random.randint(0, 5) > 0:
                dungeon[enemyX][enemyY] = "E"
                placedEnemies += 1

    return dungeon

def generateChests(dungeon, roomX1, roomY1, roomX2, roomY2, chestsCount):
    placedChests = 0
    if chestsCount > 2:
        chestsCount = 2

    if chestsCount <= 0:
        chestsCount = 1

    dungeon = fillRoomWithDots(dungeon, roomX1, roomY1, roomX2, roomY2)

    while placedChests < chestsCount:
        chestX = random.randint(roomX1, roomX2)
        chestY = random.randint(roomY1, roomY2)
        
        if dungeon[chestX][chestY] == "." or dungeon[chestX][chestY] == " ":
            if random.randint(0, 5) > 0:
                dungeon[chestX][chestY] = "C"
                placedChests += 1

    return dungeon

def placeChecker(dungeon, room, roomX, roomY):
    roomHeight = len(room)
    roomWidth = len(room[0])

    if roomX + roomHeight > len(dungeon) or roomY + roomWidth > len(dungeon[0]):
        return False

    for i in range(roomHeight):
        for j in range(roomWidth):
            if dungeon[roomX + i][roomY + j] != ".":
                return False

    for i in range(roomX - 1, roomX + roomHeight + 1):
        for j in range(roomY - 1, roomY + roomWidth + 1):
            if 0 <= i < len(dungeon) and 0 <= j < len(dungeon[0]):
                if dungeon[i][j] != ".":
                    return False

    return True

def generateDoors(dungeon, roomX, roomY, roomWidth, roomHeight):
    doors = ['u', 'd', 'l', 'r']
    
    doorDirection = random.choice(doors)

    if doorDirection == 'u': 
        doorPos = roomY + roomWidth // 2
        dungeon[roomX][doorPos] = '-'
    elif doorDirection == 'd':
        doorPos = roomY + roomWidth // 2
        dungeon[roomX + roomHeight - 1][doorPos] = '-'
    elif doorDirection == 'l':
        doorPos = roomX + roomHeight // 2
        dungeon[doorPos][roomY] = '|'
    elif doorDirection == 'r':
        doorPos = roomX + roomHeight // 2
        dungeon[doorPos][roomY + roomWidth - 1] = '|'
    
    return dungeon

def generateRooms(dungeon, width, height):
    roomsPlaced = 0
    roomsCoords = []

    for _ in range(len(dungeon)):
        room = random.choice(rooms["chestrooms"])
        roomWidth = len(room[0])
        roomHeight = len(room)
        
        placed = False
        attempts = 0

        if height <= roomHeight or width <= roomWidth:
            continue

        while not placed and attempts < 100:
            roomX = random.randint(1, max(1, height - roomHeight - 1))
            roomY = random.randint(1, max(1, width - roomWidth - 1))
            
            if placeChecker(dungeon, room, roomX, roomY):
                for i in range(roomHeight):
                    for j in range(roomWidth):
                        dungeon[roomX + i][roomY + j] = room[i][j]
                
                dungeon = generateDoors(dungeon, roomX, roomY, roomWidth, roomHeight)
                placed = True
                roomsPlaced += 1
                cRoomCoords = [roomX + 1, roomY + 1, roomX + roomHeight - 2, roomY + roomWidth - 2]
                #dungeon[cRoomCoords[0]][cRoomCoords[1]] = '+'
                #dungeon[cRoomCoords[2]][cRoomCoords[3]] = '+'
                roomsCoords.append(cRoomCoords)
            attempts += 1

    print(roomsCoords)
    if roomsPlaced == 0:
        return generateRooms(dungeon, width, height)
    else:
        return dungeon, roomsCoords

def randomSize():
    return random.randint(20, 30), random.randint(10, 15)

def generateDungeon(enemiesCount, chestsCount, floorsCount):
    width, height = randomSize() # Выбираем размер подземелья
    print(f"{width}x{height}")
    
    dungeon = generateClearDungeon(width, height)  # Генерируем пустое подземелья
    dungeon, roomsCoords = generateRooms(dungeon, width, height)  # Генеруем комнаты
    # dungeon = generateChests(dungeon, width, height, roomsCoor)  # Генерация сундуков
    # dungeon = generateEnemies(dungeon, width, height, enemiesCount)  # Генерация врагов

    return dungeon, roomsCoords, width, height