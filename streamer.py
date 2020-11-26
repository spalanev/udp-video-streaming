import base64
import cv2
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 3399

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    try:
        grabbed, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)

        sock.sendto(jpg_as_text, (UDP_IP, UDP_PORT))
        print(jpg_as_text)

    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()
        break
