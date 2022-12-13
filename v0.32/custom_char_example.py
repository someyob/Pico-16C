#(abandoned for somethin simpler)

dot_overflow_left = [ 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] 

base_b_char = [ 0x00, 0x10, 0x10, 0x10, 0x1C, 0x12, 0x12, 0x0C] 
base_o_char = [ 0x00, 0x00, 0x00, 0x00, 0x0C, 0x12, 0x12, 0x0C] 
base_d_char = [ 0x00, 0x02, 0x02, 0x02, 0x0E, 0x12, 0x12, 0x0C] 
base_h_char = [ 0x00, 0x10, 0x10, 0x10, 0x1C, 0x12, 0x12, 0x12] 

shift_char = [' ', 'f', 'g']
float_str = 'float'
base_char = [base_b_char, base_o_char, base_d_char, base_h_char]
dot_overflow_right = 0x01


def print_calc_modes(base, shift):
    #lcd.move_to(15, 1)
    #lcd.putchar(base_char[base])
    lcd.move_to(1, 1)
    lcd.putchar(shift_char[shift])
    #print(base)
    
    cust_char = base_char[base]
    if False:  # if overflow_right (not yet implemented)
        cust_char[0] = cust_char[0] | dot_overflow_right
    lcd.move_to(15, 1)
    lcd.custom_char(0, cust_char)
    lcd.putchar(chr(0))
    
    if False:  # if overflow_left (not yet impelemented)
        lcd.move_to(14, 1)
        lcd.custom_char(1, dot_overflow_left)
        lcd.putchar(chr(1))
    return