import serial
import time
import string
import pynmea2
from datetime import datetime
import MySQLdb

while True:
    now = datetime.now() 
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    #print (newdata)
    line = ser.read(6).decode("utf-8")
    #print(line)
    if line == "$GPGGA":
        line = ser.readline().decode("utf-8") # Read the entire string
        lat=(line[11] +line[12] + "." + line[13] + line[14] +line[16] +line[17] +line[18] +line[19] +line[20] )
        lon=(line[25] +line[26] + "." + line[27] + line[28] +line[30] +line[31] +line[32] +line[33] +line[34] )
        print("Latitude: " + lat + " N")
        print("Longitude: " + lon + " W")
        
        # Save the GPS data to a file
        f=open("gpsbackup.txt", "a")
        f.write(timestamp + " ")
        f.write("Latitude: " + lat + " ")
        f.write("Longitude: " + lon + " ")
        f.close()
        
        # Send GPS data to database
        db = MySQLdb.connect(host="192.168.0.16", user="pi", passwd="pi", db="weather pi")
        print('Writing to database..')
        cur = db.cursor()
        cur.execute("INSERT INTO gps (lat, lon) VALUES (%s, %s)",(lat, lon))
        db.commit()
        db.close()
        print('Successfully inserted data!\n')
