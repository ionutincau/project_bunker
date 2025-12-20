################################################################################
## Custom Screens for The Desync
################################################################################

## HUD Screen - Shows timer and neural status
screen hud():
    zorder 100
    
    frame:
        xalign 0.98
        yalign 0.02
        background "#000000cc"
        padding (15, 10)
        
        vbox:
            spacing 5
            
            # Timer display
            if time_left > 0:
                $ minutes = time_left // 60
                $ seconds = time_left % 60
                text "TIME LEFT: [minutes:02d]:[seconds:02d]" size 24 color "#ff0000" font "fonts/Courier_New_Bold.ttf"
            else:
                text "TIME LEFT: 00:00" size 24 color "#ff0000" font "fonts/Courier_New_Bold.ttf"
            
            # Neural Latency
            text "LATENCY: [neural_latency]ms" size 18 color "#ffaa00"
            
            # Signal Penetration
            if signal_penetration > 0:
                text "SIGNAL: [signal_penetration]%%" size 18 color "#00ffff"

## Say screen with HUD overlay
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Show HUD during dialogue
    if not renpy.get_screen("hud"):
        use hud


## Choice screen with timer
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    ## Show HUD during choices
    use hud


## Main Menu
screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    frame:
        xalign 0.5
        yalign 0.5

        has vbox

        vbox:
            xalign 0.5
            yalign 0.5

            spacing 20

            text "{font=fonts/Courier_New_Bold.ttf}{size=60}{color=#00ffff}THE DESYNC{/color}{/size}{/font}" xalign 0.5

            text "{size=24}Est. Playtime: 15 Minutes{/size}" xalign 0.5

            null height 20

            textbutton _("Start Game") action Start()

            textbutton _("Load Game") action ShowMenu("load")

            textbutton _("Preferences") action ShowMenu("preferences")

            textbutton _("About") action ShowMenu("about")

            textbutton _("Quit") action Quit(confirm=not main_menu)


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background Frame("gui/overlay/main_menu.png", gui.main_menu_borders, tile=gui.main_menu_tile)

style main_menu_vbox:
    xalign 0.5
    xoffset 0
    xmaximum 1200
    yalign 0.5
    yoffset 0

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## About screen
screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            text _("A psychological sci-fi horror interactive fiction about Agent Xena, the last firewall, who must choose which survivor to save in a bunker as humanity falls to a neural virus called The Desync.\n")

            text _("Playtime: Approximately 15 minutes\n")

            text _("Mechanics: Real-time timer, hub-and-spoke exploration, hidden variables affecting endings\n")

            text _("Endings: 6 distinct endings based on your choices\n")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## NVL screen for narrator text
screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

    use hud


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "#000000dd"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
