import numpy as np
import cv2

# Lee la imagen en escala de grises
img = cv2.imread("el primo.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("jupyter 0065", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# linea
print(" la linea 0065")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("line 0065", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 # circulos 
print(" circulos 0065")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260, 260), 10, (255, 0, 0), -1)

cv2.imshow("circulo 0065", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Texto
print(" textos 0065")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Nahum Flores Nc 0065", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

cv2.imshow("texto 0065", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Trackbars
print("Trackbars 0065")
import cv2
import numpy as np

def on_trackbar(val):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('frame')

cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'frame', 0, 255, on_trackbar)

while True:
    cv2.imshow('frame', img)
    
    k = cv2.waitKey(1) & 0xFF

    # 1. Detectar si la ventana fue cerrada con la "X" (retorna menor a 1 si no es visible)
    # o si se presionó la tecla ESC (27)
    if k == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

    # 2. Solo leer los trackbars si la ventana sigue existiendo
    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    img[:] = [b, g, r]

cv2.destroyAllWindows()

# Thresholding
print(" Thresholding 0065")
import cv2
import numpy as np

img = cv2.imread('el primo.jpg',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Nahum Flores Nc 0065")



