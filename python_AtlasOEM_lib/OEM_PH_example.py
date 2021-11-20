from AtlasOEM_PH import AtlasOEM_PH
import time
global pH_reading
def main():
        PH = AtlasOEM_PH() # create an OEM PH object

        PH.write_active_hibernate(1) # tell the circuit to start taking readings

    #while True:
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading = PH.read_PH_reading()            # get it from the circuit
            print("OEM pH reading: " + str(pH_reading))  # print the reading
            PH.write_new_reading_available(0)   # then clear the new reading register 
            return pH_reading
if __name__ == '__main__':
    while True:
        main()
        time.sleep(.5)
    