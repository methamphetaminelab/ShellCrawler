import curses
from dungeonGenerator import generateDungeon
from player import movePlayer, playerPos

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    dungeon, roomsCoords, width, height = generateDungeon()

    x, y = playerPos
    dungeon[x][y] = "◆"

    while True:
        stdscr.clear()
        for row in dungeon:
            for col in row:
                if col == '◆':
                    stdscr.addstr(col, curses.color_pair(4))
                elif col == '▼':
                    stdscr.addstr(col, curses.color_pair(1))
                elif col == '○':
                    stdscr.addstr(col, curses.color_pair(2))
                elif col == '●':
                    stdscr.addstr(col, curses.color_pair(3))
                else:
                    stdscr.addstr(col)
            stdscr.addstr("\n")
        stdscr.refresh()

        key = stdscr.getch()
        dungeon = movePlayer(dungeon, key, roomsCoords)

curses.wrapper(main)
