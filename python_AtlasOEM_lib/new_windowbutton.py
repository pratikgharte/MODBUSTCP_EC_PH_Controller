#Main_GUI_NewW_Backgroung.py
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
PHT = 0
ECT = 0
PHT1 = 0
ECT = 0
number = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
ec_val = 0
ph_val = 0
#var10 = 0
GPIO.setwarnings(False)
PH_HIGH = 4
PH_LOW = 17
EC_HIGH = 27
EC_LOW = 22
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
'''
root = tk.Tk()
root.geometry('800x480')
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "farmfluence-Logo.png")
background = canvas.create_image(400.0, 240.0,image=background_img)
'''

root = Tk()
#root.geometry("1024x800")
#root.title("PH EC Controller")
#root.geometry('800x480')
class App:

    def __init__(self):
        root.title("PH EC Controller")
        root.geometry("800x450")
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
                global var2
                global var1
                global var20
                ec_val = read_EC()      #take readings from the closures
                ph_val = read_pH()
                temp_val=read_temp()
        
            #do_val = read_DO()
                var2.set(f'PH:{ph_val:}')
                var1.set(f'EC:{ec_val:} uS/cm')
                var20.set(f'Temperature:{temp_val:} C')
                print("EC:" + str(ec_val), "Temperature:" + str(temp)  # print the readings
                     + "\t PH:" + str(ph_val))
                ECT = ec_val
                PHT =  ph_val
            #PH1=int(PHT)
            #ECT1=int(ECT)
            #print(PHT1)
            #print(ECT1)
                time.sleep(.5)
        
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
                    
        var2 = tk.StringVar()
        var1 = tk.StringVar()
        var20 = tk.StringVar()

        self.lbl = tk.Label(root, textvariable=var2, width=20, height=2, font=('Consolas', 15, 'bold'))
        self.lbl.grid(row=1,column=3)
        lbl1 = tk.Label(root, textvariable=var1, width=20, height=2, font=('Consolas', 15, 'bold'))
        lbl1.grid(row=2,column=3)
        lbl2 = tk.Label(root, textvariable=var20, width=20, height=2, font=('Consolas', 15, 'bold'))
        lbl2.grid(row=3,column=3)
        
        self.beginB = Button(root, text="Menu", command=self.begin, bg="green", height=1, width=8)
        self.beginB.grid(row=7, column=0)
        
    def begin(self):
        root.title("main window")
        self.beginB.destroy()
        del self.beginB
        self.goB = Button(root, text='Go on', command=self.go_on,
                                bg='red')
        self.goB.grid(sticky=E)
    def go_on(self):
        self.label = Label(root, text="you have continued")
        self.label.grid(row=1, sticky=S)
      
App()
root.mainloop()
