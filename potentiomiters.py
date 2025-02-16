LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()  #confirms  that the  board is  powered

#importing libs 
from imu import MPU6050
from time import sleep
from machine import Pin, I2C,PWM,ADC
from  lcd1602 import LCD
#initialize the lcd
lcd=LCD()
#initialize servo
servo= PWM(Pin(16))
servo.freq(50)

servo.duty_u16(8191)
sleep(1)
servo.duty_u16(1689)

#initialize the  led pins
blue = Pin(3,Pin.OUT)
green = Pin(9,Pin.OUT)
red = Pin(15,Pin.OUT)
white = Pin(14,Pin.OUT)

#initialize the potentometer
potpin=28 #led potentimeter
servopot=27 # servo potentiometer

mypot=ADC(Pin(potpin))
myservopot=ADC(Pin(servopot))
sleep(1)



#initialize the  gyroscope
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)



lcd.clear()

while True:
    #calibrate the potentiometers
        #led potentiometer
    value=mypot.read_u16()
    myvalue = (100 / 65285) * (int(value) - ((288 * 100) / 65285))
        #servopotentiometer
    servopotvalue=myservopot.read_u16()
    myservopotvalue=(8191/65285)* (int(servopotvalue)-((272*8191)/65285)+1689) # converting  potentometer values  to duty values
    servo.duty_u16(int(myservopotvalue))
    
    # turn on the led buttons   on turning the potentiometer
    if myvalue >=0 and myvalue <25:
        blue.value(1)
        green.value(0)
        red.value(0)
        white.value(0)
        lcd.write(0,0, "blue is  on"+ "   ")
    elif myvalue >25 and myvalue <=50:
        blue.value(0)
        green.value(1)
        red.value(0)
        white.value(0)
        lcd.write(0,0, "green is  on"+ "   ")
    elif myvalue >50 and myvalue <=75:
        blue.value(0)
        green.value(0)
        red.value(1)
        white.value(0)
        lcd.write(0,0, "red is  on"+ "   ")
    elif myvalue >75 and myvalue <=100:
        blue.value(0)
        green.value(0)
        red.value(0)
        white.value(1)
        lcd.write(0,0, "white is  on"+ "   ")
        
    LED.toggle()  #turns  the led on board on and off 
    
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
    #print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem)
    
    sleep(0.5)
