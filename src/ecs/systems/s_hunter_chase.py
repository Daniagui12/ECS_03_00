import pygame
import esper
from src.ecs.components.c_hunter_info import CHunterInfo
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_hunter_chase(world: esper.World):
    player_transform = world.component_for_entity(1, CTransform)

    components = world.get_components(CVelocity, CTransform, CHunterInfo)

    c_v: CVelocity
    c_t: CTransform
    c_h_info: CHunterInfo
    for _, (c_v, c_t, c_h_info) in components:
        dist_player = distance_to(c_t.pos, player_transform.pos)
        dist_hunter = distance_to(c_t.pos, c_h_info.info.pos_init)
        if dist_player < c_h_info.info.dist_start_chase:
            c_v.vel = (player_transform.pos - c_t.pos).normalize() * c_h_info.info.vel_chase
            c_h_info.info.state = "chase"
        elif dist_hunter > c_h_info.info.dist_start_return:
            c_v.vel = (c_h_info.info.pos_init - c_t.pos).normalize() * c_h_info.info.vel_return
            c_h_info.info.state = "return"
        
        elif c_h_info.info.state == "return" and dist_hunter < 1:
            c_v.vel = pygame.Vector2(0,0)
            c_h_info.info.state = "stop"

        

def distance_to(pos1: pygame.Vector2, pos2: pygame.Vector2):
    return (pos1 - pos2).magnitude()
        
            