# Quick Start Guide - The Desync

## Installation & Setup

### Step 1: Install Ren'Py
1. Download Ren'Py from: https://www.renpy.org/latest.html
2. Extract the downloaded file to a location on your computer
3. Run the Ren'Py Launcher executable

### Step 2: Add The Desync Project
1. Open Ren'Py Launcher
2. The launcher should automatically detect projects in nearby folders
3. If not detected:
   - Click **"preferences"**
   - Click **"Projects Directory"**
   - Add: `D:\Projects\School\Digital Storytelling\projects`
   - Click **"Back"**
4. You should now see **"Bunker"** or **"The Desync"** in the projects list

### Step 3: Launch the Game
1. Select the project from the list
2. Click **"Launch Project"** button
3. The game will start!

## Playing the Game

### Understanding the HUD
In the top-right corner, you'll see:
- **TIME LEFT:** Countdown timer (starts at 15:00)
- **LATENCY:** Xena's infection level
- **SIGNAL:** Corruption percentage

### Gameplay Tips
1. **Interrogate ALL characters** - Each conversation takes 2 minutes
2. **LISTEN TO LISA** - She has the critical frequency clue
3. **BE KIND TO MINA** - Empathy builds trust needed for the true ending
4. **CHOOSE WISELY** - Your final choice determines the ending

### Winning Strategy
To achieve the TRUE ENDING:
✓ Talk to Lisa and choose "So how do we survive the song?"
✓ Talk to Mina and choose empathy "Mina. Look at me. Breathe..."
✓ In the final selection, choose MINA

## Customization (Optional)

### Adding Visual Assets
The game currently uses colored placeholders. To add proper images:

1. **Download generated images** from the artifacts panel
2. **Rename them** according to the list in `game/images/PLACEHOLDER_INFO.txt`
3. **Copy to** `game/images/` folder
4. **Restart** the game to see the new images

### Adding Audio
1. Find or create .ogg audio files
2. Name them according to `game/audio/AUDIO_INFO.txt`
3. Place in `game/audio/` folder
4. Restart the game

Audio is optional - the game works fine without it!

### Modifying the Story
Edit `game/script.rpy` to change:
- Dialogue text
- Character responses
- Timer values
- Trust mechanics
- Endings

## Troubleshooting

### Game won't launch
- Make sure Ren'Py is properly installed
- Check that all .rpy files are in the `game/` folder
- Try clicking "Force Recompile" in the launcher

### Missing images error
- The game should work with placeholders
- Check that `game/images.rpy` exists
- If errors persist, add at least a `black.png` file to `game/images/`

### GUI issues
- The custom HUD requires `screens.rpy` to be present
- Check that font references in `options.rpy` point to valid fonts
- Default Ren'Py fonts will be used if custom ones are missing

## File Structure
```
Bunker/
├── game/
│   ├── script.rpy          # Main game script
│   ├── screens.rpy         # Custom HUD and UI
│   ├── options.rpy         # Game configuration
│   ├── images.rpy          # Image placeholders
│   ├── images/             # Image files (add here)
│   ├── audio/              # Sound files (optional)
│   ├── gui/                # GUI backgrounds
│   └── fonts/              # Custom fonts (optional)
├── README.md               # Full documentation
└── QUICKSTART.md          # This file
```

## Support & Resources
- **Ren'Py Documentation:** https://www.renpy.org/doc/html/
- **Ren'Py Discord:** Active community for help
- **Game Source:** All story content is in `script.rpy`

## Credits
Based on "The Desync" screenplay  
Built with Ren'Py Visual Novel Engine  
Genre: Psychological Sci-Fi Horror

---

**Ready to play? Launch the project and save humanity!**
