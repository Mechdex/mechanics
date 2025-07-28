import yaml
import os

# --- SCRIPT INSTRUCTIONS ---
# 1. This script requires the PyYAML library. If you don't have it, run: pip install pyyaml
# 2. Replace the content of the 'yaml_data_string' variable with the YAML snippets you want to process.
# 3. Run the script. It will create the correctly formatted files in their respective category folders.

yaml_data_string = """
mechanic:
  symbol: "Cpr"
  name: "Contextual Prompts"
  category: "UI"
  long_description: |
    A Contextual Prompt is a UI element that dynamically displays a button prompt on-screen when the player is near an interactable object or in a specific state. The prompt typically shows both the available action (e.g., 'Open,' 'Talk,' 'Take') and the key or button required to perform it. It serves as the direct visual feedback for the Interact mechanic, communicating available actions to the player.
  short_description: "Dynamic on-screen prompts for available actions."
  solved_problems:
    - title: "Invisible interaction points"
      description: |
        It's a design challenge to clearly communicate which of the thousands of objects in a game world are interactable without cluttering the screen with constant icons. Contextual prompts solve this by only appearing when the player is in range of an object. This keeps the world clean while providing clear, just-in-time affordances for interaction.
  examples:
    - title: "The Legend of Zelda: Breath of the Wild"
      description: |
        The game uses simple, clean text prompts that appear over objects and NPCs. This minimalist system ensures the player always knows what they can interact with without ever distracting from the game's painterly art style.
    - title: "Red Dead Redemption 2"
      description: |
        Features a complex system of contextual prompts in the bottom-right corner of the screen. The available actions and the resulting dialogue change dynamically based on who the player is targeting and their current situation, allowing for nuanced interactions.
  isHumanWritten: false
---
mechanic:
  symbol: "Dt"
  name: "Dynamic Tooltips"
  category: "UI"
  long_description: |
    A Dynamic Tooltip is an information-rich popup that appears when the player hovers their cursor over a UI element, such as an item in their inventory or an ability on their hotbar. These tooltips are "dynamic" because they update in real-time to reflect how an item's stats would change based on the player's current attributes, buffs, or even a comparison with their currently equipped gear.
  short_description: "Popups that show real-time statistical information."
  solved_problems:
    - title: "Complex statistical calculations"
      description: |
        It's difficult for a player in a complex RPG to know if a new piece of gear is an upgrade without manually calculating many different stats. Dynamic tooltips solve this by performing the comparison automatically. They instantly show the player the exact statistical gains or losses, allowing for quick, informed decisions without breaking game flow.
  examples:
    - title: "World of Warcraft"
      description: |
        The game's tooltips are foundational to its complex gearing system. By default, hovering over a new item brings up a tooltip comparing it side-by-side with the currently equipped item, showing precise stat changes in green or red.
    - title: "Path of Exile"
      description: |
        Features an extremely detailed tooltip system. Holding a key like 'Alt' can reveal additional layers of information, such as the possible range of random stat rolls on an item, providing expert players with all the data they need.
  isHumanWritten: false
---
mechanic:
  symbol: "Hud"
  name: "HUD"
  category: "UI"
  long_description: |
    The Heads-Up Display (HUD) is the collection of persistent, on-screen user interface elements that display critical real-time game information to the player. This commonly includes a health bar, ammo count, a minimap, and current objectives. It is a non-diegetic overlay designed to give the player constant access to vital information without needing to pause the game or open a menu.
  short_description: "The persistent on-screen display of vital game info."
  solved_problems:
    - title: "Hidden critical information"
      description: |
        It's a design paradox: players need constant access to critical information like their health, but pausing the game to check a menu during intense action is impossible. The HUD solves this by presenting this vital data as a persistent, non-interactive overlay. This allows the player to stay informed at a glance without ever disengaging from the core gameplay.
  examples:
    - title: "Dead Space"
      description: |
        A famous example of a 'diegetic' HUD. The player's health and stasis energy are displayed as illuminated meters on the back of the character's suit itself, rather than as an overlay. This integrates the UI directly into the game world to enhance immersion.
    - title: "Metroid Prime"
      description: |
        The HUD is cleverly framed as the inside of the character's helmet. The player can see reflections of their own face during bright flashes, and raindrops realistically trickle down the visor, making the HUD a core part of the game's immersive experience.
  isHumanWritten: false
---
mechanic:
  symbol: "Mm"
  name: "Minimap"
  category: "UI"
  long_description: |
    A Minimap is a small, real-time map of the player's immediate surroundings, displayed as a persistent element of the HUD, typically in a corner of the screen. It shows the player's position and orientation, nearby points of interest, quest objectives, and sometimes the position of enemies. It provides crucial navigational and situational awareness at a glance.
  short_description: "A small, corner-of-the-screen map for navigation."
  solved_problems:
    - title: "Constant navigation interruption"
      description: |
        Forcing a player to constantly open a full-screen map to navigate a complex area breaks the flow of gameplay. The minimap solves this. It provides essential, at-a-glance navigational information directly on the gameplay screen, allowing players to orient themselves and find objectives without interrupting their movement and exploration.
  examples:
    - title: "Grand Theft Auto (series)"
      description: |
        Its circular minimap is iconic. It not only shows the road layout but also displays objective markers, police locations, and a GPS route, making it an essential tool for navigating its dense city environments.
    - title: "The Elder Scrolls V: Skyrim"
      description: |
        Instead of a map, Skyrim uses a horizontal "compass" at the top of the screen. This serves a similar purpose, pointing out nearby discovered locations and quest markers without showing the detailed topography, encouraging more organic exploration.
  isHumanWritten: false
---
mechanic:
  symbol: "Rmn"
  name: "Radial Menus"
  category: "UI"
  long_description: |
    A Radial Menu is a user interface element where options are arranged in a circle around a central point, designed for quick selection with a controller's analog stick. When the player holds a button, the menu appears, and they select an option by flicking the stick in the corresponding direction and releasing the button. It is commonly used for weapon, item, or emote selection.
  short_description: "A circular menu designed for fast analog stick selection."
  solved_problems:
    - title: "Slow inventory access during combat"
      description: |
        It's a design problem that accessing items from a traditional, list-based menu during real-time combat is slow and clunky. A radial menu solves this. It maps a large number of items or weapons to quick, directional muscle-memory gestures on an analog stick, allowing the player to select what they need in a fraction of a second.
  examples:
    - title: "The Legend of Zelda: Ocarina of Time"
      description: |
        One of the earliest examples, used for assigning items to the C buttons. It allowed players to quickly swap between a large inventory of items, which was crucial for its puzzle-solving and combat.
    - title: "Horizon Zero Dawn"
      description: |
        Uses a radial menu to allow the player to quickly craft different types of ammunition in the heat of battle. This integrates crafting directly into the combat loop without requiring the player to pause and enter a menu.
  isHumanWritten: false
---
mechanic:
  symbol: "DEc"
  name: "Dynamic Ecosystem"
  category: "World"
  long_description: |
    A Dynamic Ecosystem is a complex simulation where different forms of AI life (predators, prey, herbivores) and sometimes even flora interact with each other and the environment based on a set of systemic rules. These systems are designed to create unscripted, emergent behaviors, such as predators hunting prey, animals traveling in herds to specific water sources, or scavengers appearing at a fresh kill.
  short_description: "A simulation of interacting flora and fauna."
  solved_problems:
    - title: "Lifeless, scripted game worlds"
      description: |
        It's a design challenge to make a game's wildlife feel authentic when every animal is just a mindless, wandering prop on a pre-set path. A dynamic ecosystem solves this by creating a web of interacting AI systems. This results in emergent, unscripted events that make the world feel like a living, breathing place that exists independently of the player's actions.
  examples:
    - title: "Red Dead Redemption 2"
      description: |
        Features an incredibly detailed ecosystem. Animals have daily routines, predators hunt prey, carcasses attract scavengers, and the player's actions (like over-hunting) can have a noticeable impact on the local animal population.
    - title: "Far Cry (series)"
      description: |
        The ecosystem is a source of chaotic, emergent gameplay. It's common for the player's carefully planned stealth infiltration of an outpost to be ruined (or aided) by a wild tiger suddenly attacking the guards.
  isHumanWritten: false
---
mechanic:
  symbol: "Dnc"
  name: "Day-Night Cycle"
  category: "World"
  long_description: |
    A Day-Night Cycle is a system that simulates the passage of time in the game world, typically with a continuously moving sun and moon, changing skyboxes, and dynamic global lighting. This cycle is often tied directly to gameplay systems, with different NPCs, enemies, quests, or resource availability being tied to a specific time of day.
  short_description: "Simulates the 24-hour passage of time."
  solved_problems:
    - title: "Static environmental conditions"
      description: |
        A world permanently locked at a single time of day feels static and artificial. A day-night cycle solves this by introducing the constant, natural rhythm of time. This not only adds visual variety but allows designers to create time-dependent gameplay, such as tougher enemies at night or shops that only open in the morning, making the world feel more dynamic.
  examples:
    - title: "Minecraft"
      description: |
        The day-night cycle is a fundamental part of its survival loop. Daytime is relatively safe for building and gathering, while nighttime is dangerous as hostile monsters spawn in the darkness, forcing the player to seek or build shelter.
    - title: "The Legend of Zelda: Ocarina of Time"
      description: |
        A pioneering example in 3D games. The transition between day and night in Hyrule Field affected which enemies appeared and which events could be triggered, making time a key factor in the player's journey.
  isHumanWritten: false
---
mechanic:
  symbol: "Eh"
  name: "Environmental Hazards"
  category: "World"
  long_description: |
    Environmental Hazards are elements of the game world that can inflict damage or a negative status effect on the player through proximity or contact. This can include natural hazards like pools of lava, deep water, or toxic gas vents, as well as man-made dangers like electrified floors, fields of radiation, or spinning blades.
  short_description: "Elements of the world that can harm the player."
  solved_problems:
    - title: "Uniformly safe traversal"
      description: |
        If the entire game world is safe to walk on, traversal becomes a simple act of holding forward with no engagement. Environmental hazards solve this. They turn the environment itself into an antagonist, forcing the player to be mindful of their surroundings and creating traversal puzzles where the path itself is a source of challenge.
  examples:
    - title: "Half-Life (series)"
      description: |
        The series is famous for its environmental hazards. Players must navigate rooms filled with radioactive waste, avoid electrified water, and use physics puzzles to bypass barnacle-infested ceilings.
    - title: "Super Mario Bros. (series)"
      description: |
        Bottomless pits and lava pools are the most iconic environmental hazards in gaming. They are a fundamental part of the platforming challenge, requiring precise jumps to avoid instant death.
  isHumanWritten: false
---
mechanic:
  symbol: "Owm"
  name: "Open World Map"
  category: "World"
  long_description: |
    An Open World Map is the user interface screen that displays the player's position within a large, non-linear game world. It serves as the primary tool for navigation, allowing players to set custom waypoints, view discovered points of interest, and often track the locations of quests and other activities spread across the expansive game space.
  short_description: "The primary navigational UI for a large game world."
  solved_problems:
    - title: "Player disorientation in large worlds"
      description: |
        It's a design challenge to allow players to freely explore a massive world without them getting hopelessly lost. The open world map is the fundamental solution. It provides the essential cartographic tool that gives players the confidence to explore, allowing them to orient themselves, plan long journeys, and track their progress.
  examples:
    - title: "The Elder Scrolls V: Skyrim"
      description: |
        Features a fully 3D world map that can be zoomed and panned. It provides a detailed topographical view of the world and is populated with hundreds of markers for discovered locations, making it an essential tool for exploration.
    - title: "Grand Theft Auto V"
      description: |
        Its map starts obscured by a 'fog of war' and is revealed as the player explores. It functions like a satellite GPS, showing a detailed road network and allowing the player to set waypoints for navigation.
  isHumanWritten: false
---
mechanic:
  symbol: "Ws"
  name: "Weather Systems"
  category: "World"
  long_description: |
    A Weather System is a feature that dynamically simulates changing atmospheric conditions, such as rain, snow, fog, thunderstorms, and wind. These systems can be purely for atmospheric effect, or they can have a direct and systemic impact on gameplay by affecting visibility, NPC behavior, traversal mechanics (e.g., slippery surfaces), or the effectiveness of certain elements like fire.
  short_description: "Dynamic and simulated atmospheric conditions."
  solved_problems:
    - title: "Static environmental conditions"
      description: |
        A world with permanently clear skies feels artificial and lacks dynamism. A weather system solves this by introducing atmospheric variety. This not only enhances immersion and visual interest but can also be used by designers to directly influence gameplay, such as fog reducing visibility in a stealth section or rain making surfaces slippery.
  examples:
    - title: "Red Dead Redemption 2"
      description: |
        Features a complex weather system where storm fronts can be seen rolling in from a distance. A heavy rain will turn roads to mud, while a blizzard in the mountains can cause the player's health to drain if they are not wearing warm enough clothing.
    - title: "The Legend of Zelda: Breath of the Wild"
      description: |
        Weather is a core gameplay mechanic. Rain makes cliffs slippery and impossible to climb, while thunderstorms can cause the player's metal equipment to attract deadly lightning strikes, forcing them to adapt their gear and plans.
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