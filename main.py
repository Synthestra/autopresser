import keyboard, json, ctypes, time
from pynput.mouse import Button, Controller

f = open("coords.json")
data = json.load(f)
events = data["events"]
f.close()


def click(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(2, x, y, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(4, x, y, 0, 0)

def right_click(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(8, x, y, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(16, x, y, 0, 0)


def get_mouse_pos():
    mouse = Controller()
    return mouse.position


def start_loop():
    
    stop = False
    while stop == False:
        if keyboard.is_pressed('#'):
            stop = True
                
        for event in events:
            if "click" in event:
                posx = 0
                posy = 0
                click_type = "left"
                
                if type(event["click"]) == dict:
                    if "type" in event["click"]:
                        click_type = event["click"]["type"]
                    posx = event["click"]["pos"][0]
                    posy = event["click"]["pos"][1]
                else:
                    posx = event["click"][0]
                    posy = event["click"][1]
                    
                if click_type == "left":
                    click(posx, posy)
                else:
                    right_click(posx, posy)
                
            if "button" in event:
                keyboard.press_and_release(event["button"])
            
            time.sleep(event["delay"])
            
            if keyboard.is_pressed('#'):
                stop = True
                break
            
        

start = False
while start == False:
    if keyboard.is_pressed('['):
        pos = get_mouse_pos()
        #ctypes.windll.user32.MessageBoxW(0, f"x = {pos[0]}, y = {pos[1]}", "Debug Coords", 0)
        print(pos[0], pos[1])
    elif keyboard.is_pressed(']'):
        start = True
        start_loop()
    else:
        pass
        

print("test")
