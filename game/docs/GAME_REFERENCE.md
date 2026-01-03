# The Desync - Design Reference

## Quick Stats
- **Playtime:** 15 minutes
- **Endings:** 6 total (1 true, 5 bad/tragic)
- **Characters:** 4 survivors + Xena + AI
- **Mechanics:** Timer, Trust, Clues

## Timer Flow
```
15:00 → Start (Awakening)
12:30 → Hub Entry (Meet survivors)
10:30 → After first interrogation (-2:00)
08:30 → After second interrogation (-2:00)
07:30 → TURNING POINT (Panel smash choice)
    06:30 → If panel smashed (-1:00 penalty)
    07:30 → If panel protected
11:30 → Deterioration (Glass breaks, mist enters)
01:00 → FINAL SELECTION (Choose survivor)
00:00 → Ending plays out
```

## Characters & Functions

| Character | Role | Key Info | Ending Type |
|-----------|------|----------|-------------|
| **Kai** | Admin | Has clearance codes, bureaucratic, sees Desync as bug | BAD (Trojan Horse) |
| **Trent** | Mechanic | Physical, knows door mechanics, aggressive | BAD (Brute Force) |
| **Lisa** | Singer | Calm, understands frequency, has B-Flat clue | BAD (Quiet Death) |
| **Mina** | Architect | Built The Bridge, traumatized, bleeding nose | TRUE (If conditions met) |

## Critical Variables

| Variable | Type | Purpose | How to Get |
|----------|------|---------|------------|
| `time_left` | Integer | Countdown timer (900→0 seconds) | Auto-decrements |
| `mina_trust` | Integer | Mina's mental stability | Choose empathy (+2) vs force (-2) |
| `frequency_clue` | Boolean | B-Flat frequency knowledge | Listen to Lisa's advice |
| `hardware_clue` | Boolean | Manual door override info | Ask Trent about locks |
| `panel_smashed` | Boolean | Manual access exposed | Let Trent smash panel |

## Dialogue Choices & Outcomes

### Kai Interrogation
- **Challenge:** "Your code failed" → kai_trust -1 (See through him)
- **Trust:** "We need stability" → kai_trust +2 (Get misled)

### Trent Interrogation  
- **Investigate:** "What mechanical lock?" → hardware_clue = True, trent_trust +2
- **Dismiss:** "Back off" → trent_trust -1

### Lisa Interrogation
- **Listen:** "How survive the song?" → **frequency_clue = True** ✓ (CRITICAL!)
- **Dismiss:** "No time for poetry" → frequency_clue = False ✗

### Mina Interrogation
- **Empathy:** "Breathe. You built this." → **mina_trust +2** ✓ (CRITICAL!)
- **Force:** "Give me the code!" → mina_trust -2 ✗

## Turning Point (07:30)
**Trent wants to smash the control panel**

- **Let him smash:** hardware_clue = True, time_left -60 (manual access gained)
- **Stop him:** Panel protected, 100% reliant on Mina

## Final Selection (01:00)

| Choice | Requirements | Outcome |
|--------|-------------|---------|
| Choose Kai | None | **Trojan Horse** - He's possessed, brings virus in |
| Choose Trent | None | **Brute Force Failure** - Cuts power, kills shields |
| Choose Lisa | None | **Quiet Death** - Can't save anyone, peaceful end |
| Choose Mina | mina_trust < 1 | **Fear is Killer** - Too scared to type |
| Choose Mina | No frequency_clue | **Wrong Song** - Guesses wrong frequency |
| Choose Mina | mina_trust ≥ 1 + frequency_clue | **HUMANITY SAVED** ✓ |

## True Ending Path

```
START
  ↓
Talk to ALL characters (manage 15-minute timer)
  ↓
MUST: Talk to Lisa → Choose "How do we survive the song?"
      → frequency_clue = True
  ↓
MUST: Talk to Mina → Choose "Breathe. You built this."
      → mina_trust +2
  ↓
OPTIONAL: Talk to Trent → Ask about mechanical lock
          → hardware_clue = True (backup plan)
  ↓
Turning Point (07:30) → Either choice works
  ↓
Final Selection (01:00) → Choose MINA
  ↓
Checks: mina_trust ≥ 1? ✓  frequency_clue = True? ✓
  ↓
TRUE ENDING: Humanity Saved
  - Xena tells Mina the frequency is B-Flat
  - Mina inverts the frequency
  - Signal terminated, world saved
  - Mina's hair turns white (trauma)
  - They're stuck in bunker forever
  - But humanity survives
```

## Color Scheme (Sci-Fi Horror)

- **Teal/Cyan (#00ffff)** - Corruption, AI, the Desync
- **Red (#ff0000)** - Emergency, warnings, timer
- **Purple (#4a2866)** - Sky, the Bridge, otherworldly
- **Black/Dark Gray** - Bunker, isolation, fear
- **White** - Xena's text, clarity, resistance

## Atmosphere Notes

- **Emergency Red** → Normal bunker lighting (danger)
- **Sickly Teal** → Corruption spreading (horror)
- **Glitching Text** → Xena's infection worsening
- **Hum/Bass** → The Desync signal (constant threat)

## Quick Player Advice

**DO:**
- ✓ Talk to everyone
- ✓ Listen to Lisa (B-Flat clue is ESSENTIAL)
- ✓ Be kind to Mina (trust is ESSENTIAL)
- ✓ Choose Mina in the end

**DON'T:**
- ✗ Rush without talking to Lisa
- ✗ Yell at Mina (breaks trust)
- ✗ Choose Kai/Trent/Lisa in final selection

## The Puzzle Logic

**The Desync is NOT:**
- A software bug (Kai's wrong)
- A power problem (Trent's wrong)
- Something Lisa can sing away (Lisa's wrong)

**The Desync IS:**
- A frequency/resonance cascade
- Requires counter-frequency (B-Flat)
- Only Mina can execute the solution
- But she needs: Knowledge (clue) + Stability (trust)

---

**Remember:** This is a deduction + empathy puzzle.  
Logic alone fails. Force alone fails. Only compassion + knowledge wins.
