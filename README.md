# 🎹 My Custom XIAO RP2040 Macropad

A custom 4-key macropad with a rotary encoder and RGB lighting, powered by CircuitPython and KMK.

## ⚡ Features
- **Microcontroller:** Seeed XIAO RP2040
- **Firmware:** KMK (CircuitPython)
- **Controls:** 4 Keys + 1 Rotary Encoder (with click)
- **Lighting:** 2x SK6812 MINI RGB LEDs

## 🎮 Keymap / Controls

| Key | Action | Function |
| :--- | :--- | :--- |
| **SW1** | `Ctrl` + `C` | **Copy** |
| **SW2** | `Ctrl` + `V` | **Paste** |
| **SW3** | Macro | Types **"sybau"** |
| **SW4** | Macro | Types **"fr"** |
| **Knob Rotate** | CW / CCW | **Volume Up / Down** |
| **Knob Click** | Press | **Mute Audio** |

## 📸 Project Gallery

| ![Macropad](1.Macropad.png) | ![Top View](2.Top.png) | ![Base](3.Base.png) |
| :---: | :---: | :---: |
| **Macropad** | **Top View** | **Base** |

| ![Schematic](4.Schematic.png) | ![PCB](5.PCB.png) | ![Board](6.Board.png) |
| :---: | :---: | :---: |
| **Schematic** | **PCB Layout** | **Assembled Board** |

## 🛠️ Wiring / Pinout

| Component | Physical Pin | CircuitPython Pin |
| :--- | :--- | :--- |
| **SW1** | Pin 8 | `board.RX` |
| **SW2** | Pin 9 | `board.SCK` |
| **SW3** | Pin 10 | `board.MISO` |
| **SW4** | Pin 11 | `board.MOSI` |
| **Encoder S1** | Pin 1 | `board.A0` |
| **Encoder A** | Pin 7 | `board.TX` |
| **Encoder B** | Pin 6 | `board.SCL` |
| **LED Data** | Pin 5 | `board.SDA` |

## 🚀 Installation Guide

1. **Install CircuitPython:**
   - Hold the `BOOT` button on the XIAO and plug it in.
   - Drag the CircuitPython `.uf2` file onto the `RPI-RP2` drive.

2. **Install Libraries:**
   - Copy the `kmk`, `adafruit_bus_device`, and `neopixel` folders into the `lib` folder on the `CIRCUITPY` drive.

3. **Upload Code:**
   - Copy `main.py` to the root of the `CIRCUITPY` drive.

## 📋 Bill of Materials (BOM)

| **Item**               | **Quantity** | **Description**                          | **Source** |
|------------------------|--------------|------------------------------------------|------------|
| Seeed XIAO RP2040      | 1            | Microcontroller                          | Seeed Studio |
| Push Buttons (6mm)     | 4            | Tactile push buttons                     | Any Electronics Store |
| Rotary Encoder         | 1            | Rotary encoder with push button          | Any Electronics Store |
| SK6812 MINI RGB LEDs   | 2            | Individually addressable RGB LEDs        | Adafruit / Online |
| Resistors (10kΩ)       | 5            | Pull-up resistors for switches and encoder | Any Electronics Store |
| Capacitors (0.1µF)     | 2            | Decoupling capacitors for LEDs           | Any Electronics Store |
| PCB                    | 1            | Custom PCB for the macropad              | Fabricated |
| Micro USB Cable        | 1            | For power and data transfer              | Any Electronics Store |
| Soldering Materials    | -            | Solder, flux, and soldering iron         | Any Electronics Store |

---