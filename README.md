# Raspberry Pico RC car with display

 <p float = "left">
  <img src = "https://github.com/rileystuartmyers/Raspberry-Pico-RC-car-with-display/blob/ffb5ffe8d5bb3453c63528d39f2ea3c620a5099f/movement_gif.gif" width = 600 height = 500>
 </p>

# How it works

 <p>
  The project makes use of several different modules including continuous-movement servos, an LCD screen, and plenty of wiring.
  The pico performs all necessary reading of inputs and communication with hardware in the main.py file.

  As input, the RC car uses an IR remote (originally intended for LED lights) and is controlled through use of its buttons.
  It's capable of four-directional movement and complete continuous rotation, along with the ability to flash faces onto the LCD, such
  as a resting, blinking, or surprised emoticon face.  0 v 0  =>  - v -

  Both servos and the LCD are connected via a breadboard to the pico's 3v3 power output, GPIO, and ground pins in order to complete their circuits.
  The entire project is powered by 4xAA batteries.
  
 </p>

 # Parts List

  * 1x  Raspberry Pi Pico
  * 1x  16x2 Digital LCD Display
  * 2x  Continuous-Rotation Servo Motor
  * 1x  IR Receiver
  * 1x  IR Remote
  * 1x Blank PCB
  * 4x 1.5V AA Batteries
  * 1x Flat Wooden/Cardboard Platform
  * ~  Solder
  * ~  Appropriate number of Dupont and Jumper Cables
 
# Board Schema

 <p float = "left">
  <img src = "https://github.com/rileystuartmyers/Raspberry-Pico-RC-car-with-display/blob/650f0e7681261073e60a8d31d87e2fcc29cd55f5/IMG_8870.JPG" width = 850 height = 500>
 </p>

# More Images

 <p float = "left">
  <img src = "https://github.com/rileystuartmyers/Raspberry-Pico-RC-car-with-display/blob/ffb5ffe8d5bb3453c63528d39f2ea3c620a5099f/IMG_8980.jpeg" width = 250 height = 250>
  <img src = "https://github.com/rileystuartmyers/Raspberry-Pico-RC-car-with-display/blob/ffb5ffe8d5bb3453c63528d39f2ea3c620a5099f/IMG_8981.jpeg" width = 250 height = 250>
  <img src = "https://github.com/rileystuartmyers/Raspberry-Pico-RC-car-with-display/blob/ffb5ffe8d5bb3453c63528d39f2ea3c620a5099f/IMG_8982.jpeg" width = 250 height = 250>
 </p>
