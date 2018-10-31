from pad4pi import rpi_gpio
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()

KEYPAD= [ [1,2,3,"A"],
           [4,5,6,"B"],
           [7,8,9,"C"],
           ["*",0,"#","D"]]

#gpio pin numbers
ROW=[7,11,13,15]
COL=[12,16,18,22]

count=0

def printKey(key):
            print key

try:
    while(count<10):
        factory=rpi_gpio.KeypadFactory()
        keypad=factory.create_keypad(keypad=KEYPAD,row_pins=ROW,col_pins=COL)

        
        keypad.registerKeyPressHandler(printKey)
        count+=1
    keypad.cleanup()    
except KeyboardInterrupt:
    GPIO.cleanup()


