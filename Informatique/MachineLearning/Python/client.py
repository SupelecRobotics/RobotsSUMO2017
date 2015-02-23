import socket
import cv2
import numpy

TCP_IP = 'localhost'
TCP_PORT = 5001

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

cap = cv2.VideoCapture(0)

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

cv2.namedWindow('Client', cv2.WINDOW_NORMAL)

end = False

while(cap.isOpened() and not end):
    
    ret,frame = cap.read()
    if(ret):
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()
        sock.send( str(len(stringData)).ljust(16))
        sock.send( stringData )

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        end = True

cap.release()
sock.close()
cv2.destroyAllWindows() 
