🛠 Components Used:
Raspberry Pi Pico W
MPU6050 (Gyroscope & Accelerometer)
LCD1602 (I2C-based)
Servo Motor (PWM-controlled)
Potentiometers (x2)
LEDs (x4)
Resistors (220Ω for LEDs)
Jumper wires
Breadboard
🔌 Wiring Guide
1️⃣ Power Connections
Raspberry Pi Pico W VCC (3.3V) → MPU6050 VCC
Raspberry Pi Pico W GND → MPU6050 GND
Raspberry Pi Pico W VCC (3.3V) → Servo Motor VCC
Raspberry Pi Pico W GND → Servo Motor GND
Raspberry Pi Pico W 3.3V → Potentiometers VCC
Raspberry Pi Pico W GND → Potentiometers GND
Raspberry Pi Pico W 3.3V → LEDs (through resistors)
2️⃣ I2C (MPU6050 & LCD)
Pico W GP0 (SDA) → MPU6050 SDA
Pico W GP1 (SCL) → MPU6050 SCL
Pico W GP0 (SDA) → LCD SDA (Shared with MPU6050)
Pico W GP1 (SCL) → LCD SCL (Shared with MPU6050)
3️⃣ Servo Motor
Pico W GP16 (PWM) → Servo Signal Pin
Pico W 3.3V → Servo Power (if needed, use external 5V)
Pico W GND → Servo GND
4️⃣ LEDs
LED	Pico Pin
Blue LED	GP3
Green LED	GP9
Red LED	GP15
White LED	GP14
Each LED needs a 220Ω resistor in series to avoid burning out.
5️⃣ Potentiometers
Potentiometer	Pico Pin
LED Potentiometer	GP28 (ADC2)
Servo Control Potentiometer	GP27 (ADC1)
Center pin of each potentiometer goes to respective ADC pin.
One side to 3.3V, other to GND.
