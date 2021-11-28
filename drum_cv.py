import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame
import sys


# Here we get the video stream from our webcam
cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,300)
detector = HandDetector( detectionCon=0.8 )


pygame.mixer.init()
snare_sound = pygame.mixer.Sound('resources/snare.wav')
kick_sound = pygame.mixer.Sound('resources/kick.wav')
hh_sound = pygame.mixer.Sound('resources/hihat.wav')

# Color consts
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Wav consts
SNARE_POS = (150,150)
HH_POS = (80,100)
KICK_POS = (300,250)


pygame.init()

# Set the width and height of the screen [width, height]
size = (650, 412)
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "Remote Drum" )

# Let's declare our image files to be used in the game.
bg = pygame.image.load("resources/drum1.png")
aim = pygame.image.load("resources/aim2.png")
aim = pygame.transform.scale(aim, (25, 25))
pygame.display.flip()

#Basic util to calculate the euclidian distance
def get_distance(pos1,pos2):
    return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5


def aim_handle(hands, detector):
    if hands:
        lmList = hands[0]['lmList']
        if len(hands) == 2 :
            lmList2 = hands[1]['lmList']
            cursor2 = lmList2[8]
            screen.blit(aim, (cursor2[0] - 10, cursor2[1] - 10))
            length2, info2, = detector.findDistance(lmList2[8], lmList2[12], )
            if length2 < 30:
                pygame.draw.circle(screen, BLACK, (cursor2[0], cursor2[1]), 10)
                if (get_distance((cursor2[0], cursor2[1]), HH_POS)) < 50:
                    hh_sound.play()
                    pygame.time.wait(int(hh_sound.get_length() * 100))
                if (get_distance((cursor2[0], cursor2[1]), SNARE_POS)) < 50:
                    snare_sound.play()
                    pygame.time.wait(int(snare_sound.get_length() * 1000))
                if (get_distance((cursor2[0], cursor2[1]), KICK_POS)) < 150:
                    kick_sound.play()
                    pygame.time.wait(int(kick_sound.get_length() * 1000))

            cursor = lmList[8]

            screen.blit( aim, (cursor[0] - 10, cursor[1] - 10) )

            length, info, = detector.findDistance( lmList[8], lmList[12], )

            if length < 30:
                pygame.draw.circle( screen, RED, (cursor[0], cursor[1]), 10 )
                if (get_distance((cursor[0], cursor[1]),HH_POS))<50:
                    hh_sound.play()
                    pygame.time.wait(int(hh_sound.get_length() * 100))
                if (get_distance((cursor[0], cursor[1]),SNARE_POS))<50:
                    snare_sound.play()
                    pygame.time.wait(int(snare_sound.get_length() * 1000))
                if (get_distance((cursor[0], cursor[1]),KICK_POS))<150:
                    kick_sound.play()
                    pygame.time.wait(int(kick_sound.get_length() * 1000))




def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img, flipType=False)

        screen.blit(bg, (0, 0))

        aim_handle(hands, detector)
        pygame.display.flip()

        cv2.imshow('Remote Drum', img)  # How we detect hand and measure distance in the background
        cv2.waitKey(1)
    pygame.quit()




if __name__ == '__main__':
    main()