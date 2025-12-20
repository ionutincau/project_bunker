## images.rpy - Image definitions and placeholders

## Define solid color placeholders for missing images
image black = Solid("#000000")
image purple_sky = Solid("#4a2866")
image tower_pulse = Solid("#006666")
image hud_boot = Solid("#1a1a1a")
image airlock_red = Solid("#330000")
image airlock_teal = Solid("#003333")
image hud_glitch = Solid("#1a1a1a")
image glass_fracture = Solid("#002222")
image blast_doors = Solid("#1a1a1a")
image sanctum_sealed = Solid("#0d0d0d")
image kai_interface = Solid("#001a33")
image waveform_overlay = Solid("#00333300")  # Transparent overlay
image kai_typing = Solid("#001a33")
image kai_possessed = Solid("#003333")
image panel_broken = Solid("#331100")
image xena_weapon = Solid("#1a0000")
image mina_concentration = Solid("#001a00")
image mina_whitehair = Solid("#333333")
image mina_collapse = Solid("#1a1a00")
image mina_typing = Solid("#001a00")
image teal_dissolve = Solid("#00666699")  # Semi-transparent teal
image dark_bunker = Solid("#000000")

## Show statements for special effects
transform glitch_effect:
    alpha 1.0
    linear 0.1 alpha 0.7
    linear 0.1 alpha 1.0
    repeat 3

transform teal_pulse:
    alpha 0.3
    linear 1.0 alpha 0.8
    linear 1.0 alpha 0.3
    repeat

## Note: Replace these with actual image files in game/images/
## These are just fallback placeholders so the game runs without errors
