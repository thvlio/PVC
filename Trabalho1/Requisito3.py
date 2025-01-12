import cv2
import numpy as np
import argparse

class Req3:
    def __init__(self, args):
        cv2.namedWindow("Requisito 3")
        cv2.setMouseCallback('Requisito 3',self.get_mouse_position)
        self.cor = (None, None, None)

        self.vid = cv2.VideoCapture(args["video"])

    def get_mouse_position(self, event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("coluna = {}  linha = {}".format(x,y))

            #pega a cor no formato BGR
            self.cor = (self.imagem[y][x][0], self.imagem[y][x][1], self.imagem[y][x][2])

            if self.isGray:
                print("Intensidade do tom de cinza = {}".format(self.cor[0]))
            else:
                print("R = {}  G = {}  B = {}".format(self.cor[2], self.cor[1], self.cor[0]))


    def checkIfGray(self):
        #pega as caracteristicas da self.imagem e percorre ela
        width, height, depth = self.imagem.shape

        if depth == 1:
            return True
            
        for w in np.arange(0, width):
            for h in np.arange(0, height):
                if not ((self.imagem[w][h][0] == self.imagem[w][h][1]) and (self.imagem[w][h][1] == self.imagem[w][h][2])):
                    return False

        return True

    def paint_pixels(self):
        #pega as caracteristicas da imagem e percorre ela
        width, height, _ = self.imagem.shape

        if self.cor == (None, None, None):
            return

        for w in np.arange(0, width):
            for h in np.arange(0, height):
                color = (self.imagem[w][h][0], self.imagem[w][h][1], self.imagem[w][h][2])
                if self.is_same_color(self.cor, color):
                    self.imagem[w][h] = (0, 0, 255)

    def is_same_color(self, cor, color):
        dB = (int(cor[0]) - int(color[0])) ** 2
        dG = (int(cor[1]) - int(color[1])) ** 2
        dR = (int(cor[2]) - int(color[2])) ** 2

        dist = (dB + dG + dR) ** (0.5)

        if dist < 13:
            return True
        else:
            return False

    def run(self):
        grabbed, self.imagem = self.vid.read()
        self.isGray = self.checkIfGray()

        while True:
            if not grabbed or self.imagem is None:
                break
        
            self.paint_pixels()

            cv2.imshow("Requisito 3", self.imagem)

            if self.cor == (None, None, None):
                k = cv2.waitKey(30) & 0xFF
            else:
                k = cv2.waitKey(1) & 0xFF
            
            if k == ord("q"):
                break

            grabbed, self.imagem = self.vid.read()

if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", default="cargoPickupGantryTest1.avi",
        help="path to input video")
    args = vars(ap.parse_args())
    
    
    t = Req3(args)
    t.run()
