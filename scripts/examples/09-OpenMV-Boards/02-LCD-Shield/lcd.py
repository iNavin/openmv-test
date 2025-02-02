# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# LCD Example
#
# Note: To run this example you will need a LCD Shield for your OpenMV Cam.
#
# The LCD Shield allows you to view your OpenMV Cam's frame buffer on the go.

import sensor
import display

sensor.reset()  # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565)  # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2)  # Special 128x160 framesize for LCD Shield.
lcd = display.SPIDisplay()  # Initialize the lcd screen.

while True:
    lcd.write(sensor.snapshot())  # Take a picture and display the image.
