import yaml
import os

# --- SCRIPT INSTRUCTIONS ---
# 1. This script requires the PyYAML library. If you don't have it, run: pip install pyyaml
# 2. Replace the content of the 'yaml_data_string' variable with the YAML snippets you want to process.
# 3. Run the script. It will create the correctly formatted files in their respective category folders.

yaml_data_string = """
mechanic:
  symbol: "Dw"
  name: "Dialogue Wheel"
  category: "Narrative"
  long_description: |
    A Dialogue Wheel is a specific user interface for presenting branching dialogue choices in a radial menu. Options are often displayed as paraphrased intentions (e.g., "Question," "Threaten," "Sarcastic") rather than the full line of dialogue. This UI is designed for quick, intuitive selection with a controller's analog stick, making it ideal for cinematic conversations where pacing is important.
  short_description: "A radial menu for selecting dialogue choices."
  solved_problems:
    - title: "Clunky dialogue navigation"
      description: |
        It's a challenge to make dialogue selection feel fluid with a controller, as traditional top-to-bottom list menus can be slow to navigate. A dialogue wheel solves this by mapping choices to the analog stick's natural, radial movement. This allows for faster, more intuitive selection, which is crucial for maintaining pacing in timed or cinematic conversations.
  examples:
    - title: "Mass Effect (series)"
      description: |
        The franchise popularized the dialogue wheel. Choices are consistently mapped (e.g., top-right for Paragon, bottom-right for Renegade), allowing players to make rapid, instinctual decisions that align with their character's established personality.
    - title: "Fallout 4"
      description: |
        Implemented a dialogue wheel where players chose a tone rather than a specific line. While controversial for its perceived lack of clarity, it demonstrated how the wheel could be used to streamline conversations into a more cinematic, action-oriented format.
  isHumanWritten: false
---
mechanic:
  symbol: "Env"
  name: "Environmental Storytelling"
  category: "Narrative"
  long_description: |
    Environmental Storytelling is a narrative technique where the history, lore, and events of the game world are communicated to the player through the level design and art direction, rather than through explicit text or dialogue. It involves telling a story through the careful placement of objects, the architecture, and the overall state of the environment (e.g., a skeleton clutching a note next to a locked door).
  short_description: "Telling a story through the world itself."
  solved_problems:
    - title: "Forced narrative exposition"
      description: |
        It's a design challenge to deliver lore and backstory without halting gameplay for a long cutscene or text dump. Environmental storytelling solves this by embedding the narrative directly into the explorable space. It respects player agency by allowing them to discover (or ignore) the story at their own pace, making lore discovery an active, immersive process.
  examples:
    - title: "BioShock"
      description: |
        The city of Rapture's story is primarily told through its environment. Propaganda posters, abandoned living quarters, and ghostly apparitions all work together to tell the story of the city's fall without relying on lengthy exposition.
    - title: "Portal"
      description: |
        Hidden behind the clean, corporate test chambers are desperate scrawlings and makeshift dens from a previous test subject. This environmental storytelling creates a haunting secondary narrative that is discovered entirely through player curiosity.
  isHumanWritten: false
---
mechanic:
  symbol: "Lrc"
  name: "Lore Collection"
  category: "Narrative"
  long_description: |
    Lore Collection is a system that scatters narrative information throughout the game world in the form of collectible items, such as books, audio logs, or item descriptions. The player is encouraged to find these fragments to piece together the history and context of the world. This content is often presented in a dedicated in-game codex or journal for later review.
  short_description: "Piece together the story via found items."
  solved_problems:
    - title: "Unmotivated exploration"
      description: |
        A large world can feel empty if the only reason to explore is to find stat-based loot. Lore collection solves this by turning narrative into a reward. It gives players a powerful, intrinsic motivation to explore every corner of the map, rewarding their curiosity with a deeper understanding of the world's history.
  examples:
    - title: "Dark Souls (series)"
      description: |
        Famously tells most of its story through the cryptic descriptions on weapons, armor, and items. The community actively pieces together this fragmented lore to form a cohesive narrative, making discovery a collective effort.
    - title: "Control"
      description: |
        The game world is filled with heavily-redacted official documents, research notes, and eerie training videos. Collecting these files is essential to understanding the game's complex and bizarre supernatural universe.
  isHumanWritten: false
---
mechanic:
  symbol: "Nls"
  name: "Non-linear Story"
  category: "Narrative"
  long_description: |
    A Non-linear Story is a narrative structure where major plot points, quests, and story arcs can be completed in an order chosen by the player. Unlike a linear story that follows a fixed A->B->C sequence, a non-linear narrative presents multiple paths that can be pursued in parallel. These paths can converge or influence each other, and player choices can lead to significantly different outcomes.
  short_description: "A story that can be experienced in a flexible order."
  solved_problems:
    - title: "Low replay value"
      description: |
        A strictly linear game offers the exact same experience on every playthrough, which limits its replayability. A non-linear story solves this by creating a branching structure. It encourages multiple playthroughs as players want to see how different choices and quest orders will affect the overall narrative and world state.
  examples:
    - title: "The Witcher 3: Wild Hunt"
      description: |
        While there is a main quest line, the player is free to pursue massive, multi-part side stories in any order they wish. The outcomes of these quests can then have significant and often surprising impacts on the main narrative and its ending.
    - title: "Fallout: New Vegas"
      description: |
        A classic example where the player is presented with multiple competing factions. The player's choice of which faction to support (or betray) creates radically different narrative paths and endings, offering high replayability.
  isHumanWritten: false
---
mechanic:
  symbol: "De"
  name: "Destructible Environments"
  category: "Physics"
  long_description: |
    Destructible Environments are a physics-based system that allows game world geometry, such as walls, cover, and entire buildings, to be dynamically damaged and destroyed by player or AI actions. This creates a battlefield that is not static, but is constantly changing and reacting to the forces of combat. Implementations can range from simple, pre-scripted destruction to fully dynamic, physics-based demolition.
  short_description: "Game world geometry can be damaged and destroyed."
  solved_problems:
    - title: "Static, predictable battlefields"
      description: |
        In most games, the level geometry is static and indestructible, leading to predictable combat encounters where cover is permanent. Destructible environments solve this by making the battlefield dynamic. Cover can be blown away, new sightlines can be created, and entire strategies are invalidated when a building collapses, forcing players to constantly adapt.
  examples:
    - title: "Red Faction: Guerrilla"
      description: |
        The game's 'Geo-Mod' engine made every single structure fully destructible. This was not just a visual effect but the core mechanic, as players would strategically demolish buildings to complete objectives or eliminate enemies.
    - title: "Battlefield (series)"
      description: |
        Known for its 'Levolution' system, which features large-scale environmental destruction. Players can do everything from blowing holes in walls to toppling entire skyscrapers, fundamentally altering the map's layout mid-match.
  isHumanWritten: false
---
mechanic:
  symbol: "Fd"
  name: "Fluid Dynamics"
  category: "Physics"
  long_description: |
    Fluid Dynamics is a complex physics simulation that models the properties of liquids, such as viscosity, flow, and buoyancy. This allows water and other fluids in the game to react realistically to forces like explosions, moving objects, and player interaction. This goes beyond simple, static water planes and simulates a fluid's volume and movement.
  short_description: "Realistic simulation of liquid movement and interaction."
  solved_problems:
    - title: "Unrealistic environmental interactions"
      description: |
        It's a design challenge to make game worlds feel truly interactive and reactive. A fluid dynamics simulation solves a piece of this by making water a dynamic element rather than a static prop. This creates a more believable and immersive world where liquids react to the player's actions in a physically plausible way.
  examples:
    - title: "BioShock"
      description: |
        Water is a constant environmental presence in the underwater city of Rapture. When glass breaks, water realistically floods the corridors, pushing objects and affecting the player's movement.
    - title: "The Legend of Zelda: Tears of the Kingdom"
      description: |
        Features a detailed fluid dynamics model that is core to many of its puzzles. Water flows downhill, can be redirected, and interacts with player-built contraptions, making it a key puzzle-solving tool.
  isHumanWritten: false
---
mechanic:
  symbol: "Gm"
  name: "Gravity Manipulation"
  category: "Physics"
  long_description: |
    Gravity Manipulation is a mechanic that gives the player a tool to directly alter the gravitational properties of objects or the environment. This can include making objects weightless, increasing their mass to create a powerful impact, reversing the direction of gravity in a room, or creating localized gravity wells.
  short_description: "Alter gravitational forces to affect gameplay."
  solved_problems:
    - title: "One-dimensional puzzle solving"
      description: |
        Many puzzles are limited to finding keys or pushing blocks. Gravity manipulation solves this by introducing physics as the core puzzle component. It allows designers to create complex challenges based on mass, trajectory, and momentum, opening up an entirely new dimension of puzzle design.
  examples:
    - title: "Half-Life 2"
      description: |
        The Gravity Gun allows players to pick up, move, and launch objects. This turns the environment into both a physics-based puzzle sandbox and a weapon, as players can grab saw blades and launch them at enemies.
    - title: "Portal 2"
      description: |
        The 'Excursion Funnels' are beams of energy that defy gravity, allowing the player and objects to float in a specific direction. Puzzles are often based on redirecting these funnels with portals to manipulate the trajectory of objects.
  isHumanWritten: false
---
mechanic:
  symbol: "Rlc"
  name: "Realistic Collision"
  category: "Physics"
  long_description: |
    Realistic Collision is a physics system that accurately simulates the transfer of forces and the resulting deformation and damage when two or more objects collide. This goes beyond simple "bounding box" collisions, where objects just bounce off each other. Instead, it models how materials bend, shatter, and break apart in a physically plausible manner, often using a "soft-body" physics engine.
  short_description: "Accurate simulation of physical impact and deformation."
  solved_problems:
    - title: "Superficial impact feedback"
      description: |
        It's a design challenge to make high-impact events, like a car crash, feel visceral and consequential. Simple collision systems often result in objects just bouncing off each other. A realistic collision model solves this by providing detailed, dynamic feedback, making every impact feel unique and unscripted.
  examples:
    - title: "BeamNG.drive"
      description: |
        The entire game is built around its revolutionary soft-body physics engine. The primary appeal is the incredibly realistic and detailed way vehicles deform and fall apart during collisions.
    - title: "Crysis (series)"
      description: |
        Known for its detailed physics, where individual palm trees can be shot down and flimsy shacks will realistically splinter and collapse when hit with explosive force.
  isHumanWritten: false
---
mechanic:
  symbol: "Rp"
  name: "Ragdoll Physics"
  category: "Physics"
  long_description: |
    Ragdoll Physics is a procedural animation system that takes over a character's model upon death, incapacitation, or major impact. Instead of playing a pre-canned, static animation, the character's body becomes a collection of rigid bodies connected by joints. This "ragdoll" then reacts realistically to the forces applied to it, causing it to tumble down stairs, slump over ledges, or be thrown by an explosion in a unique, unscripted way every time.
  short_description: "Physics-based procedural animation for bodies."
  solved_problems:
    - title: "Repetitive death animations"
      description: |
        Watching the same few pre-scripted death animations over and over is immersion-breaking and repetitive. Ragdoll physics solves this. It creates unique, dynamic, and often comedic death sequences every single time, making these moments feel more visceral and less predictable.
  examples:
    - title: "Grand Theft Auto IV"
      description: |
        Famous for its implementation of the Euphoria physics engine, which created advanced, dynamic ragdoll effects. Characters would realistically stumble, brace for impact, and react to being hit in ways that felt far more believable than in previous titles.
    - title: "Goat Simulator"
      description: |
        This game takes ragdoll physics to its comedic extreme. The entire humor of the game is based on the wacky, unpredictable, and often glitchy behavior of the goat's ragdoll as it crashes into the game world.
  isHumanWritten: false
---
mechanic:
  symbol: "Lu"
  name: "Leveling Up"
  category: "Progression"
  long_description: |
    Leveling Up is a core RPG progression system where a player character earns Experience Points (XP) for completing tasks. Upon reaching a certain XP threshold, the character's "Level" increases. This typically grants an automatic increase in base statistics (like health and damage) and often awards points to spend in other systems, like Skill Trees or perks.
  short_description: "Gain levels by earning experience points to grow stronger."
  solved_problems:
    - title: "Lack of measurable progress"
      description: |
        It can be difficult for players to feel a tangible sense of growth over a long game. A leveling system solves this by providing a clear, quantifiable measure of progress. The constant feedback of gaining XP and leveling up creates a powerful and addictive psychological loop that keeps players invested.
  examples:
    - title: "World of Warcraft"
      description: |
        The quintessential example of a level-based MMO. The entire game structure, from quests to zones to gear, is built around the player's journey from level 1 to the level cap.
    - title: "Pokémon (series)"
      description: |
        Each Pokémon levels up individually by participating in battles. Leveling up not only increases their stats but is also the primary way they learn new moves and evolve into more powerful forms.
  isHumanWritten: false
---
mechanic:
  symbol: "Ps"
  name: "Perk System"
  category: "Progression"
  long_description: |
    A Perk System is a progression system where players can unlock specific, named abilities or passive bonuses ("perks") that provide unique gameplay advantages. Unlike simple stat increases from leveling up, perks often grant new capabilities (e.g., "pick any lock") or significantly alter existing ones (e.g., "pistols now fire in a burst"). They are the primary tool for creating distinct character builds.
  short_description: "Unlock unique abilities and bonuses to specialize a build."
  solved_problems:
    - title: "Homogenous character builds"
      description: |
        If progression is just about increasing base stats, every high-level character ends up feeling the same. A perk system solves this by introducing meaningful, strategic choices. It allows players to specialize in a specific playstyle (e.g., stealth, heavy weapons, speech), creating significant build diversity and replayability.
  examples:
    - title: "Fallout (series)"
      description: |
        The series is famous for its perk system, which includes a mix of statistical bonuses and unique, often humorous abilities like "Bloody Mess" (enemies explode in a gory mess) or "Mysterious Stranger" (a character who randomly appears to help in combat).
    - title: "Dead by Daylight"
      description: |
        Perks are the core of the game's loadout system for both survivors and killers. A player's choice of four perks completely defines their strategy and abilities in a match, creating a deep meta-game of perk combinations and counters.
  isHumanWritten: false
---
mechanic:
  symbol: "St"
  name: "Skill Trees"
  category: "Progression"
  long_description: |
    A Skill Tree is a visual representation of a character's progression path, where skills and abilities are laid out in a branching, tree-like structure. Players spend points (often earned by leveling up) to unlock nodes on the tree. More powerful abilities are typically located further down a branch, requiring investment in prerequisite, lower-tier skills to reach them.
  short_description: "A visual, branching path for unlocking new abilities."
  solved_problems:
    - title: "Unclear progression paths"
      description: |
        A long, unstructured list of unlockable abilities can be overwhelming and doesn't communicate long-term goals. A skill tree solves this by visualizing the entire progression path. It allows players to plan their build in advance and make informed decisions about their character's development, providing a clear roadmap for their progression.
  examples:
    - title: "Diablo II"
      description: |
        Its skill tree system became the genre-defining standard. Each class had three distinct trees, and players had to make permanent, meaningful choices about which tree to specialize in, creating strong character identity.
    - title: "Borderlands (series)"
      description: |
        Each Vault Hunter has multiple skill trees that focus on different playstyles. The final skill in each tree is a powerful "capstone" ability that dramatically changes gameplay, heavily incentivizing specialization.
  isHumanWritten: false
---
mechanic:
  symbol: "Ul"
  name: "Unlockables"
  category: "Progression"
  long_description: |
    Unlockables are a system of rewards (such as characters, weapons, cosmetic skins, or game modes) that are initially unavailable to the player. They must be made accessible by completing specific in-game challenges, reaching progression milestones, or spending a specific in-game currency.
  short_description: "Rewards made available by completing in-game goals."
  solved_problems:
    - title: "Lack of player motivation"
      description: |
        It's a design challenge to keep players engaged after they've mastered the core gameplay. Unlockables solve this by providing a clear set of extrinsic goals. The desire to unlock a new character or a cool weapon skin provides a powerful motivation for players to continue playing and engage with different aspects of the game.
  examples:
    - title: "Super Smash Bros. (series)"
      description: |
        A large portion of the roster is locked at the start of the game. Players must complete various challenges or play a certain number of matches to unlock these iconic characters, which is a primary driver of single-player engagement.
    - title: "Call of Duty (series)"
      description: |
        The multiplayer progression is built almost entirely around unlockables. Players earn new weapons, attachments, perks, and cosmetic camos by leveling up and completing specific in-game challenges.
  isHumanWritten: false
---
mechanic:
  symbol: "Xp"
  name: "Experience Points"
  category: "Progression"
  long_description: |
    Experience Points (XP or EXP) are a numerical value awarded to players for completing in-game actions, such as winning battles, finishing quests, or discovering new locations. XP is the fundamental "currency" for the Leveling Up system; accumulating a specific amount of XP is what causes a character to gain a level and become more powerful.
  short_description: "Points earned for in-game actions that fuel leveling."
  solved_problems:
    - title: "Unrewarded player actions"
      description: |
        Players can feel like their time is being wasted if minor actions, like defeating a weak enemy, have no tangible reward. An experience point system solves this. By assigning an XP value to nearly every positive action, it ensures that the player is always making measurable progress towards their next level, no matter how small the task.
  examples:
    - title: "Final Fantasy (series)"
      description: |
        The classic implementation where each defeated enemy grants a set amount of XP, which is divided among the party members. Grinding battles to accumulate XP is a core gameplay loop of the series.
    - title: "The Elder Scrolls V: Skyrim"
      description: |
        Features a skill-based experience system. Instead of getting XP for quests, the player gains XP in a specific skill (e.g., 'One-Handed' or 'Smithing') by using it. Gaining skill levels is what contributes to the overall character level.
  isHumanWritten: false
---
mechanic:
  symbol: "Ch"
  name: "Critical Hits"
  category: "Randomness"
  long_description: |
    A Critical Hit, or "crit," is a combat mechanic where, based on a random chance (a "crit rate" percentage), an attack will deal a significantly increased amount of damage. The damage multiplier (e.g., 200%) and the chance to trigger a crit are often key stats that can be improved by a character's attributes or gear.
  short_description: "A chance-based attack that deals bonus damage."
  solved_problems:
    - title: "Predictable combat outcomes"
      description: |
        If every attack deals a fixed amount of damage, combat can become a purely mathematical and predictable exercise. Critical hits solve this by introducing an element of random chance. The possibility of a sudden burst of damage adds a layer of excitement and unpredictability to every encounter, creating memorable high-roll moments.
  examples:
    - title: "Diablo (series)"
      description: |
        Critical Hit Chance and Critical Hit Damage are two of the most important stats for increasing a character's damage output. The entire end-game gearing process revolves around maximizing these stats to create massive, screen-clearing bursts of damage.
    - title: "XCOM: Enemy Unknown"
      description: |
        Critical hits are a core part of the game's brutal probability-based combat. A well-timed critical hit can save a mission, while an enemy landing a lucky crit on a key soldier can be devastating, creating high-stakes tension.
  isHumanWritten: false"""

def process_mechanics_direct_write(data_string):
    """
    Splits a string containing multiple YAML documents and writes each one directly
    to a file, preserving the original formatting perfectly.
    """
    print("Starting direct write processing...")
    # 1. Split the master string into individual YAML document strings
    mechanic_strings = data_string.strip().split('---')
    
    count = 0
    for doc_string in mechanic_strings:
        # Skip any empty strings that might result from the split
        if not doc_string.strip():
            continue

        try:
            # 2. Parse the string temporarily just to get metadata for the filename
            doc = yaml.safe_load(doc_string)
            
            if doc and 'mechanic' in doc:
                mechanic_data = doc['mechanic']
                category = mechanic_data.get('category', 'Uncategorized')
                symbol = mechanic_data.get('symbol', 'NoSymbol')

                # Construct the path
                dir_path = os.path.join(category, symbol)
                os.makedirs(dir_path, exist_ok=True)
                file_path = os.path.join(dir_path, 'mechanic.yaml')

                # 3. Write the original, untouched string directly to the file
                with open(file_path, 'w') as f:
                    # We use strip() to remove any leading/trailing whitespace from the split
                    f.write(doc_string.strip())

                print(f"Successfully wrote: {file_path}")
                count += 1
        except yaml.YAMLError as e:
            # This helps debug if one of the snippets has a syntax error
            print(f"---Skipping a snippet due to a YAML parsing error: {e}")
            continue

    print(f"\nProcessing complete. Total mechanics written: {count}")


if __name__ == "__main__":
    if "PASTE THE ENTIRE, CORRECTLY FORMATTED YAML SNIPPET BLOCK HERE" in yaml_data_string:
        print("Please replace the placeholder content in the 'yaml_data_string' variable before running.")
    else:
        process_mechanics_direct_write(yaml_data_string)