import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("カメラを開けませんでした")
else:
    ret, frame = cap.read()
    if ret:
        print("フレーム取得成功")
    else:
        print("フレーム取得失敗")
cap.release()
