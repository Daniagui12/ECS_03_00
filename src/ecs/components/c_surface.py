import pygame

class CSurface:
    def __init__(self, size:pygame.Vector2, color:pygame.Color) -> None:
        self.surf = pygame.Surface(size)
        self.surf.fill(color)

    @classmethod
    def from_surface(cls, surface:pygame.Surface):
        c_surf = cls(pygame.Vector2(0,0), pygame.Color(0, 0, 0))
        c_surf.surf = surface
        c_surf.area = surface.get_rect()
        return c_surf
    
    def get_area_relative(area:pygame.Rect, pos_top_left:pygame.Vector2):
        new_rect = area.copy()
        new_rect.topleft = pos_top_left.copy()
        return new_rect
        