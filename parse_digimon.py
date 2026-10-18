import re
import json

with open('evolutions.js', 'r') as f:
    content = f.read()

evolution_paths = {}

pattern = r'EvolutionPaths\["([^"]+)"\] = new EvolutionPath\((.*?)\);'
matches = re.findall(pattern, content, re.DOTALL)

for digimon_name, evolution_list_str in matches:
    array_match = re.search(r'\[(.*?)\]', evolution_list_str, re.DOTALL)
    if array_match:
        array_content = array_match.group(1)
        if array_content.strip():
            evolutions = [e.strip().strip('"').strip("'") for e in array_content.split(',')]
        else:
            evolutions = []
        evolution_paths[digimon_name] = evolutions

with open('digimon.json', 'w') as f:
    json.dump(evolution_paths, f, indent=2)

print(f"Successfully parsed {len(evolution_paths)} Digimon and their evolution paths to digimon.json")
