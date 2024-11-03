import ursina
import os
import time
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
# Importation des dépendances customisés
from voxel import *
from player import *


# Définition des variables
mouse_locked = True
ressources_folder = "../ressources"
voxel_texture_folder = f"{ressources_folder}/voxel_texture/"
# Définition des variables de Ursina
app = Ursina()
window.fps_counter.enabled = True
window.borderless = False
window.exit_button.visible = False
window.title = "Minecraft"
window.icon = f"{ressources_folder}/UI/minecraft_logo.ico"

# Crétaion de la carte
os.system("cls")
for x in range(10):
    for y in range(10):
        Voxel = create_voxel(position=(x,0,y), texture=f"{voxel_texture_folder}grass_block", color_hex="#23AE43")

# Fonctions d'ursina            
def toggle_mouse_lock():
    global mouse_locked
    mouse_locked = not mouse_locked
    player.mouse_sensitivity = Vec2(40, 40) if mouse_locked else Vec2(0, 0)
    mouse.locked = mouse_locked
    mouse.visible = not mouse_locked

def input(key):
    if key == 'escape':  # Réagit uniquement quand la touche est pressée
        toggle_mouse_lock()

# Création du joueur
player = CustomFirstPersonController()

app.run()