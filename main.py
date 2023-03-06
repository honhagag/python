import cv2
import face_recognition
import numpy as np
from datetime import datetime

# tạo file ghi dữ liệu
def thamdu(name):
    with open("thamdu.csv","r+") as f:
        myDataList = f.readline()
        for line in myDataList:
            nameList=[]
            entry = line.split(",")
            nameList.append(entry)

        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dtstring}")
Camera=0

# mở cam
vid = cv2.VideoCapture(Camera)



# load ảnh từ file
jihar_image = face_recognition.load_image_file("hoang.jpg")
#mã hóa ảnh
jihar_encoding = face_recognition.face_encodings(jihar_image)[0]

known_face_encodings = [
    jihar_encoding
]

known_face_names =( "Hoàng nè")


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while(True):
    ret, frame = vid.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)

            name = "Unknown"
            #tìm điểm khác khuôn mặt
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            thamdu(name)
            face_names.append(name)
    process_this_frame = not process_this_frame
    # khai báo tọa độ khoanh khuôn mặt
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        #vẽ lên hình khuôn mặt
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()