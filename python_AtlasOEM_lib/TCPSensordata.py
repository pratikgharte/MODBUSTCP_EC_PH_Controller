#!/usr/bin/env python3


import json
import time
from collections import defaultdict
from threading import Thread
from pymodbus.constants import Endian
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
from pymodbus.payload import BinaryPayloadBuilder
import logging
import logging.handlers as Handlers
from AtlasOEM_PH import AtlasOEM_PH
import time
global pH_reading
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


#file = open('config.json', mode='r')
#config = json.loads(file.read())
#file.close()

def data_update(config, a):
        context = a[0]
        PH = AtlasOEM_PH()
        PH.write_active_hibernate(1)
         # tell the circuit to start taking readingswhile True:
        for PH in config['sensor PH']:
                   
                if PH.read_new_reading_available():              # if we have a new reading
                    pH_reading = PH.read_PH_reading()            # get it from the circuit
            #print("OEM pH reading: " + str(pH_reading))  # print the reading
                    PH.write_new_reading_available(0)   # then clear the new reading register 
                else:
            #print("waiting")
                    time.sleep(.5)  
                    #block1 = ModbusSequentialDataBlock(0x00, [pH_reading] * 0x02)
                    #block2 = ModbusSequentialDataBlock(0x10, [323] * 0x1F)
    
                    #store2 = ModbusSlaveContext(hr=block1, ir=block2)

                    #slaves = {
                            #0x01: store2,
                              #}

                    #context = ModbusServerContext(slaves=slaves, single=False)
store = ModbusSlaveContext(
ir=ModbusSequentialDataBlock(0, [17]*100))
                                
context = ModbusServerContext(slaves=store, single=True)

thread = Thread(target=data_update, args=(config, context,))
thread.start()
    
StartTcpServer(context, identity=ModbusDeviceIdentification(), address=("0.0.0.0", config['port']))