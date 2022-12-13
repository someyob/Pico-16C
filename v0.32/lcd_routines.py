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
