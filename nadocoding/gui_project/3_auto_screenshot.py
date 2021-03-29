import time
from PIL import ImageGrab  # Python Image Library

time.sleep(5)

for i in range (1,11) : # 2초 간격으로 10 개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 갖져옴
    img.save("이미지{}.png".format(i)) # 파일로 저장
    time.sleep(2)