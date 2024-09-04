import cv2
from playsound import playsound
fire_c = cv2.CascadeClassifier('fire_detection.xml')
moon = cv2.VideoCapture(0)
while(True):

    ret,frame = moon.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_c.detectMultiScale(frame,1.2,5)
    for (x,y,w,h) in fire:
        moon_gray = gray[y:y+h, x:x+w]
        moon_color = frame[y:y+h, x:x+w]
        print('Fire is detected')
        playsound('audio.mp3')
    cv2.imshow('moon', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break