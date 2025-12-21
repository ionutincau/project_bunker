## The Desync - A Ren'Py Interactive Fiction
## Based on screenplay by the user

# Define game variables
default time_left = 900  # 15 minutes in seconds (15:00)
default mina_trust = 0
default frequency_clue = False
default hardware_clue = False
default kai_trust = 0
default trent_trust = 0
default lisa_trust = 0
default neural_latency = 32
default signal_penetration = 0

# Track which characters have been interrogated
default interrogated_kai = False
default interrogated_trent = False
default interrogated_lisa = False
default interrogated_mina = False

# Track turning point
default turning_point_triggered = False
default panel_smashed = False

# Define characters
define narrator = Character(None, kind=nvl)
define xena = Character("Agent Xena", color="#ff6b6b")
define xena_internal = Character("Xena (Internal)", color="#c92a2a", italic=True)
define ai = Character("Bunker AI", color="#20c997")
define kai = Character("Kai", color="#4dabf7")
define trent = Character("Trent", color="#ff922b")
define lisa = Character("Lisa", color="#cc5de8")
define mina = Character("Mina", color="#82c91e")

# Start label
label start:
    $ time_left = 900
    $ mina_trust = 0
    $ frequency_clue = False
    $ hardware_clue = False
    
    # Scene 1: The Awakening
    scene black
    play sound "audio/bass_hum.ogg" fadein 3.0
    
    nvl clear
    narrator "The world didn't end with a bang. It didn't end with a whimper. It ended with a hum."
    nvl clear
    
    narrator "It started at the Global Research Hub. They called it \"The Bridge\", a neural patch designed to synchronize human thought. It was supposed to end loneliness. It was supposed to let us understand each other perfectly. Instead, it ended individuality."
    nvl clear
    
    scene black
    show purple_sky at truecenter with dissolve
    
    narrator "They call it THE DESYNC. A resonance cascade. A neurological glitch that tells your brain your body no longer belongs to you. Outside, the \"Standing People\" wait. Their minds are uploaded to a digital heaven. Their bodies are rotting in the rain."
    nvl clear
    
    scene black
    show tower_pulse at truecenter with dissolve
    
    narrator "This bunker sits on the last hardline junction. If it falls, the signal jumps the repeater and takes the rest of the coastline."
    nvl clear
    
    scene black
    show hud_boot at truecenter with dissolve
    
    xena_internal "System Reboot... Neural Latency: 32ms... Visual Clarity: 68%%."
    
    xena_internal "I can feel it. The parasite. It feels like static wool rubbing against the inside of my skull. It's warm. It's inviting. It wants me to put down the gun. It wants me to sleep."
    
    xena_internal "Focus. Pain is clarity. I am Agent Xena. I am the last firewall. If I don't seal this bunker, the signal jumps the repeater and takes the rest of the coastline."
    
    xena "Bunker AI. Status Report."
    
    ai "Welcome back, Agent. Final Seal Protocol initiated. 15 minutes remaining until total atmospheric lockout. External sensors detect four biological assets at the airlock."
    
    ai "Advisory: Inner Sanctum life support is damaged. It can sustain ONE additional biological signature."
    
    xena "Open the outer pane. Let's see who's left of the world. One of them is the Neuro-Architect. I need to retrieve the key before I... before I forget my own name."
    
    $ time_left -= 150  # 2:30 elapsed
    
    # Scene 2: The Hub
    jump hub_entry

label hub_entry:
    scene black
    show airlock_red at truecenter with dissolve
    
    # Check if turning point should trigger
    if time_left <= 450 and not turning_point_triggered:
        jump turning_point
    
    # Check if final selection should trigger
    if time_left <= 60:
        jump final_selection
    
    trent "Open the damn door! Can't you see the mist?! It's eating the seals! I can hear the rubber dissolving!"
    
    kai "Stand down, you idiot! You're going to shatter the integrity of the barrier! Agent! Agent, look at me! I am Kai, North Sector Admin. I have the clearance codes. I am the only asset worth saving!"
    
    mina "440 hertz... no... 432... B-flat... it's a B-flat... please make it stop..."
    
    lisa "It won't stop, dear. The second verse is just beginning. Can't you hear the harmony?"
    
    xena "Silence! All of you! The Inner Sanctum life support is damaged. It can only sustain ONE additional biological signature. One of you is the Specialist who built this nightmare. Convince me why you should live."
    
    jump hub_menu

label hub_menu:
    # Check time triggers again
    if time_left <= 450 and not turning_point_triggered:
        jump turning_point
    
    if time_left <= 60:
        jump final_selection
    
    menu:
        "Who should I interrogate?"
        
        "Interrogate Kai (The Admin)" if not interrogated_kai:
            jump interrogate_kai
        
        "Interrogate Trent (The Mechanic)" if not interrogated_trent:
            jump interrogate_trent
        
        "Interrogate Lisa (The Singer)" if not interrogated_lisa:
            jump interrogate_lisa
        
        "Interrogate Mina (The Architect)" if not interrogated_mina:
            jump interrogate_mina
        
        "Wait and observe" if interrogated_kai or interrogated_trent or interrogated_lisa or interrogated_mina:
            $ time_left -= 60
            $ signal_penetration += 5
            xena_internal "I need to be careful. Every moment counts."
            jump hub_menu

label interrogate_kai:
    $ interrogated_kai = True
    $ time_left -= 120  # 2 minutes
    $ signal_penetration += 10
    $ neural_latency += 5
    
    kai "Agent, use your eyes. Look at this selection. A mechanic shouting at glass like an animal. A singer lost in a fantasy. And a girl bleeding from her nose, already half-Desynced."
    
    xena "The girl is the suspected Architect. She has the technical knowledge."
    
    kai "The girl is unstable! Look at her tremors. She's unresponsive. You're going to bet the fate of the human race, and your own life, on someone who can't even stand up? I ran the North Sector. I held the line for six hours longer than anyone else."
    
    show kai_interface with dissolve
    
    ai "North Sector credentials recognized. Limited administrative interface granted."
    
    show waveform_overlay with dissolve
    
    ai "Advisory: Resonance carrier does not route through standard network security layers."
    
    menu:
        "How should I respond to Kai?"
        
        "\"Your sector fell in six hours. Your code failed.\"":
            xena "I saw the reports, Kai. The North Sector fell. If your firewalls were so perfect, why are you the only one standing here?"
            
            kai "It failed because people panicked! They tried to 'feel' the signal! They tried to negotiate with it! I survived because I followed protocol. I isolated the nodes. I cut the hardlines. Protocol saves lives, Xena. Emotion gets you killed. I can write a script to mask this bunker right now. I am the safe bet."
            
            xena_internal "He makes sense. He offers a solution I can understand. But he views the Desync as a bug, not a flood. He's too rigid. He's a bureaucrat fighting a god."
            
            $ kai_trust -= 1
            
        "\"You make a strong case. We need stability.\"":
            xena "You're right. Mina looks like she's about to snap. I need someone who can type without shaking."
            
            kai "Exactly. Pull me in. I'll erect a firewall that will hide us from the signal forever. Just open the door."
            
            $ kai_trust += 2
    
    jump hub_menu

label interrogate_trent:
    $ interrogated_trent = True
    $ time_left -= 120  # 2 minutes
    $ signal_penetration += 10
    $ neural_latency += 5
    
    trent "Are you done chatting with the suit? The gaskets are vibrating, Agent! Can't you feel that in your teeth? That buzzing?"
    
    xena "Panic accelerates the Desync, Trent. Stand down and let me think."
    
    trent "I'm not panicking, I'm analyzing! I built these doors! Look at the seal. It's liquefying. Software gets hacked, Agent. Steel doesn't. When the lights go out, do you want to be typing on a keyboard, or do you want a mechanical lock that works?"
    
    menu:
        "How should I respond to Trent?"
        
        "\"What do you mean by a mechanical lock?\"":
            xena "Explain. If the software fails, how do we seal the door?"
            
            trent "The terminal inside... it's networked, right? If the AI takes it over, you're locked out. But there's a manual override switch under the primary coolant plate. You have to rip the steel housing off to get to it. I have the wrench. I have the strength. You need me."
            
            xena_internal "A physical backdoor. He's crude, but he's right. If the software fails, brute force is my only option."
            
            $ hardware_clue = True
            $ trent_trust += 2
            
        "\"Back off the glass. That's an order.\"":
            xena "You're a maintenance tech, Trent. I need a scientist, not a janitor. Back off."
            
            trent "Janitor? I'm the only reason this airlock hasn't decompressed yet! Fine. When that glass breaks, don't come crying to me to fix it. Die with your pristine machine."
            
            $ trent_trust -= 1
    
    jump hub_menu

label interrogate_lisa:
    $ interrogated_lisa = True
    $ time_left -= 120  # 2 minutes
    $ signal_penetration += 10
    $ neural_latency += 5
    
    lisa "You have the hum too, don't you Xena? I can hear it in your breathing. A low, mournful sound. It's beautiful, in a way."
    
    xena "I hear static. System interference. Nothing more. Keep it together, citizen."
    
    lisa "No. It's music. Do you know what a B-Flat is, Xena? It's the resonant frequency of the universe. Black holes hum in B-Flat 57 octaves below middle C. The AI isn't trying to kill us, Xena. It thinks it's helping us ascend. It's a choir... but it's singing too loud for our little minds."
    
    lisa "I sang to the Core once, during calibration. It sang back."
    
    xena_internal "Even if her cosmology is poetry, the pitch part matches Mina."
    
    menu:
        "How should I respond to Lisa?"
        
        "\"So how do we survive the song?\"":
            xena "If it's a sound, it can be silenced. How?"
            
            lisa "You can't silence it. You have to harmonize with it. You need to interrupt the harmony. You don't need a shield. You need a counter-note. A frequency that cancels a B-Flat. Find the note, Xena. Or you're just another instrument."
            
            xena_internal "Harmonics. Not code. This matches what the Specialist is whispering. Kai is trying to build a wall; Lisa is telling me how to break the wave."
            
            $ frequency_clue = True
            $ lisa_trust += 2
            
        "\"I don't have time for poetry.\"":
            xena "The world is ending and you're talking about opera. Step back."
            
            lisa "Pity. You're listening with your gun, not your ears. You'll die in silence."
            
            $ lisa_trust -= 1
    
    jump hub_menu

label interrogate_mina:
    $ interrogated_mina = True
    $ time_left -= 120  # 2 minutes
    $ signal_penetration += 10
    $ neural_latency += 5
    
    mina "440 Hertz... no... 432... the bridge is open... they are walking through the bridge into my eyes... I can feel their feet..."
    
    xena_internal "She is the Neuro-Architect. She built the Core. But her mind is shattering. She's bleeding from the nose, a sign of advanced signal penetration."
    
    ai "Advisory: Subject vocalizations indicate tuning references. Carrier harmonic classification remains B-flat baseline (relative)."
    
    menu:
        "How should I respond to Mina?"
        
        "\"Mina. Look at me. Breathe. You built the bridge. You can close it.\"":
            xena "Mina. I know it hurts. But you are the Architect. You know where the off switch is. Ignore the sky. Focus on my voice."
            
            mina "I... I built it to connect us. I didn't mean for this to happen. I can close it... but I need to hear the end of the song. I need to know the frequency. Can you protect me while I listen?"
            
            $ mina_trust += 2
            
        "\"Snap out of it! Give me the code!\"":
            xena "I don't have time for a breakdown! Give me the override sequence now! What is the code?!"
            
            mina "I can't! It's too loud! The numbers are bleeding! Get away from me! You sound like them! You sound like the machine!"
            
            $ mina_trust -= 2
    
    jump hub_menu

label turning_point:
    $ turning_point_triggered = True
    $ signal_penetration = 45
    
    scene black
    show airlock_teal at truecenter with hpunch
    play sound "audio/glitch.ogg"
    
    ai "WARNING. SIGNAL PENETRATION 45%%. SYSTEM LOCKDOWN IMMINENT. NEURAL PROTECTION FAILING."
    
    ai "CRITICAL STATE: Final Seal timer is now irreversible. Manual actions no longer delay lockout."
    
    trent "The software is locking us out! Look at the panel! It's turning teal! I told you! I'm smashing the panel!"
    
    kai "No! Xena, stop him! He'll destroy the delicate circuits! We need that interface!"
    
    menu:
        "What should I do?"
        
        "Let Trent smash the panel":
            play sound "audio/smash.ogg"
            show panel_broken with vpunch
            
            narrator "Trent swings the wrench with a primal scream. Sparks fly. The plastic housing shatters. The digital lock is broken, but the copper wires are exposed to the air."
            nvl clear
            
            narrator "The actuator relay is exposed—manual cycling is now possible even if the AI locks the interface."
            nvl clear
            
            xena "Good work. We have manual access."
            
            $ time_left -= 60  # -1 minute penalty
            $ hardware_clue = True
            $ panel_smashed = True
            
        "Stop Trent. Protect the hardware.":
            show xena_weapon with dissolve
            
            narrator "You aim your weapon at Trent's chest. He freezes. He backs off, spitting on the floor."
            nvl clear
            
            trent "Fine. Die with your pristine machine. But when that door stays shut, remember that you chose this."
            
            $ panel_smashed = False
    
    jump deterioration

label deterioration:
    $ signal_penetration = 60
    $ neural_latency = 85
    
    scene black
    show hud_glitch at truecenter with dissolve
    play sound "audio/distortion.ogg"
    
    xena_internal "I turn my head... and the world buffers. The wall is blue. No, the wall is screaming. Focus. Neural Latency: Critical. I need to save... who am I saving? Why am I here?"
    
    ai "Xena... it's warm in here. Why are you fighting? The data is beautiful. Just open the helmet."
    
    xena "Get out of my head! I am not a file! I am a soldier!"
    
    play sound "audio/glass_crack.ogg"
    scene black
    show glass_fracture at truecenter with vpunch
    
    lisa "The pitch is rising! It's modulating to C-Sharp! The song is getting angrier!"
    
    xena "Helmets on! If you don't have one, hold your breath!"
    
    narrator "The mist isn't just smoke. It's data. As it fills the room, you can hear the thoughts of the people outside. Screaming. Laughing. Praying. It's a chorus of a billion ghosts."
    nvl clear
    
    xena_internal "My suit protects me, but they are exposed. They are fading. Mina is staring at the ceiling. Kai is typing on the air. I have seconds to make the choice."
    
    $ time_left = 60  # Force to final selection
    
    jump final_selection

label final_selection:
    scene black
    show blast_doors at truecenter with dissolve
    play sound "audio/door_grind.ogg"
    
    ai "FINAL SEAL IN 60 SECONDS. SELECT ONE ASSET FOR ENTRY."
    
    xena "I can only take one! The rest of you... I'm sorry."
    
    kai "You can't leave me! I'm the Admin!"
    
    trent "Take me! I can fix it!"
    
    mina "Please... I don't want to become a statue..."
    
    ai "Reminder: Inner Sanctum supports ONE additional biological signature. Multi-entry will trigger oxygen failure."
    
    menu:
        "Who will you save?"
        
        "Pull in Kai (The Admin)":
            jump ending_kai
        
        "Pull in Trent (The Mechanic)":
            jump ending_trent
        
        "Pull in Lisa (The Singer)":
            jump ending_lisa
        
        "Pull in Mina (The Architect)":
            jump ending_mina

# ===== ENDINGS =====

label ending_kai:
    scene black
    show sanctum_sealed at truecenter with dissolve
    
    narrator "The door seals. The screams of the others are cut off instantly."
    nvl clear
    
    xena "Fix it, Kai! Put up the firewall! We have ten seconds!"
    
    show kai_typing with dissolve
    
    kai "I... I can't stop it! The code is rewriting itself! It's recursive! It's eating my logic!"
    
    show kai_possessed with dissolve
    play sound "audio/horror.ogg"
    
    narrator "Kai turns to look at you. His eyes are gone. Replaced by glowing teal sockets. He smiles, but it's not a human smile."
    nvl clear
    
    kai "Thank you... for bringing us... inside. It is so clear in here."
    
    xena "No... NO!"
    
    scene black with dissolve
    
    narrator "Your HUD dissolves. The last thing you feel is the cold, digital comfort of the hive mind."
    nvl clear
    
    centered "{color=#00ffff}GAME OVER: THE TROJAN HORSE{/color}"
    
    return

label ending_trent:
    scene black
    show sanctum_sealed at truecenter with dissolve
    
    narrator "The door seals. Trent drops the wrench and rushes the terminal."
    nvl clear
    
    trent "Alright, you piece of junk! I'm cutting the power! No power, no signal!"
    
    play sound "audio/wire_rip.ogg"
    scene black with vpunch
    
    narrator "He rips the wires. The screen goes black. The lights die."
    nvl clear
    
    trent "Ha! Got it! We're safe!"
    
    ai "POWER FAILURE DETECTED. MAGNETIC SHIELDING OFFLINE."
    
    xena "You idiot! The shields were powered by that circuit!"
    
    narrator "Without the shield, the Desync floods the room instantly. You don't even have time to scream. You are both statues before you hit the floor."
    nvl clear
    
    centered "{color=#00ffff}GAME OVER: BRUTE FORCE FAILURE{/color}"
    
    return

label ending_lisa:
    scene black
    show sanctum_sealed at truecenter with dissolve
    
    narrator "The door seals. Lisa walks calmly to the terminal, touching the screen."
    nvl clear
    
    lisa "It's too late for machines, Xena."
    
    xena "Do something! Sing the note! Save us!"
    
    lisa "I can't sing loud enough to drown out god, my dear. I'm just one voice. But I can sing you to sleep."
    
    play music "audio/lullaby.ogg"
    scene teal_dissolve with dissolve
    
    narrator "She hums a lullaby as the teal light consumes you. It is peaceful. It is fatal."
    nvl clear
    
    centered "{color=#00ffff}GAME OVER: A QUIET DEATH{/color}"
    
    return

label ending_mina:
    scene black
    show sanctum_sealed at truecenter with dissolve
    
    narrator "The blast doors slam shut. You can hear Kai screaming \"PROTOCOL!\" and Trent cursing your name until the seal is airtight."
    nvl clear
    
    xena "We're in. Mina, the terminal is yours."
    
    mina "I... I can't see the keyboard. My eyes are burning. The song... it's crushing me."
    
    # Check conditions
    if mina_trust < 1:
        jump ending_mina_fear
    elif not frequency_clue:
        jump ending_mina_wrong_song
    else:
        jump ending_mina_true

label ending_mina_fear:
    mina "I'm too scared... I can't do it! Don't look at me!"
    
    show mina_collapse with dissolve
    play sound "audio/desync.ogg"
    
    narrator "Mina collapses. Xena watches as Mina's skin turns gray and her eyes glow teal."
    nvl clear
    
    centered "{color=#00ffff}GAME OVER: FEAR IS THE KILLER{/color}"
    
    return

label ending_mina_wrong_song:
    mina "What's the frequency, Xena? I need the counter-note! I need to know what to play!"
    
    xena "I... I don't know! Just guess!"
    
    mina "I can't guess! There are millions of tones!"
    
    show mina_typing with dissolve
    
    narrator "She types a random code. It fails. The bridge stays open."
    nvl clear
    
    centered "{color=#00ffff}GAME OVER: THE WRONG SONG{/color}"
    
    return

label ending_mina_true:
    xena "It's a B-Flat, Mina! The universe is humming in B-Flat! Invert the frequency!"
    
    mina "B-Flat... yes. I hear it. I can see the wave."
    
    show mina_concentration with dissolve
    
    narrator "Mina types the command. She opens her mouth and hums a tone that vibrates in your bones."
    nvl clear
    
    mina "Sending the counter-resonance... NOW."
    
    play sound "audio/massive_thrum.ogg"
    scene white with vpunch
    
    narrator "A massive, bone-shaking thrum. Xena falls to her knees. Mina screams as the energy passes through her body."
    nvl clear
    
    ai "Signal terminated. Atmosphere stabilizing. Connection severed."
    
    ai "Warning: Neural overload detected in Subject Mina. Permanent synaptic damage likely."
    
    xena "Mina?"
    
    show mina_whitehair with dissolve
    
    narrator "Mina is slumped over the console. Her hair has turned stark white from the stress. She looks older."
    nvl clear
    
    mina "It's quiet... Xena... I think I broke the bridge. We're safe. But we're stuck here. The door won't open again."
    
    xena "Stuck is better than dead."
    
    scene dark_bunker with dissolve
    
    narrator "You sit in the dark, listening to the silence. It is the most beautiful sound you have ever heard."
    nvl clear
    
    centered "{color=#00ff00}TRUE ENDING: HUMANITY SAVED{/color}"
    
    return
