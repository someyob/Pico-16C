

import time
import board
import busio
from time import sleep, monotonic
from circuitpython_i2c_lcd import I2cLcd
from PICO_16C_keypad import *

version_string = "KJ-16C v0.2"
release_string = "12 April 2022"

import keypad
DEFAULT_I2C_ADDR = 0x27
i2c = busio.I2C(board.GP21, board.GP20)   # SCL, SDA

# circuitpython seems to require locking the i2c bus
while i2c.try_lock():
    pass

# 2 lines, 16 characters per line
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)


base_char = [ 'd', 'h', 'o', 'b' ]
shift_char = [' ', 'f', 'g']
    
keys_char = [ '0', '1', '4', '7', '.', '2', '5', '8', '~', '3', '6', '9', '+', '-', 'x', '/' ]
# (4, 0, 1, 5, 9, 2, 6, 10, 3, 7, 11 )  # .0123456789
km = keypad.KeyMatrix( 
    row_pins=(board.GP19, board.GP18, board.GP17, board.GP16),
    column_pins=(board.GP15, board.GP14, board.GP13, board.GP12),
)



def print_calc_modes(base, shift):
    lcd.move_to(15, 1)
    lcd.putchar(base_char[base])
    lcd.move_to(1, 1)
    lcd.putchar(shift_char[shift])
    #print(base)
    return

def display_Xreg(Xreg):
    # lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(Xreg))
    return

def refresh_screen(Xreg, base, shift):
    lcd.clear()
    time.sleep(0.1)
    print_calc_modes(base, shift)
    display_Xreg(Xreg)
    return

def print_registers(Xreg, Yreg):
    print("===============")
    print("Y: ", Yreg)
    print("X: ", Xreg)
    return

def test_main():
    """Test function for verifying basic functionality."""
    print(version_string)
    print(release_string)

    lcd.clear()
    lcd.putstr(version_string)
    lcd.move_to(0, 1)
    lcd.putstr(release_string)
    
    sleep(3)
    lcd.clear()
    
    num_keys = (KP_DECIMAL_PT,KP_ZERO,KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN, KP_EIGHT, KP_NINE)
    operator_keys = (KP_ADD, KP_SUBTRACT, KP_MULTIPLY, KP_DIVIDE)  # +-x/

    base = 0   # 0=dec, 1=hex, 2=oct, 3=bin
    shift = 0  # 0=none, 1=f, 2=g
    print_calc_modes(base, shift)
    
    Xbuff = ""
    Xreg = 0
    Yreg = 0
    starting_entry = True
    display_Xreg(Xreg)
    print_registers(Xreg, Yreg)
    
    while True:
        event = km.events.get()

        if event:
            if event.pressed:
                
                # print(event.key_number, keys_char[event.key_number])
                if event.key_number in num_keys:
                    # print(" num key")
                    # lcd.putchar(keys_char[event.key_number])
                    if starting_entry:
                        Yreg = Xreg
                        starting_entry = False
                        refresh_screen(Xreg, base, shift)
                    Xbuff = Xbuff + keys_char[event.key_number];
                    Xreg = int(Xbuff)
                    # print(Xreg)
                    display_Xreg(Xreg)  # lcd.putstr(Xbuff)
                    
                elif event.key_number == KP_ENTER:
                    # print(" enter")  # temp using hash-key as proxy for other keys
                    Xbuff = ""
                    Yreg = Xreg
                    starting_entry = True
                    refresh_screen(Xreg, base, shift)
                elif event.key_number == KP_ADD: # '+'
                    Xreg = Xreg+Yreg
                    Yreg = 0
                    Xbuff = ""
                    refresh_screen(Xreg, base, shift)
                    starting_entry = True
                elif event.key_number == KP_SUBTRACT: # '-'
                    if not starting_entry:
                        Xbuff = '-' + Xbuff
                        Xreg = int(Xbuff)
                        refresh_screen(Xreg, base, shift)
                    else:
                        Xreg = Yreg-Xreg
                        Yreg = 0
                        Xbuff = ""
                        refresh_screen(Xreg, base, shift)
                        starting_entry = True
                elif event.key_number == KP_MULTIPLY: # 'x'
                    Xreg = Yreg*Xreg
                    Yreg = 0
                    Xbuff = ""
                    refresh_screen(Xreg, base, shift)
                    starting_entry = True
                elif event.key_number == KP_DIVIDE: # '/'
                    Xreg = Yreg // Xreg
                    Yreg = 0
                    Xbuff = ""
                    refresh_screen(Xreg, base, shift)
                    starting_entry = True
                print_registers(Xreg, Yreg)
    

#if __name__ == "__main__":
test_main()