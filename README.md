# Digimon Evolution Graph - Dijkstra Algorithm

This project implements Dijkstra's algorithm to find the shortest path between Digimon evolutions based on key point requirements.

## Overview

The graph represents Digimon evolution paths where:
- Each node is a Digimon
- Each edge represents a possible evolution
- Edge cost = number of key requirements (key points) needed to evolve

## Files

- `dijkstra.py` - Main implementation with Graph class and Dijkstra algorithm
- `digimon.json` - Evolution paths parsed from evolutions.js
- `costs.json` - Key point costs parsed from costs.js
- `evolutions.js` - Original JavaScript evolution paths
- `costs.js` - Original JavaScript evolution requirements
- `parse_digimon.py` - Parses evolutions.js to digimon.json
- `parse_costs.py` - Parses costs.js to costs.json

## Usage

### Generate JSON files (if needed)

```bash
python3 parse_digimon.py
python3 parse_costs.py
```

### Run Dijkstra

```bash
python3 dijkstra.py
```

## Key Points Calculation

Each evolution requirement counts as 1 key point:
- HP, MP, Offense, Defense, Speed, Brains
- Care mistakes, Weight
- Battles, Techniques
- Happiness, Discipline

Example: If a Digimon requires HP=1000, MP=1000, and Speed=100, the cost is 3 key points.

## Example Output

```
Total Digimons: 61

Running Dijkstra from Koromon

Minimum distances from Koromon:
Koromon: 0 key points
Agumon: 4 key points
MetalGreymon: 20 key points

Shortest path from Koromon to MetalGreymon:
Koromon -> Agumon -> Meramon -> MetalGreymon
Total cost: 20 key points
```

## Data Source

Inspiritation and data from the website [https://phoenix-staffel.de/digimon/DigimonWorld/evolution.html](https://phoenix-staffel.de/digimon/DigimonWorld/evolution.html) and it original source code with the evolution paths and requirements in JavaScript files [https://github.com/SydMontague/DigimonWorldWebsite/tree/master](https://github.com/SydMontague/DigimonWorldWebsite/tree/master)