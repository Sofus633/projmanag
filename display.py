import curses
import time
from datt import Project, monitor

def display_proj(cursor, proj_name):
    print(proj_name)
    stdscr = curses.initscr()
    curses.curs_set(0)  
    stdscr.clear()
    curses.noecho()
    options = proj_name
    options.append("Exit")
    selected = 0
    stdscr.timeout(1000)
    count = 0
    while True:
        stdscr.clear()

        # Display menu with highlight
        for i, option in enumerate(options):
            style = curses.A_REVERSE if i == selected else curses.A_NORMAL
            try:
                stdscr.addstr(i, 2, option, style)
            except curses.error:
                pass

        stdscr.refresh()

        key = stdscr.getch()
        try:
                    stdscr.addstr(i, 2, 'refreshing' + str(count))
        except curses.error:
            pass
        count += 1
        stdscr.refresh()
        # Handle key presses
        if key == 122 and selected > 0:
            selected -= 1
        elif key == 115 and selected < len(options) - 1:
            selected += 1
            
        elif key in [10, 13]:  # Enter key
            stdscr.addstr(len(options) + 2, 2, f"Selected: {options[selected]}")
            stdscr.refresh()
            
            if options[selected] == "Exit":
                curses.endwin()
                break

            second_selection(option[selected], stdscr, max([len(val) for val in options]))
        
        
            



def second_selection(project, stdscr, niv): 
    niv += 5
    selected = 0
    
    while True:

        options = ["Start Monitoring", "Stats", "Archive", "Remove"]
        
        for i, option in enumerate(options):
            style = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(i, niv, option, style)
            
        key = stdscr.getch()
        stdscr.refresh()
        
        if key == 122 and selected > 0:
            selected -= 1
        elif key == 115 and selected < len(options) - 1:
            selected += 1
        elif key == 113 and selected < len(options) - 1:
            break
        elif key in [10, 13]:
            match option[selected]:
                case "Start Monitoring":
                    monitor(project)
                    break
                case "Stats":
                    pass
                case "Archive":
                    pass
                case "Remove":
                    pass
        
            
class Choix:
    def __init__(self, choix, startpos, predecesseur=None):
        self.choix = choix
        self.startpos = startpos
        self.predecesseur = predecesseur
        self.alive = True
        if predecesseur != None:
            self.screen = predecesseur.screen
        else:
            self.screen = curses.initscr()
    
    def loop(self):
        
        while self.alive:
            self.checkinp()
            
    def checkinp(self):
        key = self.screen.getch()