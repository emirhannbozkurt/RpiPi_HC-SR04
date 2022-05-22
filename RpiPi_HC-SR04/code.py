import RPi.GPIO as GPIO
import thingspeak
import time


distance=0

def measure(channel):
    try:
        GPIO.setmode(GPIO.BCM)
        TRIG = 23
        ECHO = 24
        
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        while True:
            GPIO.output(TRIG, False)
            print("Olculuyor...")
            time.sleep(2)

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)
            
            if distance > 2 and distance < 400:
                print("Mesafe:",distance - 0.5,"cm")
            else:
                print("Menzil asildi")
            response = channel.update({'field1':distance })
            
            read = channel.get({})
            print("Read:", read)
        
            
    except KeyboardInterrupt:
        print("\nThanks")
        




    