import curses

def startFight():
    def fightScreen(stdscr):
        curses.curs_set(0)
        stdscr.clear()
        stdscr.addstr(0, 0, "FIGHT! Press 'q' to exit.", curses.A_BOLD)
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('q'):
                from main import game
                game(stdscr)

    curses.wrapper(fightScreen)
