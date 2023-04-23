import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.tags.c_tag_explosion import CTagExplosion

def system_explosion_remover(world:esper.World):
    components = world.get_components(CAnimation, CTagExplosion)
    for entity, (c_a, c_tag_e) in components:
        # Remove it after the animation is done
        if c_a.curr_frame == c_a.animations_list[c_a.curr_anim].end:
            world.delete_entity(entity)