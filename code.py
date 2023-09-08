# Write your code here :-)
import board
import digitalio
import time
import busio

score_button = digitalio.DigitalInOut(board.GP27)
score_button.direction = digitalio.Direction.INPUT
score_button.pull = digitalio.Pull.UP

ball_count_button = digitalio.DigitalInOut(board.GP14)
#intiall count button and attaches it toball_count_button.direction = digitalio.Direction.INPUT
ball_count_button.pull = digitalio.Pull.UP

ball_count_button.value
print

score_button.value
print(score_button.value)


from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Initialize the score variable
score = 0
#intializes the ball count version
ball_count = 3

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
i2c = busio.I2C(board.GP1, board.GP0) #initalizes variable isc nad attaches it to pin

# Talk to the LCD at I2C address 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)
lcd.set_backlight(True)

ball_count_button.value
while True:



    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("Pinball Wizard")
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Score: ")



    # When printing a number with this library, you need to make sure
    # to convert it to a string, otherwise you'll get an error
    # about a non-iterable being passed to print()
    lcd.print(str(score))
    time.sleep(1)


    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("Ball Count")
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Balls: ")

    lcd.print(str(ball_count))
    time.sleep(1)


    lcd.clear()
    lcd.print("Update!")
    print("Ball Count Button : " + str(ball_count_button.value))
    if score_button.value == True:
        print("Score Button is not pressed.")
        time.sleep(1)
    else:
        print("Score Button is pressed.")
        score = score + 100
    if ball_count_button.value == True:
        print("Ball Count Button is not pressed.")
        time.sleep(1)
    else:
        print("Ball Count Button is pressed.")
        ball_count = ball_count - 1
# Write your code here :-)
# Write your code here :-)
