"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

from tokenize import String
import cv2
import tkinter as tk 
from datetime import datetime
from gaze_tracking import GazeTracking
import os
from twilio.rest import Client
from config import *

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

wasRight = False
previousTime = datetime.now()
text = "0"
desiredTime = 2
warnings = 0

client = Client(account_sid, auth_token)


def sendMessage():
    message = client.messages.create(
    to="+13147554809", 
    from_="+19285758326",
    body="Focus, you lazy MF!")
    print(message)

sendMessage()

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    if (wasRight and (datetime.now() - previousTime).total_seconds() > 0.2 and gaze.is_left()):
        text = str((datetime.now() - previousTime).total_seconds())
        previousTime = datetime.now()
        wasRight = False
        warnings += 1
        if (warnings >= 3):
            sendMessage()
            warnings = 0

    cv2.putText(frame, "Warnings:  " + str(warnings), (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.9, (255, 255, 255), 2)

    cv2.imshow("Demo", frame)

    if (gaze.is_right()):
        wasRight = True
        
    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
