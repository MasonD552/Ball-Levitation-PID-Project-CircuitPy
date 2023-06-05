import board
import adafruit_hcsr04
from PID_CPY import PID  
import pwmio   
import time 

# Initialize PID controller with appropriate parameters
pid = PID(100, 800, 1000)
pid.setpoint = 35
pid.output_limits = (24000, 34000)

# Initialize PWM output for the fan motor
fanMotor = pwmio.PWMOut(board.D8, duty_cycle=65535, frequency=5000) # fanfanMotor
fanMotor.duty_cycle = 0

# Initialize ultrasonic distance sensor
dist = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)

while True:
    try:
        # Measure the distance and calculate the height
        height = 20 - dist.distance
        
        # Calculate the speed using the PID controller
        speed = int(pid(height))
        
        # Set the fan motor speed
        fanMotor.duty_cycle = speed
        
        # Print the speed and height for debugging purposes
        print("speed")
        print(speed)
        print("height")
        print(height)
        print(" ")
    except RuntimeError:
        # Handle any runtime errors
        print("retry")
    
    # Delay for a short period of time
    time.sleep(0.1)
