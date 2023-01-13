import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame
import sys
import consts
from drum import Drum

def main():

    # Here we get the video stream from our webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 600)
    cap.set(4, 300)
    detector = HandDetector(detectionCon=0.8)

    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode(consts.SIZE)
    pygame.display.set_caption("Remote Drum")

    # Let's declare our image files to be used in the game.
    bg = pygame.image.load("resources/drum1.png") # background
    aim = pygame.image.load("resources/aim2.png")
    aim = pygame.transform.scale(aim, (25, 25))
    pygame.display.flip()

    drum = Drum(screen,aim,detector) # object handling the drumming part

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        success, img = cap.read()
        img = cv2.flip(img, 1)

        hands, img = detector.findHands(img, flipType=False) # detecting hands

        screen.blit(bg, (0, 0))

        drum.aim_handle(hands, detector) # it manages the aim and respective drumming actions
        pygame.display.flip()

        cv2.imshow('Remote Drum', img)
        cv2.waitKey(1)

    pygame.quit()


if __name__ == '__main__':
    main()