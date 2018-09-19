#get user input as a string
CANdata = raw_input("Please enter the CAN message to be decoded (in HEX)")

LSB = CANdata[0:4]
MSB = CANdata[4:]

MF = 0.03125
newCANdata = MSB + LSB
convertedValue = int(newCANdata,16)
decodedValue = convertedValue*MF

print "Decoded value is: ", decodedValue
