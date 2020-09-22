import time
import busio
import board
import adafruit_adxl34x
from adafruit_adxl34x import Range
import datetime

y=0
i2c = busio.I2C(board.SCL, board.SDA)
acc = adafruit_adxl34x.ADXL345(i2c)
ran = Range
r=ran.RANGE_8_G
print(acc.range)
acc.range = r

preval = (0,0,0)

with open('/home/pi/values_strong_1.xlt','a') as f:

    f.write("time\tacceleration_x\tacceleration_y\tacceleration_z\tbump\n")

    while True:

        accval = list(acc.acceleration)
        accval[0]/=9.78
        accval[1]/=9.78
        accval[2]/=9.78
        accval=tuple(accval)

        if (accval[2]-preval[2] >3):
            b=True
        else:
            b=False
        
        f.write(str(datetime.datetime.now())+"\t%f\t%f\t%f\t"%(accval)+str(b)+'\n')
        print(str(datetime.datetime.now())+"\t%f\t%f\t%f\t"%(accval)+str(b))

        preval = accval
        
        '''time.sleep(0.5)'''

