import os
import yaml
from pathlib import Path

def read_yaml_file(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def process_field(value):
    if isinstance(value, list):
        return '; '.join(str(item) for item in value)
    elif isinstance(value, str):
        return value.replace('\n', ' ').strip()
    return str(value)

def generate_mechanics_table():
    mechanics_dir = Path('.')  # Changed from Path('mechanics') to Path('.')
    mechanics_data = []
    
    # recursively find all mechanic.yaml files
    for yaml_file in mechanics_dir.rglob('mechanic.yaml'):
        try:
            data = read_yaml_file(yaml_file)
            if 'mechanic' in data:
                mechanic = data['mechanic']
                # Get the symbol (current directory name) and category (parent directory name)
                symbol = yaml_file.parent.name
                category = yaml_file.parent.parent.name
                
                mechanics_data.append({
                    'name': process_field(mechanic.get('name', '')),
                    'symbol': symbol,
                    'category': category,
                    'short_description': process_field(mechanic.get('short_description', '')),
                    'long_description': process_field(mechanic.get('long_description', '')),
                    'examples': process_field(mechanic.get('examples', [])),
                    'solved_problems': process_field(mechanic.get('solved_problems', ''))
                })
        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")
    
    # markdown table template
    markdown = "# Game Mechanics Database\n\n"
    markdown += "| Name | Symbol | Category | Short Description | Long Description | Examples | Solved Problems |\n"
    markdown += "|------|--------|----------|------------------|------------------|----------|----------------|\n"
    
    for mechanic in sorted(mechanics_data, key=lambda x: (x['category'], x['name'])):
        markdown += f"| {mechanic['name']} | {mechanic['symbol']} | {mechanic['category']} | {mechanic['short_description']} | {mechanic['long_description']} | {mechanic['examples']} | {mechanic['solved_problems']} |\n"
    
    with open('mechanics_database.md', 'w') as f:
        f.write(markdown)

if __name__ == "__main__":
    generate_mechanics_table() 