import esper
import pygame
from src.create.prefab_creator import create_explosion
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_hunter import CTagHunter

def system_collision_player_enemy(world:esper.World, player_entity:int, level_cfg:dict, explosion_info:dict):
    components = world.get_components(CSurface, CTransform, CTagEnemy)
    components_hunter = world.get_components(CSurface, CTransform, CTagHunter)
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)
    pl_rect = CSurface.get_area_relative(pl_s.area, pl_t.pos)

    player_pos = pygame.Vector2(pl_t.pos.x, pl_t.pos.y)
    
    for enemy_entity, (c_s, c_t, _) in components + components_hunter:
        ene_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if ene_rect.colliderect(pl_rect):
            # create_explosion(world, c_t.pos, explosion_info)
            create_explosion(world, player_pos, explosion_info)
            world.delete_entity(enemy_entity)
            pl_t.pos.x = level_cfg["player_spawn"]["position"]["x"] - pl_s.surf.get_width() / 2
            pl_t.pos.y = level_cfg["player_spawn"]["position"]["y"] - pl_s.surf.get_height() / 2