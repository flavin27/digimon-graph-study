import re
import json


with open('costs.js', 'r') as f:
    lines = f.readlines()

code_lines = [line for line in lines if not line.strip().startswith('//')]
content = ''.join(code_lines)

pattern = r'Digimons\["([^"]+)"\].*new EvolutionRequirements\(([^)]+)\)'
matches = re.findall(pattern, content)

costs = {}

for digimon, req_str in matches:
    params = [p.strip() for p in req_str.split(',')]

    try:
        hp = int(params[0]) if params[0] != '0' else 0
        mp = int(params[1]) if params[1] != '0' else 0
        offense = int(params[2]) if params[2] != '0' else 0
        defense = int(params[3]) if params[3] != '0' else 0
        speed = int(params[4]) if params[4] != '0' else 0
        brains = int(params[5]) if params[5] != '0' else 0
        care = int(params[6]) if params[6] != '0' else 0
        weight = int(params[7]) if params[7] != '0' else 0
        battles = int(params[8]) if params[8] != '-1' and params[8] != '0' else 0
        techs = int(params[9]) if params[9] != '0' else 0
        happiness = int(params[10]) if params[10] != '0' else 0
        discipline = int(params[11]) if params[11] != '0' else 0

        key_points = sum([
            1 if hp > 0 else 0,
            1 if mp > 0 else 0,
            1 if offense > 0 else 0,
            1 if defense > 0 else 0,
            1 if speed > 0 else 0,
            1 if brains > 0 else 0,
            1 if care > 0 else 0,
            1 if weight > 0 else 0,
            1 if battles > 0 else 0,
            1 if techs > 0 else 0,
            1 if happiness > 0 else 0,
            1 if discipline > 0 else 0
        ])

        costs[digimon] = key_points

    except (ValueError, IndexError) as e:
        print(f"Error processing {digimon}: {e}")
        costs[digimon] = 0

with open('costs.json', 'w') as f:
    json.dump(costs, f, indent=2)

print(f"Costs generated successfully!")
print(f"Total digimons processed: {len(costs)}")
