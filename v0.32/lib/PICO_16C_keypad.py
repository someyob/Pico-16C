#  KEYPAD CONSTANTS
KP_DECIMAL_PT = 32
KP_STATUS = KP_DECIMAL_PT + 40
KP_NE_ZERO = KP_DECIMAL_PT + 80

KP_ZERO = 33
KP_MEM = KP_ZERO + 40
KP_NE_Y = KP_ZERO + 80

KP_ONE = 23
KP_ONES_COMP = KP_ONE + 40
KP_LE_Y = KP_ONE + 80

KP_TWO = 22
KP_TWOS_COMP = KP_TWO + 40
KP_LT_ZERO = KP_TWO + 80

KP_THREE = 21
KP_UNSGN = KP_THREE + 40
KP_GT_Y = KP_THREE + 80

KP_FOUR = 13
KP_SB = KP_FOUR + 40
KP_SF = KP_FOUR + 80

KP_FIVE = 12
KP_CB = KP_FIVE + 40
KP_CF = KP_FIVE + 80

KP_SIX = 11
KP_BQ = KP_SIX + 40
KP_FQ = KP_SIX + 80

KP_SEVEN = 3
KP_MASKL = KP_SEVEN + 40
KP_NUM_B = KP_SEVEN + 80

KP_EIGHT = 2
KP_MASKR = KP_EIGHT + 40
KP_ABS = KP_EIGHT + 80

KP_NINE = 1
KP_RMD = KP_NINE + 40
KP_DBLR = KP_NINE + 80

KP_A = 9
KP_SL = KP_A + 40
KP_LJ = KP_A + 80

KP_B = 8
KP_SR = KP_B + 40
KP_ASR = KP_B + 80

KP_C = 7
KP_RL = KP_C + 40
KP_RLC = KP_C + 80

KP_D = 6
KP_RR = KP_D + 40
KP_RRC = KP_D + 80

KP_E = 5
KP_RLn = KP_E + 40
KP_RLCn = KP_E + 80

KP_F = 4
KP_RRn = KP_F + 40
KP_RRCn = KP_F + 80

# ARITHMETIC Operators
KP_ADD = 30
KP_OR = KP_ADD + 40
KP_EQ_ZERO = KP_ADD + 80

KP_SUBTRACT = 20
KP_NOT = KP_SUBTRACT + 40
KP_GT_ZERO = KP_SUBTRACT + 80

KP_MULTIPLY = 10
KP_AND = KP_MULTIPLY + 40
KP_DBLMULT = KP_MULTIPLY + 80

KP_DIVIDE = 0
KP_XOR = KP_DIVIDE + 40
KP_DBLDIV = KP_DIVIDE + 80

KP_CHS = 31
KP_EEX = KP_CHS + 40
KP_EQ_Y = KP_CHS + 80

# Enter
KP_ENTER = 34
KP_LST_X = KP_ENTER + 80

KP_ENTER2 = 24
KP_WINDOW = KP_ENTER2 + 40

KP_BIN = 14
KP_SHOW_BIN = KP_BIN + 40
KP_ONE_OVER_X = KP_BIN + 80

KP_OCT = 15
KP_SHOW_OCT = KP_OCT + 40
KP_SQRT_X = KP_OCT + 80

KP_DEC = 16
KP_SHOW_DEC = KP_DEC + 40
KP_ISZ = KP_DEC + 80

KP_HEX = 17
KP_SHOW_HEX = KP_HEX + 40
KP_DSZ = KP_HEX + 80

KP_BSP = 25
KP_CLR_PREFIX = KP_BSP + 40
KP_CLx = KP_BSP + 80

KP_XY = 26
KP_CLR_REG = KP_XY + 40
KP_PSE = KP_XY + 80

KP_RDN = 27
KP_CLR_PGM = KP_RDN + 40
KP_RUP = KP_RDN + 80

KP_SST = 28
KP_I = KP_SST + 40
KP_BST = KP_SST + 80

KP_RS = 29
KP_I_BR = KP_RS + 40
KP_PR = KP_RS + 80

KP_GSB = 19
KP_XI_BR = KP_GSB + 40
KP_RTN = KP_GSB + 80

KP_GTO = 18
KP_XI = KP_GTO + 40
KP_LBL = KP_GTO + 80

KP_RCL = 35
KP_FLOAT = KP_RCL + 40
KP_DISP_R = KP_RCL + 80

KP_STO = 36
KP_WSIZE = KP_STO + 40
KP_DISP_L = KP_STO + 80

KP_SHIFT_F = 38
KP_SHIFT_G = 37

KP_ON = 39



##########################################################

keys_char = [ '/',  '9',   '8',  '7',  'F',     'E',   'D',   'C',   'B',   'A',
              '*',  '6',   '5',  '4',  'BIN',   'OCT', 'DEC', 'HEX', 'GTO', 'GSB',
              '-',  '3',   '2',  '1',  'E2',    'BSP', 'XY',  'RD',  'SST', 'RS',
              '+',  'CHS', '.',  '0',  'ENTER', 'RCL', 'STO', 'g',   'f',   'ON']

key_functions = [ 'f_mathOp', 'f_digit', 'f_digit', 'f_digit', 'f_digit', 'f_digit', 'f_digit', 'f_digit', 'f_digit', 'f_digit',
                  'f_mathOp', 'f_digit', 'f_digit', 'f_digit', 'f_base',  'f_base',  'f_base',  'f_base',  'f_undef', 'f_undef',
                  'f_mathOp', 'f_digit', 'f_digit', 'f_digit', 'f_undef', 'f_BSP',   'f_XY',    'f_rolld', 'f_undef', 'f_undef',
                  'f_mathOp', 'f_CHS',   'f_digit', 'f_digit', 'f_ENTER', 'f_undef', 'f_undef', 'f_shift', 'f_shift', 'f_ON',
 # shift f:                 
                  'f_mathOp', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef',
                  'f_mathOp', 'f_undef', 'f_undef', 'f_undef', 'f_base',  'f_base',  'f_base',  'f_base',  'f_undef', 'f_undef',
                  'f_mathOp', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef',
                  'f_mathOp', 'f_undef', 'f_stat',  'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_shift', 'f_shift', 'f_ON',
 # shift g:                 
                  'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef',
                  'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_undef',
                  'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_splsh', 'f_CLx',   'f_undef', 'f_rollu', 'f_undef', 'f_undef',
                  'f_undef', 'f_undef', 'f_undef', 'f_undef', 'f_LastX', 'f_pan_d', 'f_pan_d', 'f_shift', 'f_shift', 'f_ON']

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
show_base_conversion_keys = (KP_SHOW_BIN, KP_SHOW_OCT, KP_SHOW_DEC, KP_SHOW_HEX)

STATE_OFF = 0
STATE_ON = 1

SHIFT_STATE_OFF = 0
SHIFT_STATE_F = 1
SHIFT_STATE_G = 2

BASE_STATE_BIN = 0
BASE_STATE_OCT = 1
BASE_STATE_DEC = 2
BASE_STATE_HEX = 3

MAX_WORD_SIZE = 128

LEAD_ZERO_FLAG = 8
USER_FLAG_2 = 4
USER_FLAG_1 = 2
USER_FLAG_0 = 1

class Calculator():
    
    def __init__(self):
        self.name = 'Pico 16C'
        self.key = 0
        self.base = BASE_STATE_DEC
        self.shift = SHIFT_STATE_OFF
        self.calcstate = STATE_ON
        self.Xbuff = ""
        self.Xreg = 0
        self.Yreg = 0
        self.Zreg = 0
        self.Treg = 0
        self.LastX = 0
        self.wordSize = MAX_WORD_SIZE		# HP 16C has max = 64 bits
        self.complement = 2
        self.entry_in_progress = False
        self.flagIndicators = 0
        self.CarryBit = False
        self.OutOfRange = False
        self.strindex = 0
        self.showSplash = False
        self.showStatus = False
        return
        
    def clear_shift(self):
        self.shift = SHIFT_STATE_OFF
        return
    
    def f_splsh(self, key):
        self.shift = SHIFT_STATE_OFF
        self.showSplash = True
        return
    
    def f_stat(self, key):
        self.shift = SHIFT_STATE_OFF
        self.showStatus = True
        return
    
    def f_undef(self, key):
        #print(self.name + ' key undefined ' + str(key))
        self.shift = SHIFT_STATE_OFF
        return
        
    def f_digit(self, key):
        #print(' f_digit ' + str(key))
        
        if self.base == BASE_STATE_BIN and key in bin_num_keys:
            if not self.entry_in_progress:
                self.Xbuff = ""
                self.Yreg = self.Xreg
                self.Xreg = 0
            self.entry_in_progress = True
            self.Xbuff = self.Xbuff + keys_char[key]
            # print(self.Xbuff)
            self.Xreg = int(self.Xbuff, 2)
        elif self.base == BASE_STATE_OCT and key in oct_num_keys:
            if not self.entry_in_progress:
                self.Xbuff = ""
                self.Yreg = self.Xreg
                self.Xreg = 0
            self.entry_in_progress = True
            self.Xbuff = self.Xbuff + keys_char[key]
            # print(self.Xbuff)
            self.Xreg = int(self.Xbuff, 8)
        elif self.base == BASE_STATE_DEC and key in dec_num_keys:
            if not self.entry_in_progress:
                self.Xbuff = ""
                self.Yreg = self.Xreg
                self.Xreg = 0
            self.entry_in_progress = True
            self.Xbuff = self.Xbuff + keys_char[key]
            # print(self.Xbuff)
            self.Xreg = int(self.Xbuff)
        elif self.base == BASE_STATE_HEX and key in hex_num_keys:
            if not self.entry_in_progress:
                self.Xbuff = ""
                self.Xreg = 0
            self.entry_in_progress = True
            self.Xbuff = self.Xbuff + keys_char[key]
            # print(self.Xbuff)
            self.Xreg = int(self.Xbuff, 16)
        self.shift = SHIFT_STATE_OFF
        print('Bit length = ', self.Xreg.bit_length())
        return
    
    def f_mathOp(self, key):
        #print(self.name + ' f_mathOp ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.LastX = self.Xreg
        if key == KP_ADD:
            self.Xreg = self.Yreg + self.Xreg
        elif key == KP_SUBTRACT:
            self.Xreg = self.Yreg - self.Xreg
        elif key == KP_MULTIPLY:
            self.Xreg = self.Yreg * self.Xreg
        elif key == KP_DIVIDE:  # need to account for FP ops
            self.Xreg = self.Yreg // self.Xreg
        elif key == KP_OR:
            self.Xreg = self.Yreg | self.Xreg
        elif key == KP_NOT:
            num_bits = self.Xreg.bit_length()
            self.Xreg = (~self.Xreg) & (2**num_bits-1)   # need to check stack ops for unary operators
        elif key == KP_AND:
            self.Xreg = self.Yreg & self.Xreg
        elif key == KP_XOR:
            self.Xreg = self.Yreg ^ self.Xreg
        self.Yreg = self.Zreg
        self.Zreg = self.Treg
        # self.Treg = 0    # Manual page 22, Treg is regenerated for re-use
        self.entry_in_progress = False
        return
    
    def f_CLx(self, key):
        #print(self.name + ' f_CLx ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.Xreg = 0
        self.entry_in_progress = False
        return
    
    def f_LastX(self, key):
        #print(self.name + ' f_LastX ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.Yreg = self.Xreg
        self.Xreg = self.LastX
        self.entry_in_progress = False
        return
    
    def f_BSP(self, key):
        if self.entry_in_progress:
            self.Xbuff = self.Xbuff[:-1]
            if len(self.Xbuff) == 0:
                self.Xreg = 0
                self.entry_in_progress = False
            else:
                # print(self.Xbuff)
                if self.base == BASE_STATE_HEX:
                    self.Xreg = int(self.Xbuff, 16)
                elif self.base == BASE_STATE_DEC:
                    self.Xreg = int(self.Xbuff)
                elif self.base == BASE_STATE_OCT:
                    self.Xreg = int(self.Xbuff, 8)
                elif self.base == BASE_STATE_BIN:
                    self.Xreg = int(self.Xbuff, 2)
        else:  # treat as CLx
            self.shift = SHIFT_STATE_OFF
            self.Xreg = 0
            self.entry_in_progress = False
        return
    
    def f_XY(self, key):
        #print(self.name + ' f_XY ' + str(key))
        temp = self.Yreg 
        self.Yreg = self.Xreg
        self.Xreg = temp
        self.entry_in_progress = False
        return
    
    def f_base(self, key):
        #print(self.name + ' f_base ' + str(key))
        if key >= 40:
            key -= 40
        self.shift = SHIFT_STATE_OFF
        if self.calcstate == STATE_ON:
            if key == KP_BIN:
                self.base = BASE_STATE_BIN
            elif key == KP_OCT:
                self.base = BASE_STATE_OCT
            elif key == KP_DEC:
                self.base = BASE_STATE_DEC
            else:  # KP_HEX
                self.base = BASE_STATE_HEX
        self.entry_in_progress = False
        return
    
    def f_CHS(self, key):
        #print(self.name + ' f_CHS ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.entry_in_progress = False
        self.LastX = self.Xreg
        self.Xreg = -self.Xreg
        return
    
    def f_ENTER(self, key):
        #print(self.name + ' f_ENTER ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.entry_in_progress = False
        self.Treg = self.Zreg
        self.Zreg = self.Yreg
        self.Yreg = self.Xreg
        return
    
    def f_rolld(self, key):
        #print(self.name + ' f_ENTER ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.entry_in_progress = False
        temp = self.Xreg
        self.Xreg = self.Yreg
        self.Yreg = self.Zreg
        self.Zreg = self.Treg
        self.Treg = temp
        return
    
    def f_rollu(self, key):
        #print(self.name + ' f_ENTER ' + str(key))
        self.shift = SHIFT_STATE_OFF
        self.entry_in_progress = False
        temp = self.Treg
        self.Treg = self.Zreg
        self.Zreg = self.Yreg
        self.Yreg = self.Xreg
        self.Xreg = temp
        return
    
    def f_shift(self, key):
        if self.calcstate == STATE_ON:
            if self.shift == SHIFT_STATE_F:
                key -= 40
            if self.shift == SHIFT_STATE_G:
                key -= 80
            # print(self.name + ' f_shift ' + str(key))
            if key == KP_SHIFT_F:
                self.shift = SHIFT_STATE_F
            else: # key == KP_SHIFT_G:
                self.shift = SHIFT_STATE_G
        return
    
    def f_pan_d(self, key):
        if key == KP_DISP_L:
            self.strindex += 1
        elif key == KP_DISP_R:
            if self.strindex > 0:
                self.strindex -= 1
        self.shift = SHIFT_STATE_OFF
        return
    
    def f_ON(self, key):
        #print(self.name + ' f_ON ' + str(key))
        if self.calcstate == STATE_ON:
            self.calcstate = STATE_OFF
        else:
            self.calcstate = STATE_ON
        self.shift = SHIFT_STATE_OFF
        return