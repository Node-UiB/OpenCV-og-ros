import cv2 as cv
import numpy as np

#Lager en variabel som er lik en liste med informajson om bildet
image_balls = 'balls.png'
image = cv.imread(image_balls)

#Converterer ti hsv, og splitter kanalene
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
img_h, img_s, img_v = cv.split(image_hsv)

#Makser saturation og value for å isolere fargene
img_s.fill(255)
img_v.fill(255)

#Merger og konverterer tilbake til BGR, siden mesteparten av funksjonene i cv2 bruker bgr format. Litt bs, fordi andre rammeverk bruker rgb, men er mulig bare plagsomt.
hue_img = cv.merge([img_h, img_s, img_v])
hue_img = cv.cvtColor(hue_img, cv.COLOR_HSV2BGR)

#Lager en hue-maske, og prøver å isolere små hull med rektangler. Fungerer for rektangler, men dårlig for alt annet. 
lower_range = np.array([170,100,100])
upper_range = np.array([180,255,255])
mask = cv.inRange(image_hsv, lower_range, upper_range)
kernel = np.ones((23,23), np.uint8)
filtered_mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

#Lager et bilde for å vise det isolerte objektet.
output = cv.bitwise_and(image, image, mask= filtered_mask)

#Finner det største isolerte objektet.
countours, hierarchy = cv.findContours(filtered_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

if len(countours) != 0:
    #Unødvendig 
    #cv.drawContours(output, countours, -1, (0,255,0), 2)

    c = max(countours, key=cv.contourArea)
    x, y, w, h = cv.boundingRect(c)

    # Tegner den største contouren i hvit, og lager et stort grønt rektangel på det største objektet.
    cv.drawContours(output, c, -1, (255,255,255), 2)
    cv.rectangle(image, (x, y), (x+w,y+h),(0,255,0),2)

#Grei informasjon om bildet, dimensjoner og kanaler
print(image.shape)

#Viser de to bildene. 
cv.imshow('image', np.hstack([image, output]))

#Trykk på en knapp, og så utføres linjene under
cv.waitKey(0)

cv.imwrite('done_result.jpg', image)

cv.destroyAllWindows()