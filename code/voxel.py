from ursina import *

# Définition des classes
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='brick', color_hex=None):
        try:
            super().__init__(
                parent=scene,
                position=position,
                model='cube',
                origin_y=0.5,
                texture=f"{texture}",
                highlight_color=color.light_gray,
                scale=1
            )
            if color_hex:
                self.color = hex_to_rgb(color_hex)
        except Exception as e:
            print(f"Erreur lors de la création du voxel : {e}")

# Définition des fonctions
def create_voxel(position=(0,0,0), texture="brick", color_hex=None):
    return Voxel(position, texture, color_hex)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return color.rgb(
        int(hex_color[:2], 16) / 255.0,
        int(hex_color[2:4], 16) / 255.0,
        int(hex_color[4:], 16) / 255.0
    )