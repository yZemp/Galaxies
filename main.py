from simple_term_menu import TerminalMenu
import time
from Galaxy import Galaxy
import pickling as pck

###########################################################
# CONSTANTS

menu_1 = "Start Quiz"
menu_2 = "Add galaxy to database"
menu_3 = "List all galaxies loaded"
menu_4 = "Remove a galaxy from database"
menu_5 = "Exit"


###########################################################
# DATA
try:
    galaxies = pck.load()
except:
    galaxies = [] 

###########################################################
# FUNCTIONS

def clear_screen():
    print("\033[H\033[J", end="")

def start_quiz():
    for g in galaxies:
        g.show()

def add_gal():
    clear_screen()
    name = input("Galaxy name (no spaces, no quotemarks): ")
    path = input("Path to image in local folde (path/to/image.png): ")
    bar = bool(input("Does it have a bar? (true/false) "))
    type = input("What's its type? ")
    galaxies.append(Galaxy(name, path, bar, type))
    pck.store(galaxies)
    print(f"Galaxy {name} has been added to the database")
    print()

def list_all():
    clear_screen()
    print(f"{len(galaxies)} galaxy(es) in database:")
    for g in galaxies:
        print(g)
    print()

def remove_gal():
    clear_screen()
    print("Select the galaxy you want to eliminate:")
    gals = [gal.name for gal in galaxies]
    gals.insert(0, "Go back")
    elim_menu = TerminalMenu(gals)
    index = elim_menu.show()
    if index == 0: return 0
    del galaxies[index - 1]
    pck.store(galaxies)
    clear_screen()


###########################################################
# App loop

loop = True
while loop:
    options = [menu_1, menu_2, menu_3, menu_4, menu_5]
    terminal_menu = TerminalMenu(options, clear_screen = False, clear_menu_on_exit = True)
    selection = terminal_menu.show()

    if (selection == 0): start_quiz()
    if (selection == 1): add_gal()
    if (selection == 2): list_all()
    if (selection == 3): remove_gal()
    if (selection == 4): 
        print("Saving and exiting...")
        pck.store(galaxies)
        time.sleep(.5)
        loop = False


