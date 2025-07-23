import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import paho.mqtt.client as mqtt
import time
import threading
from notify import notify

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.9)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

def on_message(client, userdata, message):
    print("data from iot ")
    msg = str(message.payload.decode("utf-8"))
    if msg=="0":
        notify("Emergency service....")
   
def sendcmd(client,val):
    client.publish("handgesture1",str(val))
    client.publish("handgesture1",str(val))
    client.publish("handgesture1",str(val))
    client.publish("handgesture1",str(val))


def sendalert(client,msg):
    print('mobile alert')
    msgdata = "{\"title\":\"ID=111 HELP \" , \"body\":\"" + msg + "\"}"
    print(msgdata)
    client.publish("handgesture1",msgdata)

    
print("Connected...")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect("broker.hivemq.com") #connect to broker
client.on_message = on_message
client.loop_start() 


# Initialize the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    
    cv2.imshow('frame', frame)
    
    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                
                landmarks.append([lmx, lmy])
                #print([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
            

            # Predict gesture
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            classID= classID%5
            className = classNames[classID]

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("Output", frame) 

    if className=="A":
        thread = threading.Thread(target=sendcmd,args=(client,"1"))
        thread.start()
    elif className=="D" :
        thread = threading.Thread(target=sendcmd,args=(client,"0"))
        thread.start()
    elif className=="C" :
        thread = threading.Thread(target=sendalert,args=(client,"Please give water"))
        print('mobile alert')
        thread.start()
    elif className=="B" :
        thread = threading.Thread(target=sendalert,args=(client,"nature call"))
        print('mobile alert')
        thread.start()
    elif className=="E" :
        thread = threading.Thread(target=sendalert,args=(client,"Panic"))
        print('mobile alert')
        thread.start()

    if cv2.waitKey(1) == ord('q'):  
        break  
# Code to release resources (e.g., video capture, OpenCV window)
cv2.destroyAllWindows()


# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()