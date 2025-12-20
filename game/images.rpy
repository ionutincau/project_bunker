image black = Solid("#000000")
image white = Solid("#ffffff")
image dark_bunker = Solid("#050510")
image teal_dissolve = Solid("#00666699")
image waveform_overlay = Solid("#00333366")

transform glitch_effect:
    alpha 1.0
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 alpha 0.8
    linear 0.05 alpha 1.0
    xoffset 0
    repeat 4

transform teal_pulse:
    matrixcolor TintMatrix("#00ffff")
    alpha 0.4
    linear 1.5 alpha 0.7
    linear 1.5 alpha 0.4
    repeat

transform camera_shake:
    linear 0.1 xoffset 10 yoffset 10
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    repeat 2
