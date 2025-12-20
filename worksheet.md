Interactive Fiction Game Concept Worksheet

Step 1: General Game Concept
A. Game Title: The Desync (Working title indicating the central conflict: the neurological dissociation of humanity.)
B. Genre: Sci-Fi / Psychological Horror / Survival (A blend of high-stakes time management, futuristic tech, and atmospheric horror.)
C. Game Mechanics:
Real-Time Timer: A countdown clock (time_left) starts at 15:00. Every interaction consumes time. If the timer hits 01:00, the game forces the final choice.
Hub-and-Spoke Exploration: The player is in a central hub and chooses which character to interrogate.
Hidden Variables (Flags):
mina_trust: Determines if the specialist is mentally stable enough to perform the final task.
frequency_clue: A boolean (True/False) check required to solve the final puzzle.
hardware_clue: A boolean check regarding the physical door mechanism.
* Boolean: A variable that has only two possible states: True or False.
Dialogue Choices: Choices affect the variables above and the player's understanding of the lore.
Point of No Return: A forced "Turning Point" event at 07:30 and a "Final Selection" event at 01:00.
D. Setting:
Location: A futuristic, fortified bunker ("The Last Hardline Junction") overlooking a ruined coastline.
Atmosphere: Oppressive, glitchy, and claustrophobic. The visuals shift from "Emergency Red" to "Sickly Teal" as the corruption spreads.
Context: A post-apocalyptic event caused by a neural patch called "The Bridge." Outside, people are frozen statues ("The Standing People") while their minds are trapped in a digital hive mind.
E. Plot Overview:
Core Conflict: Agent Xena, the last firewall, must seal the bunker to stop a signal from jumping a repeater and infecting the rest of the world. She is infected with the virus ("The Desync") and losing cognitive function.
Antagonistic Force: "The Desync" (a resonance cascade/hive mind) and the encroaching time limit.
Progression: Xena wakes up, meets four survivors, and must determine which one is the "Neuro-Architect" capable of stopping the signal. She interrogates them, gathering clues while fighting her own mental deterioration. In the end, she must choose one person to save the world, leaving the others to die.

Step 2: Game Structure
1. Game Structure Type: Hub-and-Spoke with Bottleneck Endings. The middle section (The Interrogations) allows non-linear exploration; the player can talk to characters in any order. However, the game forces all players through specific "Bottleneck" events (The Turning Point and The Breach) before branching into distinct endings based on accumulated variables.
2. Exposition: The game opens with a Narrator describing the fall of humanity caused by "The Bridge." We see Xena’s Tactical HUD booting up, displaying the 15:00 timer and her Neural Latency. Xena’s internal monologue establishes the stakes: she is infected ("The parasite is warm") and must find the "Specialist" before she succumbs. The Bunker AI confirms that only ONE other person can be saved.
3. Main Turning Points:
Turning Point 1: The Hub Entry (02:30) Xena opens the blast doors and meets the four survivors (Trent, Kai, Mina, Lisa). The realization hits that she cannot save them all; she must choose only one. This shifts the game from a rescue mission to a selection process.
Turning Point 2: The Panel Smash (07:30) Triggered automatically by the timer. Trent attempts to smash the control panel. The player must choose to Let him smash it (gaining manual access but losing time) or Stop him (preserving hardware but risking a lockout). This raises the tension and forces a high-stakes decision.
Turning Point 3: The Deterioration & Breach (11:30) The AI voice glitches and starts speaking seductively ("It's warm in here"). The outer glass shatters, flooding the survivors' room with "teal mist" (data). Xena’s HUD begins to fail. This is the climax of the horror element before the final choice.

Step 3: Characters and Protagonist
Protagonist:
Agent Xena: A disciplined soldier and the "Last Firewall." She is professional and cold but driven by a promise to save humanity. She is an unreliable narrator because she is actively succumbing to the virus during gameplay (glitching text, intrusive thoughts).
Supporting Characters (The Candidates):
Kai (The Red Herring): North Sector Admin. Bureaucratic, rigid, and logical. He believes the threat is a software bug. He is persuasive but incorrect.
Trent (The Mechanic): Aggressive and practical. He represents brute force and physical reality. He knows how the doors work mechanically.
Lisa (The Lore/Clue): An opera singer. Calm and eerie. She understands the "Desync" is a sound/frequency, not a code. She holds the key clue (B-Flat).
Mina (The Specialist): The Neuro-Architect who built the system. She is young, traumatized, and bleeding from the nose. She is the only one who can save the world, but only if Xena keeps her calm.

Step 4: Choice-based Storytelling Elements
Logic of the Game: The game is a puzzle of Deduction and Emotional Management.
Logic: You must find the Frequency (B-Flat) by listening to Lisa.
Emotion: You must stabilize Mina (mina_trust) so she can execute the command.
If you focus only on Logic (Kai) or Force (Trent), you fail.

Key Branching Points:
Choice A: Investigating Kai (Logic Trap)
Context: Kai claims his sector survived longer because he followed protocol, not emotion.
Choices:
Challenge him: "Your code failed." -> Outcome: You realize he is rigid and wrong (Deduction Up).
Trust him: "We need stability." -> Outcome: You are misled into thinking he is the solution (False Trust).
Choice B: Investigating Lisa (The Critical Clue)
Context: Lisa claims the AI is singing in "B-Flat" and needs a counter-note.
Choices:
Listen: "How do we survive the song?" -> Outcome: frequency_clue = True. (Essential for winning).
Dismiss: "No time for poetry." -> Outcome: frequency_clue = False. (You will likely fail the ending).
Choice C: Investigating Mina (The Trust Mechanic)
Context: Mina is having a mental breakdown.
Choices:
Empathy: "Breathe. You built this." -> Outcome: mina_trust increases. She stabilizes.
Force: "Give me the code!" -> Outcome: mina_trust decreases. She enters shock (Locking out the good ending).

Step 5: Endings
The game has 4 distinct endings determined by who you choose in the final selection (time_left = 01:00) and the state of your variables.
Ending 1: The Trojan Horse (Bad Ending)
Condition: Player chooses Kai.
Outcome: Kai tries to upload a firewall. It fails because the threat isn't software. He gets possessed instantly, his eyes turn teal, and he thanks Xena for letting the hive mind inside. Xena is assimilated.
Ending 2: Brute Force Failure (Bad Ending)
Condition: Player chooses Trent.
Outcome: Trent cuts the power to stop the signal. This inadvertently kills the magnetic shields. The Desync floods the room instantly. Both turn into statues.
Ending 3: A Quiet Death (Bad Ending)
Condition: Player chooses Lisa.
Outcome: Lisa knows she can't stop it. She sings a lullaby to Xena as they both peacefully succumb to the virus.
Ending 4: The Wrong Song (Tragic Failure)
Condition: Player chooses Mina, but missed the Clue (frequency_clue = False).
Outcome: Mina is ready but doesn't know the counter-note. She guesses wrong. The system fails. Humanity dies.
Ending 5: Fear is the Killer (Tragic Failure)
Condition: Player chooses Mina, but treated her poorly (mina_trust is Low).
Outcome: Mina is too terrified to type. She collapses and desyncs before she can save the world.
Ending 6: Humanity Saved (True Ending)
Condition: Player chooses Mina + High Trust + Frequency Clue.
Outcome: Xena tells Mina the note is "B-Flat." Mina inverts the frequency. A massive blast clears the signal.
The Cost: Mina survives but her hair turns white from the trauma. The bunker is permanently sealed. They are stuck in the dark, but the world is saved.
