
# Imported Modules
import time
import Adafruit_DHT
from datetime import datetime
import MySQLdb
import socket

# Declarations
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
now = datetime.now() 
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Function that sends data and adds it to the database
def send_data():
    sensor = 1
    db = MySQLdb.connect(host="192.168.0.22", user="pi", passwd="pi", db="weather pi")
    print('Writing to database..')
    cur = db.cursor()
    cur.execute("INSERT INTO dht22 (temperature, humidity, sensor) VALUES (%s, %s, %s)",(temperature, humidity, sensor))
    db.commit()
    db.close()
    print('Successfully inserted data!')

# Function that saves data to a txt file on the pi
def saveToFile():
    formattedTemp = "{:.2f}".format(temperature)
    formattedHu = "{:.2f}".format(humidity)
    f=open("databackup.txt", "a")
    f.write(timestamp + " ")
    f.write("Temperature: " + str(formattedTemp) + " ")
    f.write("Humidity: " + str(formattedHu) + " ")
    f.write("Sensor: " + str(sensor) + "\n")
    f.close()
    #f=open("databackup.txt", "r")
    #print(f.read())
    
def getHost():
    global local_hostname
    local_hostname=socket.gethostname()
    print("Hostname: " + local_hostname)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = temperature * 1.8 + 32
    sensor=1

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    
    send_data()
    saveToFile()
    getHost()
    time.sleep(600)
    #break;