# Imports
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Extras for Encoder and LEDs
from kmk.modules.encoder import Encoder
from kmk.extensions.RGB import RGB

# Initialize Keyboard
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# --- 1. SWITCH PINS & DEFINITIONS ---
# Mapping based on your specific physical pins:
# SW1=Pin 8(RX), SW2=Pin 9(SCK), SW3=Pin 10(MISO), SW4=Pin 11(MOSI), EncSwitch=Pin 1(A0)
PINS = [
    board.RX,    # SW1
    board.SCK,   # SW2
    board.MISO,  # SW3
    board.MOSI,  # SW4
    board.A0     # Rotary Encoder Switch (S1)
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True, # Internal pull-ups enabled
)

# --- 2. ROTARY ENCODER ROTATION ---
# Pin 7 (TX) -> A
# Pin 6 (SCL) -> B
keyboard.modules.append(Encoder(
    (board.TX, board.SCL, 2), # (Pin A, Pin B, Divisor)
    key_keys=(
        KC.VOLU, # Clockwise
        KC.VOLD, # Counter-Clockwise
        KC.NO,   # Button handled in PINS above
    )
))

# --- 3. RGB LEDS ---
# Pin 5 (SDA) -> LED Data
keyboard.extensions.append(RGB(
    rgb_pin=board.SDA,
    num_pixels=2,
    initial_val=20, # Low brightness
    initial_hue=0,
    initial_sat=255
))

# --- 4. KEYMAP ---
# SW1=Copy, SW2=Paste, SW3="sybau", SW4="fr"
keyboard.keymap = [
    [
        # SW1: Copy (Ctrl + C)
        KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),
        
        # SW2: Paste (Ctrl + V)
        KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
        
        # SW3: Type "sybau"
        KC.MACRO("sybau"),
        
        # SW4: Type "fr"
        KC.MACRO("fr"),
        
        # Encoder Switch: Mute
        KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()