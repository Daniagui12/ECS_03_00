import pygame

class CHunterInfo:
    def __init__(self, vel_chase: int, vel_return: int, dist_start_chase: int, dist_start_return: int, pos_init: pygame.Vector2):
        self.info = HunterInfoData(vel_chase, vel_return, dist_start_chase, dist_start_return, pos_init)

class HunterInfoData:
    def __init__(self, vel_chase: int, vel_return: int, dist_start_chase: int, dist_start_return: int, pos: pygame.Vector2):
        self.vel_chase = vel_chase
        self.vel_return = vel_return
        self.dist_start_chase = dist_start_chase
        self.dist_start_return = dist_start_return
        self.pos_init = pos
        self.state = "idle"