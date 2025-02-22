import curses
import time


def display_proj(cursor, proj_name):
    stdscr = curses.initscr()
    curses.curs_set(0)  
    stdscr.clear()

    options = ["Project A", "Project B", "Project C", "Exit"]
    selected = 0

    while True:
        stdscr.clear()

        # Display menu with highlight
        for i, option in enumerate(options):
            style = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(i, 2, option, style)

        stdscr.refresh()

        key = stdscr.getch()

        # Handle key presses
        if key == 122 and selected > 0:
            selected -= 1
        elif key == 115 and selected < len(options) - 1:
            selected += 1
        elif key in [10, 13]:  # Enter key
            if options[selected] == "Exit":
                curses.endwin()
                break
            stdscr.addstr(len(options) + 2, 2, f"Selected: {options[selected]}")
            time.sleep(1)
            curses.endwin()
            return options[selected]




