import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame
import sys
import consts
import utils

#Basic util to calculate the euclidian distance




# Here we get the video stream from our webcam
cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,300)
detector = HandDetector( detectionCon=0.8 )

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode( consts.SIZE )
pygame.display.set_caption( "Remote Drum" )

# Let's declare our image files to be used in the game.
bg = pygame.image.load("resources/drum1.png")
aim = pygame.image.load("resources/aim2.png")
aim = pygame.transform.scale(aim, (25, 25))
pygame.display.flip()


def aim_handle(hands, detector):
    if hands:
        lmList = hands[0]['lmList']
        if len(hands) == 2 :
            lmList2 = hands[1]['lmList']
            cursor2 = lmList2[8]
            screen.blit(aim, (cursor2[0] - 10, cursor2[1] - 10))
            length2, info2, = detector.findDistance(lmList2[8], lmList2[12], )
            if length2 < 30:
                play_drum(consts.BLACK, cursor2)

            cursor = lmList[8]

            screen.blit( aim, (cursor[0] - 10, cursor[1] - 10) )

            length, info, = detector.findDistance( lmList[8], lmList[12], )

            if length < 30:
                play_drum(consts.RED,cursor)

def play_drum(color,cursor):
    pygame.draw.circle(screen, color, (cursor[0], cursor[1]), 10)
    if (utils.get_distance((cursor[0], cursor[1]), consts.HH_POS)) < 50:
        consts.HH_SOUND.play()
        pygame.time.wait(int(consts.HH_SOUND.get_length() * 100))
    if (utils.get_distance((cursor[0], cursor[1]), consts.SNARE_POS)) < 50:
        consts.SNARE_SOUND.play()
        pygame.time.wait(int(consts.SNARE_SOUND.get_length() * 1000))
    if (utils.get_distance((cursor[0], cursor[1]), consts.KICK_POS)) < 150:
        consts.KICK_SOUND.play()
        pygame.time.wait(int(consts.KICK_SOUND.get_length() * 1000))


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