from AtlasOEM_PH import AtlasOEM_PH
import time
global pH_reading
def main():
        PH = AtlasOEM_PH() # create an OEM PH object

        PH.write_active_hibernate(1) # tell the circuit to start taking readings

    #while True:
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading = PH.read_PH_reading()            # get it from the circuit
            #print("OEM pH reading: " + str(pH_reading))  # print the reading
            PH.write_new_reading_available(0)   # then clear the new reading register
            ph = pH_reading*100
            format_float = "{:.0f}".format(ph)
            pH1 =format_float
            pH2 = int(pH1)
            print(pH2)
            time.sleep(.5)
            return pH1
        
if __name__ == '__main__' and '__file__':
    while True:
        main()
        
    
