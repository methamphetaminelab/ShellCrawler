import curses
from dungeonGenerator import generateDungeon
from player import movePlayer, playerPos

def main(stdscr):
    dungeon, roomsCoords, width, height = generateDungeon(3, 2, 2)

    x, y = playerPos
    dungeon[x][y] = "+"

    while True:
        stdscr.clear()
        for row in dungeon:
            stdscr.addstr("".join(row) + "\n")
        stdscr.refresh()

        key = stdscr.getch()
        dungeon = movePlayer(dungeon, key, roomsCoords)

curses.wrapper(main)
