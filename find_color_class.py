import cv2 as cv
import numpy as np


class Find_color:
    def __init__(self, image_name) -> None:
        #Lager en variabel som er lik en liste med informajson om bildet
        self.image = cv.imread(image_name)
        self.image_hsv = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        self.img_h, self.img_s, self.img_v = cv.split(self.image_hsv)
    
    #Fokuserer bare på hue
    def onlyHue(self):
        self.img_s.fill(255)
        self.img_v.fill(255)
        hue_img = cv.merge([self.img_h, self.img_s, self.img_v])
        self.hue_img = cv.cvtColor(hue_img, cv.COLOR_HSV2BGR)
        
    #Lager en maske
    def createMask(self, lower_hue, upper_hue):
        lower_range = np.array([lower_hue,100,100])
        upper_range = np.array([upper_hue,255,255])
        self.onlyHue()
        mask = cv.inRange(self.image_hsv, lower_range, upper_range)
        kernel = np.ones((23,23), np.uint8)
        filtered_mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
        return mask

    

    #Finner det største isolerte objektet.
    def findCountours(self, lower_hue, upper_hue):
        mask = self.createMask(lower_hue, upper_hue)
        output = cv.bitwise_and(self.image, self.image, mask= mask)
        countours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


        if len(countours) != 0:
            #Unødvendig 
            #cv.drawContours(output, countours, -1, (0,255,0), 2)

            c = max(countours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(c)

            # Tegner den største contouren i hvit, og lager et stort grønt rektangel på det største objektet.
            cv.drawContours(output, c, -1, (255,255,255), 2)
            cv.rectangle(self.image, (x, y), (x+w,y+h),(0,255,0),2)
        self.result = np.hstack([self.image, output])
        return self.result
    
    #Viser countours
    def showCountours(self, lower, upper):
        cv.imshow('image', self.findCountours(lower, upper))
    
    #Lagrer resultat
    def saveResult(self, name):
        cv.imwrite(str(name), self.result)




#Grei informasjon om bildet, dimensjoner og kanaler
bilde = Find_color('balls.png')

#Viser de to bildene. 
bilde.showCountours(80,90)


#Trykk på en knapp, og så utføres linjene under
cv.waitKey(0)

bilde.saveResult('done_result.jpg')

cv.destroyAllWindows()