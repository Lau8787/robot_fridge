import curses

from robot_fridge import RobotFridge, MotorKit

ACTIONS = {
    'KEY_UP': 'move_forward',
    'KEY_DOWN': 'move_backward',
    'KEY_RIGHT': 'rotate_right',
    'KEY_LEFT': 'rotate_left',
    ' ': 'halt',
}

def main(win):
    bot = RobotFridge.from_kit(MotorKit())

    win.nodelay(True)

    try:
        while True:          
            try:                 
                key = win.getkey()         
                win.clear()                

                if key == '\x1b':
                    win.addstr('stop')
                    break           

                action = ACTIONS.get(key)
                if action is not None:
                    win.addstr(action)
                    getattr(bot, action)()
            except Exception:
                # No input   
                pass 
    finally:
        bot.halt()


if __name__ == '__main__':
    curses.wrapper(main)
