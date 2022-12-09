# version to test out classes

import time
import board
import busio
from time import sleep, monotonic
from circuitpython_i2c_lcd import I2cLcd
from PICO_16C_keypad import *


version_string = "Pico 16C v0.23"
release_string = "28 Nov 2022"

import keypad

i2c = busio.I2C(board.GP21, board.GP20)   # SCL, SDA
# circuitpython seems to require locking the i2c bus
while i2c.try_lock():
    pass

DEFAULT_I2C_ADDR = 0x27
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

km = keypad.KeyMatrix( 
    row_pins=(board.GP2, board.GP3, board.GP4, board.GP5), 
    column_pins=(board.GP15, board.GP14, board.GP13, board.GP12,
                 board.GP10, board.GP11, board.GP9,
                 board.GP7, board.GP8, board.GP6)
)

def splash():
    lcd.backlight_on()
    print(version_string)
    print(release_string)
    lcd.clear()
    lcd.putstr(version_string)
    lcd.move_to(0, 1)
    lcd.putstr(release_string)
    sleep(3)


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
        #print(len(f'{Xreg:b}'))
        Xstr = f'{Xreg:>16b}'
    elif base == BASE_STATE_OCT:
        #print(len(f'{Xreg:o}'))
        Xstr = f'{Xreg:>16o}'
    elif base == BASE_STATE_DEC:
        #print(len(f'{Xreg}'))
        Xstr = f'{Xreg:>16}'
    elif base == BASE_STATE_HEX:
        #print(len(f'{Xreg:x}'))
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
    print(strindex, ">", Xstr, "<")
    lcd.putstr(Xstr)
    return OFlow
    
def print_calc_modes(base, shift, OFlow):
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
    
    if OFlow & overflow_right_flag:  # if overflow_right (not yet impelemented)
        lcd.move_to(14, 1)
        lcd.custom_char(1, arrow_overflow_right)
        lcd.putchar(chr(1))
    return
    

def refresh_screen(Xreg, base, shift, strindex):
    lcd.clear()
    # time.sleep(0.1)
    
    OFlow = display_Xreg(Xreg, base, strindex)
    print_calc_modes(base, shift, OFlow)
    return

def print_status(Xreg, Yreg, Treg, base, shift):
    print("\nX ", Xreg, "  Y ", Yreg, "  T ", Treg)
    print("Base ", base, "  Shift ", shift)

def test_main():

    splash()
    lcd.clear()
    lcd.backlight_off()
    calculator = Calculator()

    while True:
        event = km.events.get()
        if event:
            if event.pressed:
                # print(event.key_number, key_functions[event.key_number]) # calc.keypressed(event.key_number)
                
                key_pressed = event.key_number
                if calculator.shift == SHIFT_STATE_F:
                    key_pressed += 40
                elif calculator.shift == SHIFT_STATE_G:
                    key_pressed += 80
                
                key_event = getattr(calculator, key_functions[key_pressed])
                key_event(key_pressed)             
                if calculator.calcstate == STATE_OFF:
                    lcd.clear()
                    lcd.backlight_off()
                else:
                    # splash()
                    lcd.backlight_on()
                    refresh_screen(calculator.Xreg, calculator.base, calculator.shift,
                                   calculator.strindex)
                    print_status(calculator.Xreg, calculator.Yreg, calculator.Treg,
                                 calculator.base, calculator.shift)
                  
    

#if __name__ == "__main__":
test_main()