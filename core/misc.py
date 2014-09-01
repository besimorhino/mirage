import os
def clear(): # clear the screen
    if (os.name == 'nt'):    
        c = os.system('cls')
    else:
        c = os.system('clear')