from datt import get_proj_name, monitor
from display import display_proj

import time
def select_proj():
    cursorpos = 0
    proj_name = get_proj_name()
    return display_proj(cursorpos,  proj_name) 


actions = {}

def main():
    while True:
        select_proj()
        break

main()



