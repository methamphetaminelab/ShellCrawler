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

def generateEnemies(dungeon, width, height, enemiesCount):
    for _ in range(enemiesCount):
        chestX = random.randint(1, height - 2)
        chestY = random.randint(1, width - 2)
        
        while dungeon[chestX][chestY] != ".":
            chestX = random.randint(1, height - 2)
            chestY = random.randint(1, width - 2)
        
        dungeon[chestX][chestY] = 'E'

    return dungeon

def generateChests(dungeon, width, height, chestsCount):
    for _ in range(chestsCount):
        chestX = random.randint(1, height)
        chestY = random.randint(1, width)
        
        while dungeon[chestX][chestY] != ".":
            chestX = random.randint(1, height)
            chestY = random.randint(1, width)
        
        dungeon[chestX][chestY] = 'C'

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

    for row in dungeon:
        print(''.join(row))

    return dungeon, roomsCoords, width, height