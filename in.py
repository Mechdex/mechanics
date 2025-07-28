import yaml
import os

# --- SCRIPT INSTRUCTIONS ---
# 1. This script requires the PyYAML library. If you don't have it, run: pip install pyyaml
# 2. Replace the content of the 'yaml_data_string' variable with the YAML snippets you want to process.
# 3. Run the script. It will create the correctly formatted files in their respective category folders.

yaml_data_string = """
mechanic:
  symbol: "QtE"
  name: "Quick Time Event"
  category: "Actions"
  long_description: |
    A Quick Time Event (QTE) is a scripted interaction where the player must press a prompted button, or sequence of buttons, within a short time limit. Its primary function is to maintain player engagement during a non-interactive or highly cinematic sequence, effectively bridging the gap between active gameplay and passive cutscenes.

    The design of a QTE is defined by its consequences and presentation. Failure can result in instant death, a minor penalty, or a branching narrative path. Modern implementations often favor less intrusive UI and more meaningful outcomes to avoid breaking player immersion.
  short_description: "Timed button prompts for cinematic actions."
  solved_problems:
    - title: "Non-standard character actions"
      description: |
        A game's core verbs (move, jump, attack) can't cover every unique action a cinematic story beat might demand. Your narrative may require a specific physical feat, like holding a door shut, or you may have a costly animation for a dramatic moment with no way to trigger it via the standard controls. QTEs are a simple way to connect one-off actions to the game without breaking immersion or building a massive action set.
    - title: "Breaking immersion during cutscenes"
      description: |
        To keep players engaged during long cinematics, designers need a form of light interaction. QTEs provide this by using minimal, clearly telegraphed prompts for simple actions. This keeps the player focused as an active participant without cluttering the screen with a full UI. As a bonus, it also prevents the jarring 'fumble for the controller' when the scene suddenly demands input.
  examples:
    - title: "God of War (Original Trilogy)"
      description: |
        QTEs are used as brutal, cinematic finishers for bosses and large enemies. Success results in a spectacular animation that acts as a reward for winning the fight. The system is purely about spectacle and reinforcing the power fantasy of the character.
    - title: "Heavy Rain"
      description: |
        This game uses QTEs as its core gameplay mechanic to simulate physical and emotional strain. The prompts are often intentionally awkward or require holding multiple buttons to mirror the character's physical and emotional strain. Failure doesn't lead to a 'game over,' but instead causes permanent narrative branching.
  isHumanWritten: false
---
mechanic:
  symbol: "Mc"
  name: "Modular Construction"
  category: "Building"
  long_description: |
    Modular Construction is a "snap-together" building system that uses a limited set of pre-fabricated, interlocking pieces (like floors, walls, and ramps). These pieces are designed to connect to each other seamlessly, often on a grid system, allowing for rapid and intuitive building. This method contrasts with more granular, free-form systems like voxel-based construction.
  short_description: "Flexible building with modular parts."
  solved_problems:
    - title: "High barrier to entry for building"
      description: |
        Free-form building systems can be overwhelming and often result in ugly, non-functional structures for unskilled players. A modular system solves this by using a limited set of easy-to-use, snap-together pieces. This guarantees that even novice builders can create structurally sound and aesthetically pleasing buildings quickly.
    - title: "Slow-paced building in a fast-paced game"
      description: |
        It's a design conflict to have a deep building system in a fast-paced combat game, as traditional building is too slow to be used effectively under pressure. Modular construction solves this. By using a limited set of pieces that snap together instantly, it transforms building into a rapid, reflexive combat skill, allowing for dynamic creation of cover and structures mid-fight.
  examples:
    - title: "Fortnite: Battle Royale"
      description: |
        The game's signature mechanic is its fast-paced modular construction, where players can instantly build walls, ramps, and floors in the middle of a firefight. This turns building into a core combat and traversal skill.
    - title: "No Man's Sky"
      description: |
        Base building relies on a large library of modular components that snap together, allowing players to easily construct sprawling and complex bases without needing to place every single wall panel individually.
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