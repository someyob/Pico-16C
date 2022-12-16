# Pico-16C

Wanted an HP 16C calculator, the gold standard for early programmers.  Didn't have one, too cheap to buy one off eBay, and while the new ones you can get from SwissMicro https://www.swissmicros.com/product/dm16l look great, they don't scratch my other itch, which is to play with microcontrollers and learn a new language (python).

![20221216_111350](https://user-images.githubusercontent.com/3163755/208143630-0adfedb8-aefc-4b81-bcc0-ad03d90b67fd.jpg)

Tools and materials used:
  - Raspberry Pi Pico
  - breadboards and soldering iron
  - perfboard, w. 22awg wire
  level shifter module
  two 3x4 and one 4x4 aliexpress keypads (modified to jam as close together as possible)
  3d Printer
  Glue gun
  PTouch Labelmaker
  Laser printer (for keypad overlay), highlighter pens
  Thonny with Circuitpython 7.2.3
  
The software emulates (mimics) the basic operations of a 16C, all in Reverse Polish Notation (RPN) with the standard X, Y, Z and T registers.
What it's currently capable of:
  integer entry in either hexadecimal, octal, decimal or binary
  conversions between those bases
  ordinary arithmatic (+ - / *), some bitwise operations (NOT, AND, etc)
  stack operations x<->y, R^, Rv
  
Differences between this and a real 16C:
  maximum 128 bit words (vs 16C 64 bit)
  16 character display, with eight 16 character windows, scrolling with shift-g < and > keys
  'Enter' key is standard size, not double lenth like a real 16C
  
