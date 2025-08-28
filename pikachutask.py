from itertools import combinations

pokedex = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire', 'Flying'),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

def strongest_squads(pokedex, k):
    best_count = -1
    best = []

    for team in combinations(pokedex.keys(), k):
        types = set()
        for name in team:
            types.update(pokedex[name])

        tcount = len(types)
        if tcount > best_count:
            best_count = tcount
            best = [(team, types)]
        elif tcount == best_count:
            best.append((team, types))

    return best_count, best


def main():
    k = int(input("Enter a number"))
    count, winners = strongest_squads(pokedex, k)
    print(f"Strongest type coverage for k={k}: {count} distinct types")
    for team, types in winners:
        print(f"- Team: {', '.join(team)}")
        print(f"  Types ({len(types)}): {', '.join(sorted(types))}")
