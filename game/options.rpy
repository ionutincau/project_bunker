## options.rpy - Game configuration for The Desync

## Game Information
define config.name = _("The Desync")
define config.version = "1.0"
define gui.about = _("A psychological sci-fi horror interactive fiction.")

## Build Configuration
define build.name = "TheDesync"

## Window Configuration
define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

## Default Text Speed
default preferences.text_cps = 40
default preferences.afm_time = 15

## Theme and GUI
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans-Bold.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"
define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 22
define gui.label_text_size = 28
define gui.notify_text_size = 16
define gui.title_text_size = 50

## Colors - Sci-fi/Horror theme
define gui.accent_color = "#00ffff"  # Teal
define gui.idle_color = "#888888"
define gui.idle_small_color = "#aaaaaa"
define gui.hover_color = "#00ffff"
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#444444"
define gui.muted_color = "#003d3d"
define gui.hover_muted_color = "#005d5d"

define gui.text_color = "#ffffff"
define gui.interface_text_color = "#ffffff"

## Main and Game Menu Backgrounds
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"
define gui.main_menu_borders = Borders(0, 0, 100, 0)
define gui.main_menu_tile = False

## Dialogue
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0
define gui.name_xpos = 240
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50
define gui.dialogue_width = 744
define gui.dialogue_text_xalign = 0.0

## Buttons
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_xalign = 0.0
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Choice Buttons
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#00ffff"

## NVL-Mode
define gui.nvl_borders = Borders(0, 0, 0, 0)
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_xalign = 1.0
define gui.nvl_name_yalign = 0.5
define gui.nvl_name_width = 150
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_xalign = 0.0
define gui.nvl_text_yalign = 0.0
define gui.nvl_text_width = 590
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_xalign = 0.0
define gui.nvl_thought_yalign = 0.0
define gui.nvl_thought_width = 780
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## History
define config.history_length = 250
define gui.history_height = 140
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

## Mobile Devices
define gui.quick_button_borders = Borders(10, 10, 10, 0)

## Localization
define gui.language = "english"

init python:
    ## Disable rollback (for timer integrity)
    config.rollback_enabled = False
    
    ## Custom save name
    config.save_directory = "TheDesync-1.0"
    
    ## Auto-save configuration
    config.has_autosave = True
    config.autosave_on_choice = True
    config.autosave_frequency = 200
    
    ## Skip Configuration
    config.allow_skipping = True
    config.fast_skipping = False
