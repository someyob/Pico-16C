# to do:
# CLEAR PRGM
# CLEAR REG
# CLEAR PREFIX

import gc
import time
import board
import busio
from time import sleep, monotonic
from circuitpython_i2c_lcd import I2cLcd
from PICO_16C_keypad import *


version_string = "Pico 16C v0.4"
release_string = "13 Dec 2022"

import keypad


i2c = busio.I2C(board.GP21, board.GP20)   # SCL, SDA
# circuitpython seems to require locking the i2c bus
while i2c.try_lock():
    pass

DEFAULT_I2C_ADDR = 0x27
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def splash():
    lcd.backlight_on()
    print(version_string)
    print(release_string)
    lcd.clear()
    lcd.putstr(version_string)
    lcd.move_to(0, 1)
    lcd.putstr(release_string)
    sleep(3)
    return

base_char = [ 'b', 'o', 'd', 'h' ]
shift_char = [' ', 'f', 'g']
float_str = 'float'
arrow_overflow_right = [ 0x00, 0x08, 0x0C, 0x0E, 0x0C, 0x08, 0x00, 0x00]
arrow_overflow_left = [ 0x00, 0x02, 0x06, 0x0E, 0x06, 0x02, 0x00, 0x00]
overflow_right_flag = 1
overflow_left_flag = 2


def display_Xreg(Xreg, base, strindex):
    # lcd.clear()
    lcd.move_to(0,0)
    OFlow = 0
    if base == BASE_STATE_BIN:
        Xstr = f'{Xreg:>16b}'
    elif base == BASE_STATE_OCT:
        Xstr = f'{Xreg:>16o}'
    elif base == BASE_STATE_DEC:
        Xstr = f'{Xreg:>16}'
    elif base == BASE_STATE_HEX:
        Xstr = f'{Xreg:>16x}'.upper()

    OFlow = 0
    if len(Xstr) > 16:
        if strindex == 0:
            Xstr = Xstr[-16:]
            OFlow += overflow_left_flag
        else:
            Xstr = Xstr[-16-strindex:-strindex]
            OFlow = overflow_right_flag + overflow_left_flag
            if len(Xstr) != 16:
                OFlow -= overflow_left_flag
            while len(Xstr) < 16:
                Xstr = ' ' + Xstr
    # print(strindex, ">", Xstr, "<")
    lcd.putstr(Xstr)
    return OFlow
    
def print_calc_modes(base, shift, carry, OFlow):
    lcd.move_to(15, 1)
    lcd.putchar(base_char[base])
    lcd.move_to(1, 1)
    lcd.putchar(shift_char[shift])
    #print(base)
    
    cust_char = base_char[base]
    if OFlow & overflow_left_flag: 
        lcd.move_to(13, 1)
        lcd.custom_char(0, arrow_overflow_left)
        lcd.putchar(chr(0))
    
    if OFlow & overflow_right_flag:  
        lcd.move_to(14, 1)
        lcd.custom_char(1, arrow_overflow_right)
        lcd.putchar(chr(1))
        
    if carry:
        lcd.move_to(11, 1)
        lcd.putchar('c')
    return
    
def display_status(calc):
    lcd.clear()
    lcd.move_to(3, 0)
    lcd.putstr(f'{calc.complement}-{calc.wordSize}-{calc.flagIndicators:0{4}b}')
    return
    
def refresh_screen(calc):
    lcd.clear()
    # time.sleep(0.1)
    
    OFlow = display_Xreg(calc.Xreg, calc.base, calc.strindex)
    print_calc_modes(calc.base, calc.shift, calc.CarryBit, OFlow)
    return

def print_status(calc):
    print("\nT ", calc.Treg)
    print("Z ", calc.Zreg)
    print("Y ", calc.Yreg)
    print("X ", calc.Xreg)
    print("  ", calc.LastX, "< LastX")
    print("Base (", base_char[calc.base], "),  Shift (", shift_char[calc.shift], ")")
    # print("strindex = ", calc.strindex)

    gc.collect()
    start_mem = gc.mem_free()
    print( "Point 1 Available memory: {} bytes".format(start_mem) ) 
    return

def main_loop():

    splash()
    lcd.clear()
    
    calculator = Calculator()
    refresh_screen(calculator)
    print_status(calculator)

    while True:
        if calculator.check_timeout() and calculator.calcstate == STATE_ON:
            lcd.backlight_off()
            # print("Timed out")
            calculator.wait_keypress()
            lcd.backlight_on()
             
        calculator.check_keypress()
        
        if (calculator.key >= 0):
            key_event = getattr(calculator, key_functions[calculator.key])
            key_event(calculator.key)             
            if calculator.calcstate == STATE_OFF:
                lcd.clear()
                lcd.backlight_off()
            else:
                lcd.backlight_on()
                if calculator.showSplash:
                    splash()
                    calculator.wait_keypress()
                    calculator.showSplash = False
                if calculator.showStatus:
                    display_status(calculator)
                    calculator.wait_keypress()
                    calculator.showStatus = False
                      
                refresh_screen(calculator)
                print_status(calculator)
    return
    

#if __name__ == "__main__":
main_loop()