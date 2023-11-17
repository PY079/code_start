# pip install opencv-python
# если честно, то я сам не знаю как этим всем пользоваться
# фото нашел с помощью алисы, можно найти любое фото
import cv2

# загрузить изображение по полному пути
image = cv2.imread(r'image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('initial', image) # открыть окно с бинарным изображением
cv2.imshow('bin', binary) # открыть окно с бинарным изображением

cv2.waitKey(0)
cv2.destroyAllWindows()