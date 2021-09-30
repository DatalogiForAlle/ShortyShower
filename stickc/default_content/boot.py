import sys
sys.path.append('flowlib/lib')

import machine, time, m5base, uiflow
from m5stack import *
__VERSION__ = m5base.get_version()
#lcd.print(__VERSION__, lcd.RIGHT, 65)

def reset_screen():
    lcd.setRotation(1)
    lcd.image(lcd.CENTER, 0, 'ucphlogo.bmp')
    lcd.setTextColor(0x000000, 0xffffff)

reset_screen()
