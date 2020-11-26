import socket
import numpy as np
import cv2
import base64

UDP_IP = "127.0.0.1"
UDP_PORT = 3399

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind ((UDP_IP, UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(65507)
        img = base64.b64decode(data)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break