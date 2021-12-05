import gc
import time
import math
import json
import board
import busio
import displayio
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal
Mbackground='/bmps/dk.bmp'

BITPLANES = 6      # Ideally 6, but can set lower if RAM is tight
MATRIX = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True, bit_depth=BITPLANES)
DISPLAY = MATRIX.display
FILENAME = Mbackground

FONT = "/fonts/IBMPlexMono-Medium-24_jep.bdf"

MATRIX.add_text(
    text_font=FONT,
    text_position=(13, 12),
    text_color=(0xC0C0C0),
    text_scale=.4,
    scrolling=True,
)


# Static 'Connecting' Text
MATRIX.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (MATRIX.graphics.display.height // 2) - 1),
)

SCROLL_DELAY = 0.03

while True:
    MATRIX.set_background(FILENAME)
    time.sleep(1)
    MATRIX.set_background(0x0)
    MATRIX.set_text('Donkey Kong December')
    MATRIX.set_text_color('#9c5d05')
    MATRIX.scroll_text(SCROLL_DELAY)
    MATRIX.set_background(0x0)
    MATRIX.set_background('/bmps/dk1.bmp')
    time.sleep(1.5)
    MATRIX.set_background(0x0)
    #time.sleep(1)
