def helloCallBack1():
    os.system('python PlotPH.py')
   
    
def helloCallBack2():
    os.system('python PlotEC.py')
    
def helloCallBack3():
    os.system('python PH_EC_HoldingTCP.py')
    
def create_window():
    window = tk.Toplevel(root)
    

def Cal_4_Mode(var3):
    print("Entering CAL 4.0 Mode")
    var3.set("Please DIP the PH Probe in PH 4.0 Buffer Solution ")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

            # high again when it acquires a new reading
            
    PH.read_calibration_data()
   
    PH.write_calibration_request(0)
    PH.write_calibration_data(4.00)
    #PH.write_calibration_request(0)
            #PH.write_calibration_request(3)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    time.sleep(20)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    var3.set("Successfully Calibated LOW POINT PH 4.0")
    
def Cal_7_Mode(var4):
    print("Entering CAL 7.0 Mode")
    var4.set("Please DIP the PH Probe in PH 7.0 Buffer Solution")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

    
    PH.read_calibration_data()
    
    PH.write_calibration_request(1)
    PH.write_calibration_data(7.00)
    #PH.write_calibration_request(1)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    time.sleep(20)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
    #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    var3.set("Successfully Calibated MID POINT PH 7.0")
    
def Cal_10_Mode(var5):
    print("Entering CAL 10.0 Mode")
    #var5.set("Please DIP the PH Probe in PH 10.0 Buffer Solution")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking reading
            
    PH.read_calibration_data()
   
    PH.write_calibration_request(2)
    PH.write_calibration_data(10.00)
    #PH.write_calibration_request(2)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    time.sleep(20)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    var5.set("Successfully Calibated MID POINT PH 10.0")
def Cal_EC_Mode(var6):
    EC = AtlasOEM_EC(name = "EC") # create an OEM EC object
    EC.write_active_hibernate(1)

    

    if EC.read_new_reading_available():   # if we have a new reading
                EC.write_new_reading_available(0)  # then clear the new reading register    # then clear the new reading register 
                EC.read_calibration_data()
                EC_CalData = EC.read_calibration_data()
                print("OEM EC CAL reading: " + str(EC_CalData))
                EC.write_calibration_data(1413)
                EC.write_calibration_request(3)
                #PH.write_calibration_request(2)
                #PH.write_calibration_request(0)
                #PH.read_calibration_confirm()
                #time.sleep(1)
                time.sleep(20)
                #PH.write_calibration_request(2)
                EC_ReadCal = EC.read_calibration_confirm()
                
                print("OEM pH CALCONF reading: " + str(EC_ReadCal))
                var6.set("Successfully Calibated EC 1413")
def Cal_DeletePH_Mode(var7):
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

            # high again when it acquires a new reading
            
    PH.read_calibration_data()
    
    PH.write_calibration_request(0)
    PH.write_calibration_data(0)
            #PH.write_calibration_request(3)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    time.sleep(5)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    


def PH_plus():
    global number
    maxN = 14
    number += 0.5
    number = min(maxN, number)
    label.config(text=number)
    print(number)

def PH_minus():
    global number
    minN = 0
    number -= 0.5
    number = max(minN, number)
    label.config(text=number)
    print(number)
    
def PH_plus1():
    global number1
    maxN = 14
    number1 += 0.5
    number1 = min(maxN, number1)
    label6.config(text=number1)
    print(number1)

def PH_minus1():
    global number1
    minN = 0
    number1 -= 0.5
    number1 = max(minN, number1)
    label6.config(text=number1)
    print(number1)
    
def EC_plus():
    global number2
    maxN = 10000
    number2 += 100
    number2 = min(maxN, number2)
    label7.config(text=number2)
    print(number2)

def EC_minus():
    global number2
    minN = 0
    number2 -= 100
    number2 = max(minN, number2)
    label7.config(text=number2)
    print(number2)
    
def EC_plus1():
    global number3
    maxN = 10000
    number3 += 100
    number3 = min(maxN, number3)
    label8.config(text=number3)
    print(number3)

def EC_minus1():
    global number3
    minN = 0
    number3 -= 100
    number3 = max(minN, number3)
    label8.config(text=number3)
    print(number3)

def start_Cal4_Mode(var3):
    t = threading.Thread(target=Cal_4_Mode, args=(var3,))
    t.start()
    
def start_Cal7_Mode(var4):
    t = threading.Thread(target=Cal_7_Mode, args=(var4,))
    t.start()
    
def start_Cal10_Mode(var5):
    t = threading.Thread(target=Cal_10_Mode, args=(var5,))
    t.start()
    
def start_CalEC_Mode(var6):
    t = threading.Thread(target=Cal_EC_Mode, args=(var6,))
    t.start()
def start_CalDeletePH_Mode(var7):
    t = threading.Thread(target=Cal_DeletePH_Mode, args=(var7,))
    t.start()
    

label = tk.Label(root, text=number, width=5, height=2, font=('Consolas', 15, 'bold'))
label.grid(row=3,column=11)
label3 = tk.Label(root, text="PH HIGH", width=10, height=2, font=('Consolas', 12, 'bold'))
label3.grid(row=2,column=11)
label4 = tk.Label(root, text="Thresholds", width=10, height=2, font=('Consolas', 15, 'bold'))
label4.grid(row=1,column=12)
label5 = tk.Label(root, text="PH LOW", width=10, height=2, font=('Consolas', 12, 'bold'))
label5.grid(row=5,column=11)
label6 = tk.Label(root, text=number1, width=5, height=2, font=('Consolas', 15, 'bold'))
label6.grid(row=6,column=11)
label7 = tk.Label(root, text=number2, width=5, height=2, font=('Consolas', 15, 'bold'))
label7.grid(row=3,column=12)
label8 = tk.Label(root, text=number3, width=5, height=2, font=('Consolas', 15, 'bold'))
label8.grid(row=6,column=12)
label5 = tk.Label(root, text="EC HIGH", width=10, height=2, font=('Consolas', 12, 'bold'))
label5.grid(row=2,column=12)
label5 = tk.Label(root, text="EC LOW", width=10, height=2, font=('Consolas', 12, 'bold'))
label5.grid(row=5,column=12)
#label = tk.Label(root, text="PH_HIGH Input")
#label.grid(row=4,column=10)
b = tk.Button(root, text="Cal 4.0", width=8, height=1, bg="black", fg = "white", font=("Arial",14), command=lambda: start_Cal4_Mode(var3))
b.grid(row=2,column=0)
c = tk.Button(root, text="Cal 7.0", width=8, height=1, bg="black", fg = "white", font=("Arial",14), command=lambda: start_Cal7_Mode(var4))
c.grid(row=1,column=0)
d = tk.Button(root, text="Cal 10.0", width=8, height=1, bg="black", fg = "white", font=("Arial",14), command=lambda: start_Cal10_Mode(var5))
d.grid(row=3,column=0)
e = tk.Button(root, text="Cal  EC", width=8, height=1, bg="black", fg = "white", font=("Arial",14), command=lambda: start_CalEC_Mode(var6))
e.grid(row=4,column=0)
b1=tk.Button(root, text="Trend PH",bg="black", fg = "white", font=("Arial",14),command=helloCallBack1)
b1.grid(row=5, column=0)
b2=tk.Button(root, text="Trend EC",bg="black", fg = "white", font=("Arial",14),command=helloCallBack2)
b2.grid(row=6, column=0)

PH_plus = tk.Button(root, text="PH +", command=PH_plus, font=("Helvetica", 12))
PH_plus.grid(row=4,column=10)
PH_minus = tk.Button(root, text="PH -", command=PH_minus, font=("Helvetica", 12))
PH_minus.grid(row=4,column=11)

PH_plus1 = tk.Button(root, text="PH +", command=PH_plus1, font=("Helvetica", 12))
PH_plus1.grid(row=7,column=10)
PH_minus1 = tk.Button(root, text="PH -", command=PH_minus1, font=("Helvetica", 12))
PH_minus1.grid(row=7,column=11)

EC_plus = tk.Button(root, text="EC +", command=EC_plus, font=("Helvetica", 12))
EC_plus.grid(row=4,column=12)
EC_minus = tk.Button(root, text="EC -", command=EC_minus, font=("Helvetica", 12))
EC_minus.grid(row=4,column=13)

EC_plus1 = tk.Button(root, text="EC +", command=EC_plus1, font=("Helvetica", 12))
EC_plus1.grid(row=7,column=12)
EC_minus1 = tk.Button(root, text="EC -", command=EC_minus1, font=("Helvetica", 12))
EC_minus1.grid(row=7,column=13)



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