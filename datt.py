import sqlite3
import curses
import time
import random
from lorem import gen_lorem
class Project:
    def __init__(self, id=None,name="unamed" ,subject="no subject" ,description="No description", time=0, files=None):
        self.name = name
        self.subject = subject
        self.arguments = 
        self.description = description
        self.time = int(time)
        self.files = files
        self.id = id
    def __str__(self):
        return f"{self.name}, {self.time}, {self.subject} : {self.description}" 

def load_proj(proj):
    return Project(*get_proj(f"SELECT * FROM projects WHERE name == '{proj}'")[0])

def monitor(proj):
    print(f"start monitoring {proj}")
    time.sleep(1)
    stdscr = curses.initscr()
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.timeout(1000)
    curses.noecho()
    stat = load_proj(proj)
    while True:
        stdscr.clear()

        stdscr.addstr(0, 2, f"{proj} Current Stats :")
        stdscr.addstr(1, 2, f"time : {stat.time}")
        stdscr.refresh()
        t = time.time()
        key = stdscr.getch()
        waittime = max(0, 1 - (time.time() - t))

        if key in [10, 13]:  # Enter key
            curses.endwin()
            break
        stat.time += 1
        time.sleep(waittime)
    save_proj(stat)


def get_proj(request):     
    with sqlite3.connect("dttb.db") as conn:
        c = conn.cursor()
        c.execute(request)
    return c.fetchall() 

def create_proj(proj):
    print(f'INSERT INTO projects (name, subject, description, files) VALUES ("{proj.name}", "{proj.subject}", "{proj.description}", "{proj.files if proj.files != None else 'NULL'}") ')
    get_proj(f'INSERT INTO projects (name, subject, description, files) VALUES ("{proj.name}", "{proj.subject}", "{proj.description}", "{proj.files if proj.files != None else 'NULL'}") ')

def save_proj(proj):
    get_proj(f"UPDATE projects SET name = '{proj.name}', subject = '{proj.subject}', description = '{proj.description}', time = '{proj.time}',files = 'NULL' WHERE id = '{proj.id}'  ")

def get_proj_name():
    return [row[0] for row in get_proj("SELECT name FROM projects")]

def lorem(len):
    return 


if __name__ == "__main__":
    pass
