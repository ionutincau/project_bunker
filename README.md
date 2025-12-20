# The Desync - Ren'Py Visual Novel

## Game Overview
**The Desync** is a psychological sci-fi horror interactive fiction game where you play as Agent Xena, the last firewall, who must choose which survivor to save in a bunker as humanity falls to a neural virus.

**Estimated Playtime:** 15 minutes  
**Genre:** Sci-Fi / Psychological Horror / Survival  
**Endings:** 6 distinct endings based on your choices

## Game Mechanics
- **Real-Time Timer:** Starts at 15:00 and counts down with each interaction
- **Hub-and-Spoke Exploration:** Choose which character to interrogate in any order
- **Hidden Variables:** Your choices affect trust levels and clue discovery
- **Multiple Endings:** Based on who you choose and what you learned

## Win Condition
To achieve the TRUE ENDING (Humanity Saved), you must:
1. Choose **Mina** in the final selection
2. Have **High Trust** with Mina (gained through empathy)
3. Have discovered the **B-Flat Frequency Clue** (from listening to Lisa)

## Game Structure

### Key Files Created
- **`game/script.rpy`** - Main game script with all story content
- **`game/screens.rpy`** - Custom HUD and UI screens
- **`game/options.rpy`** - Game configuration

### Characters
1. **Agent Xena** - The protagonist, a soldier fighting the virus while infected
2. **Kai** - North Sector Admin (The Logic Trap)
3. **Trent** - The Mechanic (Brute Force)
4. **Lisa** - The Opera Singer (Holds the frequency clue)
5. **Mina** - The Neuro-Architect (The only one who can save humanity)

### Endings
1. **The Trojan Horse** - Choose Kai (Bad Ending)
2. **Brute Force Failure** - Choose Trent (Bad Ending)
3. **A Quiet Death** - Choose Lisa (Bad Ending)
4. **The Wrong Song** - Choose Mina without the frequency clue (Tragic Failure)
5. **Fear is the Killer** - Choose Mina with low trust (Tragic Failure)
6. **HUMANITY SAVED** - Choose Mina with high trust + frequency clue (TRUE ENDING)

## Installation Instructions

### Option 1: Using Ren'Py Launcher (Recommended)
1. Download and install [Ren'Py](https://www.renpy.org/latest.html)
2. Launch the Ren'Py Launcher
3. Click "Projects" → "Add Existing Project"
4. Navigate to this directory: `D:\Projects\School\Digital Storytelling\projects\Bunker`
5. Click "Launch Project" to play

### Option 2: Quick Development
1. Open Ren'Py Launcher
2. Select the project from the projects list
3. Click "script.rpy" to edit the story
4. Click "Launch Project" to test

## Required Assets (Placeholder System)

The game uses placeholder images and sounds. To enhance the experience, add these files:

### Images (game/images/)
- `black.png` - Black screen
- `purple_sky.png` - Purple/teal sky with standing people
- `tower_pulse.png` - Transmission tower pulsing teal
- `hud_boot.png` - Tactical HUD booting up
- `airlock_red.png` - Bunker airlock with emergency red lighting
- `airlock_teal.png` - Airlock being corrupted by teal mist
- `hud_glitch.png` - Glitching HUD overlay
- `glass_fracture.png` - Cracked glass with teal mist
- `blast_doors.png` - Heavy blast doors closing
- `sanctum_sealed.png` - Interior of sealed sanctum
- Character visuals for endings

### Audio (game/audio/)
- `bass_hum.ogg` - Low, throbbing bass sound
- `glitch.ogg` - Digital glitch sound effect
- `smash.ogg` - Panel smashing sound
- `distortion.ogg` - Audio distortion
- `glass_crack.ogg` - Glass cracking
- `door_grind.ogg` - Heavy doors grinding
- `horror.ogg` - Horror sting
- `wire_rip.ogg` - Electrical wire ripping
- `lullaby.ogg` - Calm lullaby music
- `desync.ogg` - Desync effect sound
- `massive_thrum.ogg` - Deep, bone-shaking sound

### GUI (game/gui/)
- `main_menu.png` - Main menu background (dark, sci-fi themed)
- `game_menu.png` - Game menu background

## Tips for Playing
1. **Talk to everyone** - Each interrogation takes 2 minutes, manage your time wisely
2. **Listen to Lisa** - She holds the critical clue about the B-Flat frequency
3. **Be kind to Mina** - Empathy increases her trust, which is essential for the true ending
4. **Pay attention to details** - The game gives hints about who the real specialist is
5. **Timer awareness** - The turning point triggers at 07:30, final selection at 01:00

## Technical Notes
- **Rollback is disabled** to maintain timer integrity
- **Auto-save** is enabled at each choice
- The HUD displays in the top-right corner showing:
  - Time remaining
  - Neural latency (Xena's infection level)
  - Signal penetration percentage

## Customization

### Adding Your Own Images
1. Place images in `game/images/` directory
2. Use the exact filenames listed above, or
3. Edit `script.rpy` to reference your custom filenames

### Modifying the Story
Edit `game/script.rpy` to:
- Change dialogue
- Add new choices
- Modify trust values
- Adjust timer consumption

### Changing the Theme
Edit `game/options.rpy` to:
- Change color scheme (currently teal/cyan sci-fi theme)
- Adjust fonts
- Modify button styles

## Credits
Based on the screenplay "The Desync"  
Developed for Ren'Py Visual Novel Engine  
Genre: Psychological Sci-Fi Horror

## Support
For Ren'Py documentation: https://www.renpy.org/doc/html/

---

**Good luck, Agent. Save humanity... if you can.**
