# Imported Modules
import mysql.connector
import MySQLdb
from datetime import datetime
import base64
from picamera import PiCamera
from time import sleep
# Declarations
now = datetime.now() 
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Function that sends data and adds it to the database
def storeImage():
    with open("hi.jpg", "rb") as imageFile:
        str= base64.b64encode(imageFile.read())
        print (str)
    db = MySQLdb.connect(host="192.168.0.16", user="pi", passwd="pi", db="weather pi")
    print('Writing to database..')
    cur = db.cursor()
    cur.execute("INSERT INTO images (image) VALUES (%s)",(str,))
    db.commit()
    db.close()
    print('Successfully inserted image!')
    
def snapshot():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('hi.jpg')
    camera.stop_preview()
    camera.close()
    
def record():
    import picamera
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()

while True:
    print("starting camera..")
    #record()
    snapshot()
    storeImage()
    break;
