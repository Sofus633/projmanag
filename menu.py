import curses

class Menu:
    def __init__(self, options, precedent=None, exit=None):
        self.options = options
        self.screen = curses.initscr()
        self.precedent = precedent
        self.selected = 0
        self.position = 0
        self.rows, self.cols = self.screen.getmaxyx()
        if precedent != None:
            self.goback = True
            self.exit = None
        else:
            self.exit = exit
            self.options.insert(0, self.exit)
        curses.curs_set(0)
        curses.noecho()
        self.screen.timeout(1000)
        self.screen.clear()
        self.loop()

    
    def loop(self):
        key = 0
        while True:
            self.screen.clear()
            for i, option in enumerate(self.options):
                style = curses.A_REVERSE if i == self.selected else curses.A_NORMAL
                try:
                    self.screen.addstr(i-self.position, 2, option, style)
                except curses.error:
                    pass
            key = self.screen.getch()
            
            
            if key == 122 and self.selected > 0:
                self.selected -= 1
                if self.selected == self.position - 1:
                    self.position -= 1
            elif key == 115 and self.selected < len(self.options) - 1:
                self.selected += 1
                if self.selected > self.rows - 1:
                    self.position += 1
            elif key in [10, 13]:
                if self.options[self.selected] == self.exit:
                    curses.endwin()
                    break
                self.options[self.selected][1]()
                    

        
        
if __name__ == "__main__":
    menu = Menu([f"Option {i}" for i in range(10)], exit="Exit")