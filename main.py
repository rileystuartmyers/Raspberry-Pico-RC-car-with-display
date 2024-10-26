import time
from servo import Servo
from machine import Pin, freq, I2C
from print_error import print_error
from pico_i2c_lcd import I2cLcd
from nec import NEC_8

display_arm = Servo(pin_id = 19)
display_arm.write(90)
my_servo = Servo(pin_id=22)
my_servo_2 = Servo(pin_id = 20)
pin_ir = Pin(17, Pin.IN)

#orange = sda
#yellow = scl

motion_sensor = Pin(18, Pin.IN, Pin.PULL_DOWN)
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def decodeKeyValue(data):
    if data == 0x16:
        return "0"
    if data == 0x0C:
        return "1"
    if data == 0x18:
        return "2"
    if data == 0x5E:
        return "3"
    if data == 0x08:
        return "4"
    if data == 0x1C:
        return "5"
    if data == 0x5A:
        return "6"
    if data == 0x42:
        return "7"
    if data == 0x52:
        return "8"
    if data == 0x4A:
        return "9"
    if data == 0x09:
        return "+"
    if data == 0x15:
        return "-"
    if data == 0x7:
        return "EQ"
    if data == 0x0D:
        return "U/SD"
    if data == 0x19:
        return "CYCLE"
    if data == 0x44:
        return "PLAY/PAUSE"
    if data == 0x43:
        return "FORWARD"
    if data == 0x40:
        return "BACKWARD"
    if data == 0x45:
        return "POWER"
    if data == 0x47:
        return "MUTE"
    if data == 0x46:
        return "MODE"
    return "ERROR"

def motion_detected(pin):
    
    for y in range(10):
        
        for x in range(90):
            
            my_servo.write(x)
            
        for x in range(90, 0, -1):
            
            my_servo.write(x)
            
        time.sleep(0.15)

def callback(data, addr, ctrl):
    
    if data < 0:
        
        pass
    
    elif data == 0x46: #MODE
       
        my_servo.write(150)
        my_servo_2.write(30)
        
    elif data == 0x40: #BACKWARD
            
       my_servo.write(90)
       my_servo_2.write(90)
            
    elif data == 0x15: #-
        
        my_servo.write(30)
        my_servo_2.write(150)
            
    elif data == 0x44: #PLAY/PAUSE
            
        my_servo.write(75)
        my_servo_2.write(75)
            
    elif data == 0x43: #FORWARD
        
        my_servo.write(105)
        my_servo_2.write(105)
            
    elif data == 0x45: #POWER
        
        display_arm_position = display_arm.read() // 1 - 20
        
        if (display_arm_position <= 0):
            
            display_arm_position = 0
            
        display_arm.write(display_arm_position)
        
    elif data == 0x47: #MUTE
        
        display_arm_position = display_arm.read() // 1 + 20
        
        if (display_arm_position >= 180):
            
            display_arm_position = 180
            
        display_arm.write(display_arm_position)
        
    elif data == 7: #EQ
        
        lcd.clear()
        lcd.putstr("      O O              v")    

    elif data == 0x09: #+
        
        lcd.clear()
        lcd.putstr("      _ _              v")    

    print(data)
    
ir = NEC_8(pin_ir, callback)  # Instantiate receiver
ir.error_function(print_error)  # Show debug information

try:
    while True:    
        pass
except KeyboardInterrupt:
    ir.close()
