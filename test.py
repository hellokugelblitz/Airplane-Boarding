import time
import sys

#This is just a good example for writing out a timer to the CLI
for remaining in range(1000, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
    sys.stdout.flush()
    time.sleep(0.01)

sys.stdout.write("\rComplete!            \n")