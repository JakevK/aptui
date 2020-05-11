import os



def dimensions():
    screen_sizes = os.popen('stty size', 'r').read().split()
    screen_y, screen_x = map(int, screen_sizes)
    
    return {"x": screen_x, "y": screen_y}


def clear():
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 