#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer


#Constants
nbPCAServo=8 
host_name = '192.168.254.34'  # Change this to your Raspberry Pi IP address
host_port = 8000

#Parameters
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=8)




# function main 
def main():
        while True:
                menu(0,0,0)

def menu(selection, part, angle):
        availableChoices = ["stop", "come", "point", "peace", "control", "up/down", "left/right", "binary count", "server control"]
        print("Menu choices")
        for number, choice in enumerate(availableChoices):
                print("{0}: {1}".format(number, choice))
        selection = int(input())
        if selection == 0:
                stop()
        elif selection == 1:
                come()
        elif selection == 2:
                pointing()
        elif selection == 3:
                peace()
        elif selection == 4:
                part = input("Enter part index: 0-6\n")
                angle = input("Enter angle: 0-180\n")
                control(part,angle)
        elif selection == 5:
                upDown()
        elif selection == 6:
                leftRight()
        elif selection == 7:
                binaryCount()
        elif selection == 8:
                http_server = HTTPServer((host_name, host_port), MyServer)
                print("Server Starts - %s:%s" % (host_name, host_port))

                try:
                    http_server.serve_forever()
                except KeyboardInterrupt:
                    http_server.server_close()
        print()

#function to control individual parts of the hand and wrist
#part is part of hand or wrist
# 0 wrist left/right
# 1 thumb
# 2 index
# 3 middle
# 4 ring
# 5 pinky
# 6 wrist up/down
def control(part, angle):
        pca.servo[int(part)].angle = int(angle)

def upDown():
        for i in range(0,160,1):
                pca.servo[6].angle=i
                time.sleep(0.01)
        for i in range(160,0,-1):
                pca.servo[6].angle=i
                time.sleep(0.01)
        for i in range(0,160,1):
                pca.servo[6].angle=i
                time.sleep(0.01)
        for i in range(160,0,-1):
                pca.servo[6].angle=i
                time.sleep(0.01)
        pca.servo[6].angle=None

def stop():
        pca.servo[0].angle=None
        pca.servo[1].angle=None
        pca.servo[2].angle=None
        pca.servo[3].angle=None
        pca.servo[4].angle=None
        pca.servo[5].angle=None
        pca.servo[6].angle=None
        exit()

# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        #for j in range(MAX_ANG[i],MIN_ANG[i],-1):
        #    print("Send angle {} to Servo {}".format(j,i))
        #    pca.servo[i].angle = j
        #    time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)

def leftRight():
        for j in range(90,0,-1):
                pca.servo[0].angle = j
                time.sleep(0.01)
        for j in range(0,180,1):
                pca.servo[0].angle = j
                time.sleep(0.01)
        for j in range(180,0,-1):
                pca.servo[0].angle=j
                time.sleep(0.01)
        for j in range(0,180,1):
                pca.servo[0].angle=j
                time.sleep(0.01)
        for j in range(180,90,-1):
                pca.servo[0].angle=j
                time.sleep(0.01)
        pca.servo[0].angle=None

def pointing():
    for j in range(180,10,-1):
        pca.servo[1].angle = j
        pca.servo[3].angle = j
        pca.servo[4].angle = j
        pca.servo[5].angle = j
    time.sleep(1)
    
    for j in range(0, 180,1):
        pca.servo[1].angle = j
        pca.servo[3].angle = j
        pca.servo[4].angle = j
        pca.servo[5].angle = j

    pca.servo[1].angle=None
    pca.servo[3].angle=None
    pca.servo[4].angle=None
    pca.servo[5].angle=None
    time.sleep(1)
    
def peace():
    for j in range(180,10,-1):
        pca.servo[1].angle = j
        pca.servo[3].angle = j
        pca.servo[4].angle = j
    time.sleep(1)
    
    for j in range(0, 180,1):
        pca.servo[1].angle = j
        pca.servo[3].angle = j
        pca.servo[4].angle = j

    pca.servo[1].angle=None
    pca.servo[3].angle=None
    pca.servo[4].angle=None
    time.sleep(1)

def come():
    for i in range(3):
        for j in range(180,10,-1):
            pca.servo[1].angle = j
            pca.servo[2].angle = j
            pca.servo[3].angle = j
            pca.servo[4].angle = j
            pca.servo[5].angle = j

        for j in range(0, 180,1):
            pca.servo[1].angle = j
            pca.servo[2].angle = j
            pca.servo[3].angle = j
            pca.servo[4].angle = j
            pca.servo[5].angle = j
        pca.servo[1].angle=None
        pca.servo[2].angle=None
        pca.servo[3].angle=None
        pca.servo[4].angle=None
        pca.servo[5].angle=None

    time.sleep(1)

def binaryCount():
    for j in range(180,20,-1):
        pca.servo[2].angle = j
        pca.servo[3].angle = j
        pca.servo[4].angle = j
        pca.servo[5].angle = j
    time.sleep(1) #1
    
    for j in range(180,20,-1):
        pca.servo[1].angle = j
    for j in range(0,180,1):
        pca.servo[2].angle = j
    time.sleep(1) #2
    
    for j in range(0,180,1):
        pca.servo[1].angle = j
    time.sleep(1) #3
    
    for j in range(180,20,-1):
        pca.servo[1].angle = j
        pca.servo[2].angle = j
    for j in range(0,180,1):
        pca.servo[3].angle = j
    time.sleep(1) #4
    
    for j in range(0,180,1):
        pca.servo[1].angle = j
    time.sleep(1) #5
    
    for j in range(180,20,-1):
        pca.servo[1].angle = j
    for j in range(0,180,1):
        pca.servo[2].angle = j
    time.sleep(1) #6
    
    for j in range(0,180,1):
        pca.servo[1].angle = j
    time.sleep(1) #7

    for j in range(0,180,1):
        pca.servo[4].angle = j
    for j in range(180,20,-1):
        pca.servo[1].angle = j
        pca.servo[2].angle = j
        pca.servo[3].angle = j
    time.sleep(1) #8
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #9
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #10
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #11
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
        pca.servo[2].angle=j
    for j in range(0,180,1):
        pca.servo[3].angle=j
    time.sleep(1) #12

    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #13
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #14
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #15
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
        pca.servo[2].angle=j
        pca.servo[3].angle=j
        pca.servo[4].angle=j
    for j in range(0,180,1):
        pca.servo[5].angle=j
    time.sleep(1) #16
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #17

    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #18
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #19
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
        pca.servo[2].angle=j
    for j in range(0,180,1):
        pca.servo[3].angle=j
    time.sleep(1) #20
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #21
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #22

    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #23
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
        pca.servo[2].angle=j
        pca.servo[3].angle=j
    for j in range(0,180,1):
        pca.servo[4].angle=j
    time.sleep(1) #24
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #25
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #26

    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #27
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
        pca.servo[2].angle=j
    for j in range(0,180,1):
        pca.servo[3].angle=j
    time.sleep(1) #28
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #29
    
    for j in range(180,20,-1):
        pca.servo[1].angle=j
    for j in range(0,180,1):
        pca.servo[2].angle=j
    time.sleep(1) #30
    
    for j in range(0,180,1):
        pca.servo[1].angle=j
    time.sleep(1) #31s

    pca.servo[1].angle=None
    pca.servo[2].angle=None
    pca.servo[3].angle=None
    pca.servo[4].angle=None
    pca.servo[5].angle=None
    time.sleep(1)

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_POST(self):
        """ do_POST() can be tested using curl command
            'curl -d "submit=On" http://server-ip-address:port'
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        part, angle = post_data.split('-', 1)
        control(part, angle)
        print(part)
        print(angle)
        self._redirect('/')  # Redirect back to the root url

        
# function init 
def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


if __name__ == '__main__':
    #init()
    main()