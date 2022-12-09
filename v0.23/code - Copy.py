

import time
import board
import busio
from time import sleep, monotonic
from circuitpython_i2c_lcd import I2cLcd
from PICO_16C_keypad import *

version_string = "Pico 16C v0.1"
release_string = "2 Sep 2022"

import keypad

DEFAULT_I2C_ADDR = 0x27
i2c = busio.I2C(board.GP21, board.GP20)   # SCL, SDA

# circuitpython seems to require locking the i2c bus
while i2c.try_lock():
    pass

# 2 lines, 16 characters per line
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

keys_char = [ '/', '9', '8', '7', 'F', 'E', 'D', 'C', 'B', 'A',
              '*', '6', '5', '4', 'BIN', 'OCT', 'DEC', 'HEX', 'GTO', 'GSB',
              '-', '3', '2', '1', 'E2', 'BSP', 'XY', 'RD', 'SST', 'RS',
              '+', 'CHS', '.', '0', 'ENTER', 'RCL', 'STO', 'g', 'f', 'ON']

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

km = keypad.KeyMatrix( 
    row_pins=(board.GP2, board.GP3, board.GP4, board.GP5), 
    column_pins=(board.GP15, board.GP14, board.GP13, board.GP12,
                 board.GP10, board.GP11, board.GP9,
                 board.GP7, board.GP8, board.GP6)
)

base_char = [ 'b', 'o', 'd', 'h' ]
shift_char = [' ', 'f', 'g']
float_str = 'float'

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
    
    base = 3   # 0=bin, 1=oct, 2=dec, 3=hex, 4=float
    shift = 0  # 0=none, 1=f, 2=g
    print_calc_modes(base, shift)
    
    bin_num_keys = (KP_ZERO, KP_ONE)
    oct_num_keys = (KP_ZERO, KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN)
    dec_num_keys = (KP_ZERO, KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN, KP_EIGHT, KP_NINE)
    hex_num_keys = (KP_ZERO, KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN, KP_EIGHT, KP_NINE,
                    KP_A, KP_B, KP_C, KP_D, KP_E, KP_F)
    float_num_keys = (KP_DECIMAL_PT, KP_ZERO, KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN, KP_EIGHT, KP_NINE)
    all_num_keys = (KP_DECIMAL_PT, KP_ZERO, KP_ONE, KP_TWO, KP_THREE, KP_FOUR, KP_FIVE, KP_SIX, KP_SEVEN, KP_EIGHT, KP_NINE,
                    KP_A, KP_B, KP_C, KP_D, KP_E, KP_F)
    operator_keys = (KP_ADD, KP_SUBTRACT, KP_MULTIPLY, KP_DIVIDE)  # +-x/
    base_keys = (KP_BIN, KP_OCT, KP_DEC, KP_HEX)
    
    Xbuff = ""
    Xreg = 0
    Yreg = 0
    starting_entry = True
    display_Xreg(Xreg)
    
    while True:
        event = km.events.get()

        if event:
            if event.pressed:
                print(event.key_number, ', "', keys_char[event.key_number], '"')
                if event.key_number == KP_ON:
                    if lcd.backlight:
                        lcd.backlight_off()
                    else:
                        lcd.backlight_on()
                elif event.key_number in base_keys:
                    base = event.key_number - KP_BIN   # sequence starts at KP_BIN
                    print_calc_modes(base, shift)
                elif event.key_number == KP_F:
                    shift = 1
                    print_calc_modes(base, shift)
                elif event.key_number == KP_G:
                    shift = 2
                    print_calc_modes(base, shift)
                elif base == 2 and event.key_number in dec_num_keys:
                    if starting_entry:
                        Yreg = Xreg
                        starting_entry = False
                        refresh_screen(Xreg, base, shift)
                    Xbuff = Xbuff + keys_char[event.key_number]
                    Xreg = int(Xbuff)
                    print(Xreg)
                    display_Xreg(Xreg)
                elif event.key_number == KP_BSP:
                    if starting_entry:
                        Xreg = 0
                    else:
                        print('buff', Xbuff, len(Xbuff))
                        Xbuff = Xbuff[:-1]
                        if len(Xbuff) == 0:
                            Xbuff = '0'
                        Xreg = int(Xbuff)
                    print(Xreg)
                    refresh_screen(Xreg, base, shift)
                        
                    
                  
    

#if __name__ == "__main__":
test_main()