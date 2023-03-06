import time
import cv2
import threading
import os



foder = input("Nhập tên Foder")
os.mkdir(foder)
print("Đã tạo Forder tên ",foder)
nameimg = input("Nhập tên ảnh: ")


DriverVideo = 0
cap = cv2.VideoCapture(DriverVideo)
i=0


while (True):
    ret,frame= cap.read()
    cv2.imshow("Camera",frame)
    i=i+1
    cv2.imwrite(r'E:/img/'+ nameimg + str(i) +'.png',frame)
    print("Đã chụp ảnh tên "+nameimg+ " theo thứ tự số ",i)
    print(time.ctime())

    if i>5:
        cap.release()
        cv2.destroyAllWindows()
        break