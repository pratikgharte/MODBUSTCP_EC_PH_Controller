import RPi.GPIO as GPIO
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
import time
import threading
from AtlasOEM_PH import AtlasOEM_PH
from AtlasOEM_EC import AtlasOEM_EC
import time
from tkinter import messagebox
global fullscreen
from PIL import ImageTk,Image
from tkinter import *
global ph_HIGH
global ph_LOW
import time
import board
import digitalio
import adafruit_max31865
import os
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import Tk, Canvas, Frame, BOTH
PHT = 7
ECT = 600
number = 4
number1 = 6
number2 = 900
number3 = 1100
number4 = 0
ec_val = 0
ph_val = 0
#var10 = 0
GPIO.setwarnings(False)
PH_LOW = 4
PH_HIGH = 17
EC_LOW = 27
EC_HIGH = 22
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

   
    
'''
def read_sensor():
    global var2
    global var1
    global var20
    global PH
    global EC
    global ec_val
    global ph_val
    PH = AtlasOEM_PH(name = "PH") # create an OEM PH object
    EC = AtlasOEM_EC(name = "EC") # create an OEM EC object
    #DO = AtlasOEM_DO(name = "DO") # create an OEM DO object
    
    PH.write_active_hibernate(1) # tell the circuits to start taking readings
    EC.write_active_hibernate(1)
    #DO.write_active_hibernate(1)
    
    spi = board.SPI()
    cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
    sensor = adafruit_max31865.MAX31865(spi, cs)
    global temp
        # Read temperature.
    tempraw = sensor.temperature
    temp = float("{0:.2f}".format(tempraw))
    #temp1 = temp * 100
    #temp2 = str.format()

    #formatted_float = "{:g}".format(temp1)
    #print(formatted_float)
    #print(temp)
        #print("Temperature: {0:0.1f}C".format(temp))
        # Delay for a second.
    def get_OEM_reading(OEM_circuit, readfunction):    # creates a closure to take readings for each circuit         
        reading = [1]                                  # we use a list to approximate a static variable to cache previous readings
        def OEM_reading_closure():                     # make a custom function to do the readings
            if OEM_circuit.read_new_reading_available():   # if we have a new reading
                reading[0] = readfunction()            # get it from the circuit
                #print("OEM " + OEM_circuit.get_name() + \
                #      " reading: " + str(reading))  # print the reading
                OEM_circuit.write_new_reading_available(0)  # then clear the new reading register 
                OEM_circuit.read_temperature_compensation()                                  # so the circuit can set the register
                OEM_circuit.write_temperature_compensation(temp)
                OEM_circuit.read_temperature_confirmation()
                ec_tempdata = OEM_circuit.read_temperature_confirmation()
                #print("OEM EC Temp data CALCONF reading: " + str(ec_tempdata))
                
            return reading[0]                       # return the value in the list
        return OEM_reading_closure                  # return the custom function without calling it, so we can call it when we want readings
    
    def get_all_EC_values():                        # we can gt all 3 EC values by returning them in a list
        EC_val = EC.read_EC_reading()
        #TDS_val = EC.read_TDS_reading()
        #sal_val = EC.read_salinitiy_reading()
        return EC_val #,TDS_val, sal_val]
    
    read_pH = get_OEM_reading(PH, PH.read_PH_reading) #assign the closures so we can call them to get readings
    read_EC = get_OEM_reading(EC, get_all_EC_values)
    #read_DO = get_OEM_reading(DO, DO.read_DO_reading)
    
    time.sleep(.5)
    
    def read_temp():
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
        sensor = adafruit_max31865.MAX31865(spi, cs)
        global temp
        # Read temperature.
        tempraw = sensor.temperature
        temp = float("{0:.1f}".format(tempraw))
        # Print the value.
        #print("Temperature: {0:0.1f}C".format(temp))
        # Delay for a second.
        time.sleep(.5)
        return temp
    
        
    while True:
        
        ec_val = read_EC()      #take readings from the closures
        ph_val = read_pH()
        temp_val=read_temp()
        
        #do_val = read_DO()
        #var2.set(f'PH:{ph_val:}')
        #var1.set(f'EC:{ec_val:}')
        #var20.set(f'Temperature:{temp_val:}')
        print("EC:" + str(ec_val), "Temperature:" + str(temp)  # print the readings
              + "\t PH:" + str(ph_val))
        ECT = ec_val
        PHT =  ph_val
        #print(str(PHT))
        #print(str(ECT))
        time.sleep(.5)
 '''
def Relay_TH():
    
        if (PHT < number):
            GPIO.output(PH_LOW, GPIO.HIGH)
            GPIO.output(PH_HIGH, GPIO.LOW)
            
            if (PHT > number1):
                GPIO.output(PH_HIGH, GPIO.HIGH)
                GPIO.output(PH_LOW, GPIO.LOW)
            
            elif (ECT < number2):
                GPIO.output(EC_LOW, GPIO.HIGH)
                GPIO.output(EC_HIGH, GPIO.HIGH)
            
            elif (ECT > number3):
                GPIO.output(EC_HIGH, GPIO.LOW)
                GPIO.output(EC_LOW, GPIO.LOW)
        
            else:
                GPIO.output(EC_LOW, GPIO.LOW)
                GPIO.output(EC_HIGH, GPIO.LOW)
                GPIO.output(PH_HIGH, GPIO.LOW)
                GPIO.output(PH_LOW, GPIO.LOW)
        #PH = ph_val
        #EC = ec_val
if __name__ == '__main__':
   while True:
        #read_sensor()
        Relay_TH()
        time.sleep(1)       