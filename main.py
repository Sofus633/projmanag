from datt import start_session, get_proj_name
from display import display_proj
import time
def select_proj():
    cursorpos = 0
    proj_name = get_proj_name()
    return display_proj(cursorpos, proj_name) 


actions = {
        "startsession" : start_session

}

print("welcome silly lil mushroom")
def main():

    
    while True:
        option = select_proj()
        print(option)
        if option != None:
            print(option)
        else:
            break
        
        



main()
