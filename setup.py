#!/usr/bin/env python3
"""
Setup script for The Desync Ren'Py game
Creates necessary directories and placeholder files
"""

import os
import shutil

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_DIR = os.path.join(BASE_DIR, "game")

# Create directory structure
directories = [
    os.path.join(GAME_DIR, "images"),
    os.path.join(GAME_DIR, "audio"),
    os.path.join(GAME_DIR, "gui"),
    os.path.join(GAME_DIR, "gui", "overlay"),
    os.path.join(GAME_DIR, "fonts"),
]

print("Creating directory structure for The Desync...")
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"✓ Created: {directory}")

# Create placeholder image list
image_placeholders = [
    "black.png",
    "purple_sky.png",
    "tower_pulse.png",
    "hud_boot.png",
    "airlock_red.png",
    "airlock_teal.png",
    "hud_glitch.png",
    "glass_fracture.png",
    "blast_doors.png",
    "sanctum_sealed.png",
    "kai_interface.png",
    "waveform_overlay.png",
    "kai_typing.png",
    "kai_possessed.png",
    "panel_broken.png",
    "xena_weapon.png",
    "mina_concentration.png",
    "mina_whitehair.png",
    "mina_collapse.png",
    "mina_typing.png",
    "teal_dissolve.png",
    "dark_bunker.png",
]

# Create placeholder text file for missing images
images_dir = os.path.join(GAME_DIR, "images")
placeholder_info_path = os.path.join(images_dir, "PLACEHOLDER_INFO.txt")

with open(placeholder_info_path, "w") as f:
    f.write("PLACEHOLDER IMAGES NEEDED\n")
    f.write("=" * 50 + "\n\n")
    f.write("The following images should be placed in this directory:\n\n")
    for img in image_placeholders:
        f.write(f"  - {img}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write("You can use the generated images from artifacts or create your own.\n")

print(f"\n✓ Created placeholder info: {placeholder_info_path}")

# Create audio placeholder info
audio_dir = os.path.join(GAME_DIR, "audio")
audio_info_path = os.path.join(audio_dir, "AUDIO_INFO.txt")

audio_files = [
    "bass_hum.ogg - Low, throbbing bass sound",
    "glitch.ogg - Digital glitch sound effect",
    "smash.ogg - Panel smashing sound",
    "distortion.ogg - Audio distortion",
    "glass_crack.ogg - Glass cracking",
    "door_grind.ogg - Heavy doors grinding",
    "horror.ogg - Horror sting",
    "wire_rip.ogg - Electrical wire ripping",
    "lullaby.ogg - Calm lullaby music",
    "desync.ogg - Desync effect sound",
    "massive_thrum.ogg - Deep, bone-shaking sound",
]

with open(audio_info_path, "w") as f:
    f.write("AUDIO FILES NEEDED\n")
    f.write("=" * 50 + "\n\n")
    f.write("The following audio files should be placed in this directory:\n\n")
    for audio in audio_files:
        f.write(f"  - {audio}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write("Note: If audio files are missing, the game will still run.\n")
    f.write("Ren'Py will simply skip playing the missing sounds.\n")

print(f"✓ Created audio info: {audio_info_path}")

# Create simple black placeholder image using PIL if available
try:
    from PIL import Image
    
    # Create black image
    black_img = Image.new('RGB', (1920, 1080), color='black')
    black_img.save(os.path.join(images_dir, "black.png"))
    print(f"✓ Created black.png placeholder")
    
    # Create simple colored backgrounds for testing
    purple_sky = Image.new('RGB', (1920, 1080), color=(75, 50, 100))
    purple_sky.save(os.path.join(images_dir, "purple_sky.png"))
    print(f"✓ Created purple_sky.png placeholder")
    
    teal_bg = Image.new('RGB', (1920, 1080), color=(0, 100, 100))
    teal_bg.save(os.path.join(images_dir, "tower_pulse.png"))
    print(f"✓ Created tower_pulse.png placeholder")
    
except ImportError:
    print("\n⚠ PIL/Pillow not available. Skipping placeholder image generation.")
    print("  Install with: pip install pillow")

# Create GUI background placeholder
gui_dir = os.path.join(GAME_DIR, "gui")
gui_info_path = os.path.join(gui_dir, "GUI_INFO.txt")

with open(gui_info_path, "w") as f:
    f.write("GUI IMAGES NEEDED\n")
    f.write("=" * 50 + "\n\n")
    f.write("Place these files in the gui/ directory:\n\n")
    f.write("  - main_menu.png (1920x1080 - Dark sci-fi background)\n")
    f.write("  - game_menu.png (1920x1080 - Dark background for pause menu)\n")
    f.write("\n")
    f.write("Note: Generated main_menu_background image can be used.\n")

print(f"✓ Created GUI info: {gui_info_path}")

print("\n" + "=" * 50)
print("Setup complete!")
print("=" * 50)
print("\nNext steps:")
print("1. Move generated images from artifacts to game/images/")
print("2. Add audio files to game/audio/ (optional)")
print("3. Open Ren'Py Launcher and select this project")
print("4. Click 'Launch Project' to play!")
print("\nProject location:", BASE_DIR)
