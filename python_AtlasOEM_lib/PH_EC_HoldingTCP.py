# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
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
from pymodbus.server.sync import StartTcpServer, ModbusTcpServer
from AtlasOEM_PH import AtlasOEM_PH
import time
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
import threading
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
import os
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
channel1 = 4
channel2 = 17
channel3 = 27
channel4 = 22

GPIO.setup(channel1, GPIO.OUT)
GPIO.output(channel1, GPIO.LOW)

GPIO.setup(channel2, GPIO.OUT)
GPIO.output(channel2, GPIO.LOW)

GPIO.setup(channel3, GPIO.OUT)
GPIO.output(channel3, GPIO.LOW)

GPIO.setup(channel4, GPIO.OUT)
GPIO.output(channel4, GPIO.LOW)

def run_server():
    # ----------------------------------------------------------------------- #
    # initialize your data store
    # ----------------------------------------------------------------------- #
    #   di=block, co=block, hr=block, ir=block
    #   block = ModbusSequentialDataBlock(0x00, [123]*0x20)
    #   store = ModbusSlaveContext(hr=block)
        block1 = ModbusSequentialDataBlock(0x00, [100] * 0x0F)
        #block2 = ModbusSequentialDataBlock(0x02, [323] * 0x1F)
        block2 = ModbusSequentialDataBlock(0x00, [1] * 0x04),
        store2 = ModbusSlaveContext(hr=block1, di=block2)
            
        slaves = {
        0x01: store2,
        }

        context = ModbusServerContext(slaves=slaves, single=False)

    #   print(block1.values)
    #   print(block2.values)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- #
        identity = ModbusDeviceIdentification()
        identity.VendorName = 'Pymodbus'
        identity.ProductCode = 'PM'
        identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
        identity.ProductName = 'Pymodbus Server'
        identity.ModelName = 'Pymodbus Server'


    # ----------------------------------------------------------------------- #
    # run the server you want
    # ----------------------------------------------------------------------- #
    # Tcp:
    # server = StartTcpServer(context, identity=identity, address=('0.0.0.0', 255))

    # start server in a separate thread so that is not blocking
    # server.start_server()

    # to access the blocks for slave 1
    # store_1=server.context[1]

    # to read from the block
    # print("------")
    # print(store_1.getValues(4,0,32))

    # to write to the block
    # store_1.setValues(0x0F, 0, [111, 121, 122, 123, 124])
    # Type-2 Implementationt
        interval = 2
    # loop = LoopingCall(f=updatevalues, a=(context,))
    # loop.start(time, now=True)
        server = ModbusTcpServer(context, identity=identity,
                            address=('0.0.0.0', 5056))
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
            
    #q = threading.Thread(target=updatevalues, daemon=True)
    #q.start()
    #z = threading.Thread(target=run_server, daemon=True)
    #z.start()

        loop = LoopingCall(f=updatevalues, a=server)
        loop.start(interval, now=True)
        reactor.run()
        

        
def updatevalues(a):
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
    
    def get_OEM_reading(OEM_circuit, readfunction):    # creates a closure to take readings for each circuit         
        reading = [1]                                  # we use a list to approximate a static variable to cache previous readings
        def OEM_reading_closure():                     # make a custom function to do the readings
            if OEM_circuit.read_new_reading_available():   # if we have a new reading
                reading[0] = readfunction()            # get it from the circuit
                #print("OEM " + OEM_circuit.get_name() + \
                #      " reading: " + str(reading))  # print the reading
                OEM_circuit.write_new_reading_available(0)  # then clear the new reading register 
                                                    # so the circuit can set the register
                                                    # high again when it acquires a new reading
            return reading[0]                       # return the value in the list
        return OEM_reading_closure                  # return the custom function without calling it, so we can call it when we want readings
    
    def get_all_EC_values():                        # we can gt all 3 EC values by returning them in a list
        EC_val = EC.read_EC_reading()
        #TDS_val = EC.read_TDS_reading()
        #sal_val = EC.read_salinitiy_reading()
        return EC_val #,TDS_val, sal_val]
    
    read_pH = get_OEM_reading(PH, PH.read_PH_reading) #assign the closures so we can call them to get readings
    read_EC = get_OEM_reading(EC, get_all_EC_values)
    #read_pH = float("{0:.1f}".format(read_pHraw))
    #read_EC = float("{0:.1f}".format(ead_ECraw))
    #read_DO = get_OEM_reading(DO, DO.read_DO_reading)
    
    time.sleep(10)
    # give circuits time to get the initial readings
    
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
        time.sleep(10)
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
        time.sleep(.5)
        ecint=ec_val
        format_float1 = "{:.0f}".format(ecint)
        ECACT = format_float1
        #ECNEW = int(float(ECACT))
        #ec1 = "{:.0f}".format(ECNEW)
        ec2 = int(ECACT)
        #print(ecint)
        print(ec2)
        #ec1 =format_float
        #ec2 = int(ec1)
        #print(ec2)
        
        
        Temp = temp
        Tempgate = Temp*10
        temp1 = "{:.0f}".format(Tempgate)
        temp2 = int(temp1)
        print(temp2)
        
###################################################################################################################       
        pH_reading = ph_val
        ph = pH_reading*100
        format_float = "{:.0f}".format(ph)
        pH1 =format_float
        pH2 = int(pH1)
        #print(pH2)
        
        print("------------START----------")
        cfuncode = 1
        rfuncode = 3
        wfuncode = 16
        slave_id = 0x01
        address = 0x00
        #address1 = 0x01
        contxt = a.context[slave_id]
        values = contxt.getValues(3, address, count=10)
        values1 = contxt.getValues(1, address, count=10)
        print(values)
        DI1 = GPIO.input(channel1)
        DI2 = GPIO.input(channel2)
        DI3 = GPIO.input(channel3)
        DI4 = GPIO.input(channel4)
        
        
        contxt.setValues(1, 0x00, DI1)
        contxt.setValues(1, 0x01, DI2)
        contxt.setValues(1, 0x02, DI3)
        contxt.setValues(1, 0x03, DI4)
        contxt.setValues(3, 0x00, pH2)
        contxt.setValues(3, 0x01, ec2)
        contxt.setValues(3, 0x02, temp2)
        #contxt.setValues(3, 0x02, ecint)
        print("-------------END-------------")

if __name__ == "__main__":
    while True:
        run_server()
        updatevalues()
        time.sleep(.5)
    
        
