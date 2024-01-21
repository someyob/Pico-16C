# Pico-16C

Notes for new version 0.5:
  - added floating point entry and operations.  Note that CicruitPython only uses single precision floats, so some results will seem unexpected.  < examples follow >  I may restrict the number of decimal places (for example, entering float mode by pressing f-FLOAT-{0..9,.}, where 0 to 9 represents the number of decimal points you want to work with) to 5, even though that doesn't really mitigate the issue.  Best option would be for CircuitPython to match what Python 3 is able to handle double precision floats.  Not going to get hung up on it, as I would typically not frequently use the calculator for floating point calculations.
  - Differences between Pico16C 0.5 and the HP 16C:
      - switching from an intager base to floating point will convert what's in the X register, but the opposite is not true.
      - added a 'hidden function' to allow for a 'thousands separator' (eg. 64,636) to make readibility better for long numbers.  Unfortunately, separators do not work for binary and hex representations (eg. 1100 1100 0001, or FFEH AE12)

Wanted an HP 16C calculator, the gold standard for early programmers.  Didn't have one, too cheap to buy one off eBay, and while the new ones you can get from SwissMicro https://www.swissmicros.com/product/dm16l look great, they don't scratch my other itch, which is to play with microcontrollers and learn a new language (python).

![20221216_111350](https://user-images.githubusercontent.com/3163755/208143630-0adfedb8-aefc-4b81-bcc0-ad03d90b67fd.jpg)

Python is well suited to this application given a full suite of excellent string manipulation and math libraries, adafruit libraries, etc.  Execution speed is not an issue.

I was helped a lot during development with access to a couple of different software emulators out there (http://www.hp16c.org/ and https://stendec.io/ctb/rpn_prog.html), especially when I can see what's happening with the stack.  The manual https://literature.hpcalc.org/community/hp16c-oh-en.pdf was also essential reading.

An early version of this project got a mention on the Raspberry Pi blog https://www.raspberrypi.com/news/replica-hp-16c-coding-calculator/ and on Adafruit's Python on Hardware newsletter https://blog.adafruit.com/2022/10/19/icymi-python-on-microcontrollers-newsletter-ladyada-at-espressif-devcon-this-week-circuitpython-8-beta-2-and-more-circuitpython-icymi-raspberrypi-micropython-raspberry_pi/

![display](https://user-images.githubusercontent.com/3163755/208183857-9a8b2352-2085-4349-9562-698ef9c96bff.jpg)

Tools and materials used:
  - Raspberry Pi Pico
  - 1602 LCD display (w. i2c backpack)
  - breadboards and soldering iron
  - perfboard, w. 22awg wire
  - level shifter module (only using 2 out of 4 lines for i2c)
  - two 3x4 and one 4x4 aliexpress keypads (modified to jam as close together as possible)
  - 3d Printer
  - Glue gun
  - PTouch Labelmaker
  - Laser printer (for keypad overlay), highlighter pens
  - Thonny with Circuitpython 7.2.3
  
The software emulates (mimics) the basic operations of a 16C, all in Reverse Polish Notation (RPN) with the standard X, Y, Z and T registers.
What it's currently capable of:
  - integer entry in either hexadecimal, octal, decimal or binary
  - conversions between those bases
  - ordinary arithmatic (+ - / *), some bitwise operations (NOT, AND, etc)
  - stack operations x<->y, R^, Rv, LastX
  
Differences between this and a real 16C:
  - maximum 128 bit words (vs 16C 64 bit)
  - 16 character display, with eight 16 character windows, scrolling with shift-g < and > keys
  - 'Enter' key is standard size, not double lenth like a real 16C
  - Has a splash screen that gives you the current version number
  - Has a timeout feature that turns off the LCD after 5 minutes (hard coded)
  - The calculator is always 'running', ON and OFF simply turns off the display and backlight

Work to come in the near future:
  - floating point
  - more bitwise operations, 1's and 2's complement arithmetic

Work to come in the far future (if ever):
  - Programming mode

  
