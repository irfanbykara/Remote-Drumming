import consts
import pygame

class Drum:

    def __init__(self,screen,aim,detector):
        super().__init__()
        self.screen = screen
        self.aim = aim
        self.detector = detector

    # method for calculating finger positions and their distance then playing drums accordingly
    def aim_handle(self,hands,detector):
        if hands: # If hands found
            landmark_list = hands[0]['lmList'] # first detected hand
            if len(hands) == 2:
                landmark_list_2 = hands[1]['lmList']  # second detected hand
                cursor2 = landmark_list_2[8]
                self.screen.blit(self.aim, (cursor2[0] - 10, cursor2[1] - 10))
                length2, info2, = detector.findDistance(landmark_list_2[8], landmark_list_2[12], )
                if length2 < 30:
                    self.play_drum(consts.BLACK, cursor2)

                cursor = landmark_list[8]

                self.screen.blit(self.aim, (cursor[0] - 10, cursor[1] - 10))

                length, info, = self.detector.findDistance(landmark_list[8], landmark_list[12], )

                if length < 30:
                    self.play_drum(consts.RED, cursor)

    # Play the drum if the playing action is taken on drum parts, (hi-hat, snare, kick)
    def play_drum(self,color,cursor):
        pygame.draw.circle(self.screen, color, (cursor[0], cursor[1]), 10)
        if (self.get_distance((cursor[0], cursor[1]), consts.HH_POS)) < 50:
            consts.HH_SOUND.play()
            pygame.time.wait(int(consts.HH_SOUND.get_length() * 100))
        if (self.get_distance((cursor[0], cursor[1]), consts.SNARE_POS)) < 50:
            consts.SNARE_SOUND.play()
            pygame.time.wait(int(consts.SNARE_SOUND.get_length() * 1000))
        if (self.get_distance((cursor[0], cursor[1]), consts.KICK_POS)) < 150:
            consts.KICK_SOUND.play()
            pygame.time.wait(int(consts.KICK_SOUND.get_length() * 1000))

    @staticmethod
    def get_distance(pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5



