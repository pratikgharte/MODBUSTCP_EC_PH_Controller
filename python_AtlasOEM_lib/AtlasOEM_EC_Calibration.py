from AtlasOEM_EC import AtlasOEM_EC
import time

def main(): 
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
            
            
                                
        
if __name__ == '__main__':
    main()

