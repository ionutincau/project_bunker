## HUD Screen - timer and neural status
screen hud():
    zorder 100
    
    # Timer to decrement time_left every second and trigger events
    if time_left > 0:
        timer 1.0 action [
            SetVariable("time_left", time_left - 1),
            If(time_left <= 300 and not turning_point_triggered, true=Jump("turning_point")),
            If(time_left <= 60 and current_label not in ["deterioration", "final_selection", "ending_kai", "ending_trent", "ending_lisa", "ending_mina", "ending_mina_fear", "ending_mina_wrong_song", "ending_mina_true"], true=Jump("deterioration"))
        ] repeat True
        
    frame:
        xalign 0.98
        yalign 0.02
        background "#000000cc"
        padding (15, 10)
        
        vbox:
            spacing 5
            
            # Timer display
            if time_left > 0:
                $ minutes = int(time_left // 60)
                $ seconds = int(time_left % 60)
                text "TIME LEFT: [minutes:02d]:[seconds:02d]" size 24 color "#ff0000"
            else:
                text "TIME LEFT: 00:00" size 24 color "#ff0000"
            
            # Neural Latency
            text "LATENCY: [neural_latency]ms" size 18 color "#ffaa00"
            
            # Signal Penetration
            if signal_penetration > 0:
                text "SIGNAL: [signal_penetration]%" size 18 color "#00ffff"

## Say screen with HUD overlay
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        vbox:
            xalign 0.5
            ypos 20
            xsize gui.dialogue_width

            if who is not None:
                window:
                    style "namebox"
                    text who id "who" xalign 0.5
                
                null height 5

            text what id "what" xalign 0.5

    ## Show HUD during dialogue
    if not renpy.get_screen("hud"):
        use hud

style namebox is default
style say_label is default
style say_dialogue is default
style say_window is default

style namebox:
    xalign 0.5
    background None
    xpadding 0
    ypadding 0

style say_label:
    size gui.name_text_size
    font gui.name_text_font
    color gui.accent_color
    xalign 0.5
    text_align 0.5
    yalign 0.5

style say_dialogue:
    size gui.text_size
    font gui.text_font
    text_align 0.5
    xalign 0.5

style say_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background "#000000cc"


screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.6
        spacing 15

        for i in items:
            textbutton i.caption action i.action

    ## Show HUD during choices
    use hud

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_button:
    background Solid("#000000aa")
    hover_background Solid("#00ffff33")
    padding (40, 10)
    xsize 800
    xalign 0.5
    
style choice_button_text:
    idle_color "#cccccc"
    hover_color "#00ffff"
    size 28
    xalign 0.5
    text_align 0.5
    outlines [ (1, "#000000", 0, 0) ]


## Main Menu
screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background xalign 0.5 yalign 0.5

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5

            spacing 20

            text "{size=60}{color=#00ffff}THE DESYNC{/color}{/size}" xalign 0.5

            if not main_menu:
                textbutton _("Resume") action Return() xalign 0.5

            textbutton _("Start Game") action Start() xalign 0.5

            textbutton _("Quit") action Quit(confirm=not main_menu) xalign 0.5


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xalign 0.5
    yalign 0.5
    yfill True
    padding (40, 40)
    background "#000000aa"

style main_menu_vbox:
    xalign 0.5
    xoffset 0
    xmaximum 1200
    yalign 0.5
    yoffset 0

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    xalign 0.5
    text_align 0.5

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## NVL screen for narrator text
screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        vbox:
            xalign 0.5
            yalign 0.4
            spacing gui.nvl_spacing
            
            use nvl_dialogue(dialogue)

            for i in items:
                textbutton i.caption:
                    action i.action
                    style "nvl_button"
                    xalign 0.5

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
    xalign 0.5
    text_align 0.5
    size 24
    xsize 1200
    layout "subtitle"

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


## Confirm screen
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    
    add "#000000aa"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 60)
        background "#000000cc"
        
        vbox:
            xalign 0.5
            spacing 45

            label _(message):
                xalign 0.5
                text_text_align 0.5

            hbox:
                xalign 0.5
                spacing 150
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

## Notify screen
screen notify(message):
    zorder 100
    frame:
        at notify_appear
        xalign 1.0
        ypos 100
        background "#000000cc"
        padding (20, 10)
        text "[message!t]"
    timer 3.2 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

## Skip indicator
screen skip_indicator():
    zorder 100
    frame:
        xalign 1.0
        ypos 10
        background "#000000cc"
        padding (20, 10)
        hbox:
            spacing 9
        text _("Skipping")
        text "▸" at delayed_blink(0.0, 1.0)
        text "▸" at delayed_blink(0.2, 1.0)
        text "▸" at delayed_blink(0.4, 1.0)

transform delayed_blink(delay, cycle):
    alpha 1.0
    pause delay
    block:
        linear .2 alpha .2
        linear .2 alpha 1.0
        pause (cycle - .4)
        repeat
