import cv2
import numpy as np

# img_file = '8117.jpg'
# img= cv2.imread(img_file)
# save_file = '8117-1.jpg'
# img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
# # dst2 = cv2.resize(img, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
# if img is not None:
#     cv2.imshow('IMG', img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
# else:
#     print('No image file.')




#img_canny = cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
# 첫번째 아규먼트 : 입력 이미지
# 두번째, 세번째 아규먼트 : 최소 threshold, 최대 threshold
# 네 번째 아규먼트 : edges에 Canny 결과를 저장할 변수를 적어준다.
# 파이썬에선 Canny 함수 리턴으로 받을 수 있기 때문에 필요없는 항목이다.
# 다섯번째 아규먼트는 이미지 그레디언트를 구할때 사용하는 소벨 커널 크기이다. 디폴트 :3
# 여섯 아규먼트 : True이면 그레디언트 크기를 계산할때 sqrt{(dI/dx)^2 + (dI/dy)^2}를 사용합니다.
# False라면 근사값인 |dI/dx|+|dI/dy|를 사용합니다. 디폴트값은 False입니다.

img_gray = cv2.imread('8117.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.resize(img_gray, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow('Original', img_gray)

img_canny = cv2.Canny(img_gray, 50, 150)
cv2.imshow('Canny Edge', img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()